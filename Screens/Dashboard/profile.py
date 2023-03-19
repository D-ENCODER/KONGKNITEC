# Date    : 15/02/23 6:53 pm
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0
import customtkinter as ctk
from numpy.core.defchararray import strip
import configure
from Backend.SqliteServices.signup_sqlite_services import SignupSqliteServices
from Screens.Refactor.customWidgets import CustomWidgets
from Screens.Validator.validatorLogic import Validator


class Profile(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.__parent = kwargs['parent']
        self.__controller = kwargs['controller']
        self.email_error_label = CustomWidgets.customErrorLabel(parent=self, error_text='')
        self.sql = SignupSqliteServices()
        self.__profileGUI()

    def __profileGUI(self):
        CustomWidgets.customHeaderLabel(self, 'EDIT PROFILE').grid(row=0, column=0)
        ctk.CTkLabel(master=self, text='', height=15).grid(row=1, column=0, columnspan=2)
        self.firstname_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        ctk.CTkLabel(master=self.firstname_frame, text='First Name', text_font=(configure.font, 12, 'bold'),
                     width=30).grid(row=1, column=0, sticky='e')
        self.firstname_entry = CustomWidgets.customEntry(parent=self.firstname_frame, placeholder='Maulik')
        self.firstname_entry.grid(row=1, column=1, padx=50)
        self.firstname_entry.bind('<FocusOut>', lambda event: self._validate_fields(0))
        self.firstname_frame.grid(row=2, column=2, pady=10)
        self.lastname_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        ctk.CTkLabel(master=self.lastname_frame, text='Last Name', text_font=(configure.font, 12, 'bold'),
                     width=30).grid(row=1, column=0, sticky='e')
        self.lastname_entry = CustomWidgets.customEntry(parent=self.lastname_frame, placeholder='Parmar')
        self.lastname_entry.grid(row=1, column=1, padx=50)
        self.lastname_entry.bind('<FocusOut>', lambda event: self._validate_fields(1))
        self.lastname_frame.grid(row=3, column=2, pady=10)
        self.email_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        ctk.CTkLabel(master=self.email_frame, text='E-mail', text_font=(configure.font, 12, 'bold'),
                     width=30).grid(row=1, column=0, sticky='e')
        self.email_entry = CustomWidgets.customEntry(parent=self.email_frame, placeholder='mm.2004.parmar@gmail.com')
        self.email_entry.grid(row=1, column=1, padx=50)
        self.email_frame.grid(row=4, column=2, pady=10)
        self.email_entry.bind('<FocusOut>', lambda event: self.validateEmail(parent=self))
        self.phone_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        ctk.CTkLabel(master=self, text='Contact', text_font=(configure.font, 12, 'bold'),
                     width=30).grid(row=5, column=1, sticky='e')
        self.phone_entry = CustomWidgets.customEntry(parent=self.phone_frame, placeholder='1234567890')
        self.phone_entry.grid(row=5, column=2)
        self.phone_entry.bind('<FocusOut>', lambda event: self._validate_fields(0))
        self.phone_frame.grid(row=5, column=2, pady=10, padx=25)
        self.birth_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        ctk.CTkLabel(master=self.birth_frame, text='DoB', text_font=(configure.font, 12, 'bold'),
                     width=70).grid(row=6, column=1, sticky='e')
        self.day = CustomWidgets.customEntry(parent=self.birth_frame, placeholder='DD', width=40)
        self.day.bind('<KeyRelease>', lambda event: self._switch(0))
        self.day.grid(row=6, column=2)
        ctk.CTkLabel(master=self.birth_frame, text='/', text_font=(configure.font, 12, 'bold'),
                     width=30).grid(row=6, column=3)
        self.month = CustomWidgets.customEntry(parent=self.birth_frame, placeholder='MM', width=40)
        self.month.bind('<KeyRelease>', lambda event: self._switch(1))
        self.month.grid(row=6, column=4)
        ctk.CTkLabel(master=self.birth_frame, text='/', text_font=(configure.font, 12, 'bold'),
                     width=30).grid(row=6, column=5)
        self.year = CustomWidgets.customEntry(parent=self.birth_frame, placeholder='YYYY', width=55)
        self.year.bind('<KeyRelease>', lambda event: self._switch(2))
        self.year.grid(row=6, column=6)
        self.birth_frame.grid(row=6, column=1, columnspan=2, pady=10, padx=25)
        ctk.CTkLabel(master=self, text='', height=40).grid(row=7, column=1, columnspan=2)
        self.save = ctk.CTkButton(master=self, text='Save',
                                  text_font=(configure.font, 13, "bold"),
                                  text_color=configure.very_dark_gray, fg_color=configure.vivid_cyan,
                                  hover_color=configure.light_cyan, width=100, height=35, corner_radius=10)
        self.save.grid(row=8, column=2)

    def validateEmail(self):
        """
        This is the function which is used to validate the email address when the focus pops out of the entry
        :return: None
        """
        if Validator.validate_email(self.email_entry.get())[0]:
            # If the email is valid then remove the error label
            self.email_error_label.destroy()
            # reset the color of the entry to default
            self.email_entry.configure(border_color=configure.dark_gray)
            return True
        else:
            # checks if the error label is already present or not
            if self.email_error_label.winfo_exists():
                # If the error label is already present then destroy it
                self.email_error_label.destroy()
            # Create the custom error label
            self.email_error_label = CustomWidgets.customErrorLabel(parent=self.email_frame,
                                                                    error_text=Validator.validate_email(
                                                                        self.email_entry.get())[1])
            # Place the error label in the grid layout
            self.email_error_label.grid(row=1, column=0, columnspan=2)
            # Change the color of the entry to dominant color
            self.email_entry.configure(border_color=configure.light_cyan)
            return False

    def _validate_fields(self, index):
        match index:
            case 0:
                if strip(self.firstname_entry.get()) == '':
                    self.first_error_label = CustomWidgets.customErrorLabel(parent=self.firstname_frame,
                                                                            error_text='First name is required')
                    self.first_error_label.grid(row=2, column=1)
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
                    self.last_error_label.grid(row=2, column=1)
                    self.lastname_entry.configure(border_color=configure.light_cyan)
                    return False
                else:
                    self.lastname_entry.configure(border_color=configure.dark_gray)
                    self.last_error_label.destroy()
                    return True

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
