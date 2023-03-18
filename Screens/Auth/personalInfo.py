# Date    : 01/10/22 01:00 pm
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0
import customtkinter as ctk
import requests
from numpy.core.defchararray import strip
from phonenumbers import parse, carrier, NumberParseException
import configure
from Backend.signup_sqlite_services import SignupSqliteServices
from Helper_Functions.customErrorBox import CustomBox
from Backend.smtp_services import sendVerifyOtp
from Screens.Refactor.customWidgets import CustomWidgets
from Screens.Refactor.loginHeaderGUI import loginHeaderGUI
from Screens.Auth.signup import Signup


class UserDetailsStack(Signup):

    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self._controller = kwargs['controller']
        self.container = ctk.CTkFrame(self, fg_color=configure.very_dark_gray)
        loginHeaderGUI(self.container)
        CustomWidgets.customHeaderLabel(self.container, 'Personal Info').grid(row=3, column=0, sticky='w')
        self.container.grid(row=0, column=0, sticky='nsew')
        self.frames = {}
        self.frame_stack = (PersonalInfo, ContactInfo, Signup)
        for window in self.frame_stack:
            page_name = window.__name__
            frame = window(parent=self.container, controller=self, parent_controller=self._controller)
            self.frames[page_name] = frame
            frame.grid(row=4, column=0, sticky='nsew')
        self.showFrame("PersonalInfo")

    def showFrame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class PersonalInfo(UserDetailsStack):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.dob_error_label = ctk.CTkLabel()
        self._controller = kwargs['controller']
        self._parent_controller = kwargs['parent_controller']
        self.first_error_label = ctk.CTkLabel()
        self.last_error_label = ctk.CTkLabel()
        self.sql = SignupSqliteServices()
        self._personalInfoGUI()

    def validate_date(self):
        if self._switch(0) and self._switch(1) and self._switch(2):
            return True
        else:
            return False

    def _switch(self, index):
        match index:
            case 0:
                if len(self.day.get()) == 2 and self.day.get().isdigit() and int(self.day.get()) <= 31:
                    self.day.configure(border_color=configure.dark_gray)
                    self.month.focus()
                    return True
                else:
                    self.day.configure(border_color=configure.light_cyan)
                    return False
            case 1:
                if len(self.month.get()) == 2 and self.month.get().isdigit() and int(self.month.get()) <= 12:
                    self.month.configure(border_color=configure.dark_gray)
                    self.year.focus()
                    return True
                else:
                    self.month.configure(border_color=configure.light_cyan)
                    return False
            case 2:
                if len(self.year.get()) == 4 and self.year.get().isdigit() and 2021 >= int(self.year.get()) >= 1900:
                    self.year.configure(border_color=configure.dark_gray)
                    return True
                else:
                    self.year.configure(border_color=configure.light_cyan)
                    return False

    def _validate_fields(self, index):
        match index:
            case 0:
                if strip(self.firstname_entry.get()) == '':
                    self.first_error_label = CustomWidgets.customErrorLabel(parent=self.firstname_frame,
                                                                            error_text='First name is required')
                    self.first_error_label.grid(row=1, column=0, columnspan=2)
                    self.firstname_entry.configure(border_color=configure.light_cyan)
                    return False
                else:
                    self.first_error_label.destroy()
                    self.firstname_entry.configure(border_color=configure.dark_gray)
                    return True
            case 1:
                if strip(self.lastname_entry.get()) == '':
                    self.last_error_label = CustomWidgets.customErrorLabel(parent=self.lastname_frame,
                                                                           error_text='Last name is required')
                    self.last_error_label.grid(row=1, column=0, columnspan=2)
                    self.lastname_entry.configure(border_color=configure.light_cyan)
                    return False
                else:
                    self.lastname_entry.configure(border_color=configure.dark_gray)
                    self.last_error_label.destroy()
                    return True

    def _personalInfoGUI(self):
        self.gender_val = ctk.IntVar(value=0)
        self.firstname_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.firstname_entry = CustomWidgets.customEntry(parent=self.firstname_frame, placeholder='First name')
        self.firstname_entry.grid(row=0, column=0, columnspan=2)
        self.firstname_entry.bind('<FocusOut>', lambda event: self._validate_fields(0))
        self.firstname_frame.grid(row=4, column=0, columnspan=2, pady=10)
        self.lastname_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.lastname_entry = CustomWidgets.customEntry(parent=self.lastname_frame, placeholder='Last name')
        self.lastname_entry.grid(row=0, column=0, columnspan=2)
        self.lastname_entry.bind('<FocusOut>', lambda event: self._validate_fields(1))
        self.lastname_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.birth_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        ctk.CTkLabel(master=self.birth_frame, text='DoB', text_font=(configure.font, 12, 'bold'),
                     width=70, anchor='w').grid(row=0, column=0, sticky='w')
        self.day = CustomWidgets.customEntry(parent=self.birth_frame, placeholder='DD', width=40)
        self.day.bind('<KeyRelease>', lambda event: self._switch(0))
        self.day.grid(row=0, column=1)
        ctk.CTkLabel(master=self.birth_frame, text='/', text_font=(configure.font, 12, 'bold'),
                     width=30).grid(row=0, column=2)
        self.month = CustomWidgets.customEntry(parent=self.birth_frame, placeholder='MM', width=40)
        self.month.bind('<KeyRelease>', lambda event: self._switch(1))
        self.month.grid(row=0, column=3)
        ctk.CTkLabel(master=self.birth_frame, text='/', text_font=(configure.font, 12, 'bold'),
                     width=30).grid(row=0, column=4)
        self.year = CustomWidgets.customEntry(parent=self.birth_frame, placeholder='YYYY', width=55)
        self.year.bind('<KeyRelease>', lambda event: self._switch(2))
        self.year.grid(row=0, column=5)
        self.birth_frame.grid(row=6, column=0, columnspan=2, pady=10)
        self.gender_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        ctk.CTkLabel(master=self, text='Gender', text_font=(configure.font, 12, 'bold'), anchor='w').grid(row=7,
                                                                                                          column=0,
                                                                                                          sticky='w')
        self.male = ctk.CTkRadioButton(master=self.gender_frame, variable=self.gender_val, value=1,
                                       text_font=(configure.font, 12),
                                       text='Male', border_color=configure.dark_gray, hover_color=configure.light_cyan,
                                       fg_color=configure.vivid_cyan, border_width_checked=5)
        self.male.grid(row=1, column=0, sticky='w')
        self.female = ctk.CTkRadioButton(master=self.gender_frame, variable=self.gender_val, value=2,
                                         text_font=(configure.font, 12),
                                         text='Female', border_color=configure.dark_gray,
                                         hover_color=configure.light_cyan, fg_color=configure.vivid_cyan,
                                         border_width_checked=5)
        self.female.grid(row=2, column=0, sticky='w', pady=10)
        self.other = ctk.CTkRadioButton(master=self.gender_frame, variable=self.gender_val, value=3,
                                        text_font=(configure.font, 12),
                                        text='Prefer not to say', border_color=configure.dark_gray,
                                        hover_color=configure.light_cyan, fg_color=configure.vivid_cyan,
                                        border_width_checked=5)
        self.other.grid(row=3, column=0, sticky='w')
        self.gender_frame.grid(row=8, column=0, columnspan=2, pady=10)
        self.male.select()

        def _verify():
            if self._validate_fields(0) and self._validate_fields(1) and self.validate_date():
                Signup.credentials['first name'] = self.firstname_entry.get()
                Signup.credentials['last name'] = self.lastname_entry.get()
                Signup.credentials['date of birth'] = self.day.get() + '-' + self.month.get() + '-' + self.year.get()
                if self.gender_val.get() == 1:
                    Signup.credentials['gender'] = 'Male'
                elif self.gender_val.get() == 2:
                    Signup.credentials['gender'] = 'Female'
                else:
                    Signup.credentials['gender'] = 'None'
                self.sql.insertPersonalDetails(self.firstname_entry.get(), self.lastname_entry.get(),
                                               Signup.credentials['date of birth'], Signup.credentials['gender'],
                                               Signup.credentials['email'])
                self._controller.showFrame('ContactInfo')
            else:
                self._validate_fields(0)
                self._validate_fields(1)
                self.validate_date()

        self.button_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        CustomWidgets.customButton(parent=self.button_frame, text='BACK', fg_color=configure.dark_gray,
                                   command=lambda: self._parent_controller.showFrame('Signup', self),
                                   text_color=configure.white,
                                   hover_color=configure.very_dark_gray).grid(row=0, column=0, sticky='nsew', padx=10)
        CustomWidgets.customButton(parent=self.button_frame, text='NEXT', command=lambda: _verify()).grid(row=0,
                                                                                                          column=1,
                                                                                                          sticky='nsew',
                                                                                                          padx=10)
        self.button_frame.grid(row=9, column=0, columnspan=2, pady=10)


class ContactInfo(PersonalInfo):
    phonenumber = None
    enrollment = None

    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.enroll_error_label = ctk.CTkLabel()
        self._controller = kwargs['controller']
        self._parent_controller = kwargs['parent_controller']
        self.phone_error_label = ctk.CTkLabel()
        self.sql = SignupSqliteServices()
        self._contactInfoGUI()

    def _validate_fields(self, index):
        match index:
            case 0:
                phone = self.phone_entry.get()
                if strip(phone) == '':
                    if self.phone_error_label.winfo_exists():
                        self.phone_error_label.destroy()
                    self.phone_error_label = CustomWidgets.customErrorLabel(parent=self.phone_frame,
                                                                            error_text='Phone number is required')
                    self.phone_error_label.grid(row=1, column=0, columnspan=2)
                    self.phone_entry.configure(border_color=configure.light_cyan)
                    return False
                if not phone.isdigit() and phone.startswith('+'):
                    if self.phone_error_label.winfo_exists():
                        self.phone_error_label.destroy()
                    self.phone_error_label = CustomWidgets.customErrorLabel(parent=self.phone_frame,
                                                                            error_text='Invalid phone format\n '
                                                                                       '1234567890')
                    self.phone_error_label.grid(row=1, column=0, columnspan=2)
                    self.phone_entry.configure(border_color=configure.light_cyan)
                    return False
                if len(phone) < 10:
                    if self.phone_error_label.winfo_exists():
                        self.phone_error_label.destroy()
                    self.phone_error_label = CustomWidgets.customErrorLabel(parent=self.phone_frame,
                                                                            error_text='Phone number is too short')
                    self.phone_error_label.grid(row=1, column=0, columnspan=2)
                    self.phone_entry.configure(border_color=configure.light_cyan)
                    return False
                else:
                    if self.phone_error_label.winfo_exists():
                        self.phone_error_label.destroy()
                    try:
                        phone = parse("+91" + phone, "IN")
                        info = [carrier.name_for_number(phone, "en")]
                    except NumberParseException as e:
                        info = ['Invalid', e.args]
                    self.phone_error_label = CustomWidgets.customErrorLabel(parent=self.phone_frame,
                                                                            error_text=info)
                    self.phone_error_label.grid(row=1, column=0, columnspan=2)
                    self.phone_entry.configure(border_color=configure.dark_gray)
                    return True
            case 1:
                enroll = self.enroll_entry.get()
                if len(enroll) == 6 and enroll != configure.obj.getAdminCode():
                    if self.enroll_error_label.winfo_exists():
                        self.enroll_error_label.destroy()
                    self.enroll_error_label = CustomWidgets.customErrorLabel(parent=self.enroll_frame,
                                                                             error_text='Wrong Admin Code')
                    self.enroll_error_label.grid(row=1, column=0, columnspan=2)
                    self.enroll_entry.configure(border_color=configure.light_cyan)
                    return False
                if strip(enroll) == '':
                    if self.enroll_error_label.winfo_exists():
                        self.enroll_error_label.destroy()
                    self.enroll_error_label = CustomWidgets.customErrorLabel(parent=self.enroll_frame,
                                                                             error_text='Admin Code/Application Id/\n'
                                                                                        'Enrollment number is required')
                    self.enroll_error_label.grid(row=1, column=0, columnspan=2)
                    self.enroll_entry.configure(border_color=configure.light_cyan)
                    return False
                if len(enroll) < 6 or len(enroll) > 12:
                    if self.enroll_error_label.winfo_exists():
                        self.enroll_error_label.destroy()
                    self.enroll_error_label = CustomWidgets.customErrorLabel(parent=self.enroll_frame,
                                                                             error_text='Invalid Enrollment No/ Admin '
                                                                                        'Code')
                    self.enroll_error_label.grid(row=1, column=0, columnspan=2)
                    self.enroll_entry.configure(border_color=configure.light_cyan)
                    return False
                else:
                    if self.enroll_error_label.winfo_exists():
                        self.enroll_error_label.destroy()
                    self.enroll_entry.configure(border_color=configure.dark_gray)
                    return True

    def _contactInfoGUI(self):
        self.phone_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.phone_entry = CustomWidgets.customEntry(parent=self.phone_frame, placeholder='1234567890')
        self.phone_entry.grid(row=0, column=0, columnspan=2)
        self.phone_entry.bind('<FocusOut>', lambda event: self._validate_fields(0))
        self.phone_frame.grid(row=4, column=0, columnspan=2, pady=10)
        self.enroll_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.enroll_entry = CustomWidgets.customEntry(parent=self.enroll_frame,
                                                      placeholder='Admin Code/Application Id/Enrollment Number')
        self.enroll_entry.grid(row=0, column=0, columnspan=2)
        self.enroll_entry.bind('<FocusOut>', lambda event: self._validate_fields(1))
        self.enroll_frame.grid(row=5, column=0, columnspan=2, pady=10)

        def _verify():
            if self._validate_fields(0) and self._validate_fields(1):
                try:
                    requests.get('https://google.com')
                    try:
                        Signup.credentials['otp'] = sendVerifyOtp(Signup.credentials['email'])
                        Signup.credentials['phone number'] = self.phone_entry.get()
                        Signup.credentials['enrollment'] = self.enroll_entry.get()
                        self.sql.insertContactDetails(self.phone_entry.get(), self.enroll_entry.get(),
                                                      Signup.credentials['email'])
                        self._parent_controller.showFrame('Verify', self)
                    except Exception as e:
                        # Custom messagebox object
                        self.obj = CustomBox()
                        self.obj.errorBox('Error', 'Something went wrong ' + '(' + str(e) + ')')
                except requests.exceptions.ConnectionError as e:
                    self._parent_controller.showFrame('NoInternet', self)
            else:
                self._validate_fields(0)
                self._validate_fields(1)

        self.button_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        CustomWidgets.customButton(parent=self.button_frame, text='BACK', fg_color=configure.dark_gray,
                                   command=lambda: self._controller.showFrame('PersonalInfo'),
                                   text_color=configure.white,
                                   hover_color=configure.very_dark_gray).grid(row=0, column=0, sticky='nsew', padx=10)
        CustomWidgets.customButton(parent=self.button_frame, text='VERIFY',
                                   command=lambda: _verify()).grid(row=0, column=1, sticky='nsew', padx=10)
        self.button_frame.grid(row=6, column=0, columnspan=2, pady=10)
