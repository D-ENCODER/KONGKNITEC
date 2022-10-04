# Date    : 01/10/22 01:00 pm
# Author  : Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0
import customtkinter as ctk
from numpy.core.defchararray import strip

import configure
from Screens.Refactor.custom_widgets import CustomWidgets
from Screens.Refactor.header_gui import header_gui
from Screens.Validator.validator import validate_fields


class PersonalInfo(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.dob_error_label = ctk.CTkLabel()
        self.fname = False
        self.lname = False
        self._controller = kwargs['controller']
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

    def _personalInfoGUI(self):
        header_gui(self)
        gender = ctk.IntVar(value=0)
        CustomWidgets.customHeaderLabel(self, 'Personal Info').grid(row=3, column=0, sticky='w')
        self.firstname_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.firstname_entry = CustomWidgets.customEntry(parent=self.firstname_frame, placeholder='First name')
        self.firstname_entry.grid(row=0, column=0, columnspan=2)
        self.first_error_label = CustomWidgets.customErrorLabel(self=self.firstname_frame,
                                                                error_text="This field is required")
        self.firstname_entry.bind('<FocusOut>', lambda event: validate_fields(parent=self, widget=self.firstname_entry,
                                                                              parent_frame=self.firstname_frame,
                                                                              error_widget=self.first_error_label,
                                                                              bool=self.fname))
        self.firstname_frame.grid(row=4, column=0, columnspan=2, pady=10)
        self.lastname_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.lastname_entry = CustomWidgets.customEntry(parent=self.lastname_frame, placeholder='Last name')
        self.lastname_entry.grid(row=0, column=0, columnspan=2)
        self.last_error_label = CustomWidgets.customErrorLabel(self=self.lastname_frame,
                                                               error_text="This field is required")
        self.lastname_entry.bind('<FocusOut>', lambda event: validate_fields(parent=self, widget=self.lastname_entry,
                                                                             parent_frame=self.lastname_frame,
                                                                             error_widget=self.last_error_label,
                                                                             bool=self.lname))
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
        self.male = ctk.CTkRadioButton(master=self.gender_frame, variable=gender, value=1,
                                       text_font=(configure.font, 12),
                                       text='Male', border_color=configure.dark_gray, hover_color=configure.light_cyan,
                                       fg_color=configure.vivid_cyan, border_width_checked=5)
        self.male.grid(row=1, column=0, sticky='w')
        self.female = ctk.CTkRadioButton(master=self.gender_frame, variable=gender, value=2,
                                         text_font=(configure.font, 12),
                                         text='Female', border_color=configure.dark_gray,
                                         hover_color=configure.light_cyan, fg_color=configure.vivid_cyan,
                                         border_width_checked=5)
        self.female.grid(row=2, column=0, sticky='w', pady=10)
        self.other = ctk.CTkRadioButton(master=self.gender_frame, variable=gender, value=3,
                                        text_font=(configure.font, 12),
                                        text='Prefer not to say', border_color=configure.dark_gray,
                                        hover_color=configure.light_cyan, fg_color=configure.vivid_cyan,
                                        border_width_checked=5)
        self.other.grid(row=3, column=0, sticky='w')
        self.gender_frame.grid(row=8, column=0, columnspan=2, pady=10)
        self.male.select()

        def verify():
            if strip(self.firstname_entry.get()) != '' and strip(self.lastname_entry.get()) != '' and self.validate_date():
                print("all good")
            else:
                print("not good")
                print(self.fname, self.lname, self.validate_date())

        self.button_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        CustomWidgets.customButton(self=self.button_frame, text='BACK', fg_color=configure.dark_gray,
                                   command=lambda: self._controller.show_frame('Signup'), text_color=configure.white,
                                   hover_color=configure.very_dark_gray).grid(row=0, column=0, sticky='nsew', padx=10)
        CustomWidgets.customButton(self=self.button_frame, text='NEXT', command=lambda: verify()).grid(row=0, column=1,
                                                                                                       sticky='nsew',
                                                                                                       padx=10)
        self.button_frame.grid(row=9, column=0, columnspan=2, pady=10)
