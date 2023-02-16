# Date    : 28/09/22 8:53 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import requests

import configure
from Helper_Functions.customErrorBox import CustomBox
from Backend.smtp_services import sendVerifyOtp, sendResetOtp
from Screens.Refactor.customWidgets import CustomWidgets
from Screens.Refactor.loginHeaderGUI import loginHeaderGUI
from Screens.Validator.validator import validate_email, validate_enrollment


class ForgotPassword(ctk.CTkFrame):
    """
    Frame to show the forgot password screen
    """
    credentials = {}

    def __init__(self, **kwargs):
        """
        constructor of the class to initialize the frame
        """
        super().__init__(kwargs['parent'], fg_color=configure.very_dark_gray)
        self._controller = kwargs['controller']
        self.email_error_label = ctk.CTkLabel()
        self._forgotPasswordGUI()

    def _forgotPasswordGUI(self):
        loginHeaderGUI(self)
        CustomWidgets.customHeaderLabel(self, 'RECOVERY').grid(row=3, column=0, sticky='w')
        self.email_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.email_entry = CustomWidgets.customEntry(parent=self.email_frame, placeholder='E-mail address')
        self.email_entry.grid(row=0, column=0, columnspan=2)
        self.email_frame.grid(row=4, column=0, columnspan=2, pady=10)

        def validate():
            try:
                requests.get('https://google.com')
                try:
                    ForgotPassword.credentials['otp'] = sendResetOtp(self.email_entry.get())
                    ForgotPassword.credentials['email'] = self.email_entry.get()
                    self._controller.showFrame('Verify', self)
                except Exception as e:
                    obj = CustomBox()
                    obj.errorBox('Error', 'Something went wrong ' + '(' + str(e.args[0]) + ')')
            except requests.exceptions.ConnectionError:
                self._controller.showFrame('NoInternet', self)

        CustomWidgets.customButton(parent=self, text='BACK', command=lambda: self._controller.showFrame('Login', self),
                                   fg_color=configure.dark_gray, text_color=configure.white,
                                   hover_color=configure.very_dark_gray).grid(row=5, column=0, pady=10)
        CustomWidgets.customButton(parent=self, text='SEND', command=validate).grid(row=5, column=1, pady=10)
