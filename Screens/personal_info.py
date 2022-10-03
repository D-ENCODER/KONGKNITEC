# Date    : 01/10/22 01:00 pm
# Author  : Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0
import customtkinter as ctk
import configure
from Screens.Refactor.custom_widgets import CustomWidgets
from Screens.Refactor.header_gui import header_gui
from Screens.Validator.validator import validate_fields


class PersonalInfo(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.dob_error_label = ctk.CTkLabel()
        self._controller = kwargs['controller']
        self._personalInfoGUI()

    def _personalInfoGUI(self):
        header_gui(self)
        radio = ctk.IntVar()
        CustomWidgets.customHeaderLabel(self, 'Personal Info').grid(row=3, column=0)
        self.firstname_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.firstname_entry = CustomWidgets.customEntry(parent=self.firstname_frame, placeholder='First name')
        self.firstname_entry.grid(row=0, column=0, columnspan=2)
        self.first_error_label = CustomWidgets.customErrorLabel(self=self.firstname_frame,
                                                                error_text="This field is required")
        self.firstname_entry.bind('<FocusOut>', lambda event: validate_fields(parent=self, widget=self.firstname_entry,
                                                                              parent_frame=self.firstname_frame,
                                                                              error_widget=self.first_error_label))
        self.firstname_frame.grid(row=4, column=0, columnspan=2, pady=10)
        self.lastname_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.lastname_entry = CustomWidgets.customEntry(parent=self.lastname_frame, placeholder='Last name')
        self.lastname_entry.grid(row=0, column=0, columnspan=2)
        self.last_error_label = CustomWidgets.customErrorLabel(self=self.lastname_frame,
                                                               error_text="This field is required")
        self.lastname_entry.bind('<FocusOut>', lambda event: validate_fields(parent=self, widget=self.lastname_entry,
                                                                             parent_frame=self.lastname_frame,
                                                                             error_widget=self.last_error_label))
        self.lastname_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.birth_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.birth_entry = CustomWidgets.customEntry(parent=self.birth_frame, placeholder='DD/MM/YYYY')
        self.birth_entry.grid(row=0, column=0, columnspan=2)
        self.birth_frame.grid(row=6, column=0, columnspan=2, pady=10)
        ctk.CTkLabel(master=self, text='Gender:', text_color=configure.white,
                     text_font=(configure.font, 11, 'bold'), anchor='w').grid(row=7, column=0, columnspan=2, sticky='w')
        ctk.CTkRadioButton(master=self, text='Male', value=1, variable=radio).grid(row=8, column=0, sticky='w')
        ctk.CTkRadioButton(master=self, text='Female', value=2, variable=radio).grid(row=8, column=0, sticky='e')
        ctk.CTkRadioButton(master=self, text='Not to say', value=3, variable=radio).grid(row=8, column=1, sticky='e')
        ctk.CTkLabel(master=self, text='', anchor='center').grid(row=9, column=0, columnspan=2)
        CustomWidgets.customButton(self=self, text='BACK', command=lambda: self._controller.show_frame('Login'),
                                   fg_color=configure.dark_gray, text_color=configure.white,
                                   hover_color=configure.very_dark_gray).grid(row=11, column=0, pady=10)
        CustomWidgets.customButton(self=self, text='SIGN-UP', command=None).grid(row=11, column=1, pady=10)
