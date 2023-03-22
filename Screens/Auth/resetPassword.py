# Date    : 30/09/22 6:12 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import requests
from PIL import Image

import configure
from Backend.FirebaseServices.authenticationServices import AuthenticationServices
from Backend.encryptor import encrypt
from Backend.smtp_services import sendPasswordChanged
from Helper_Functions.loadImage import loadImage
from Screens.Refactor.customWidgets import CustomWidgets
from Screens.Refactor.loginHeaderGUI import loginHeaderGUI
from Screens.Validator.validator import validate_password
from Screens.Auth.forgotPassword import ForgotPassword


class ResetPassword(ForgotPassword):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self._controller = kwargs['controller']
        self.password_error_label = ctk.CTkLabel(master=self)
        self._show_icon = ctk.CTkImage(Image.open("Assets/hide.png"), size=(17, 17))
        self._hide_icon = ctk.CTkImage(Image.open("Assets/show.png"), size=(17, 17))
        self.confirm_password_error_label = ctk.CTkLabel(master=self)
        self.obj = AuthenticationServices()
        self._resetPasswordGUI()

    def _resetPasswordGUI(self):
        self.frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.frame.grid(row=0, column=0, padx=(configure.screen_width - 300) / 2, pady=(configure.screen_height - 600) / 2)
        loginHeaderGUI(self.frame)
        CustomWidgets.customHeaderLabel(self.frame, 'RESET').grid(row=3, column=0, sticky='w')
        self.password_frame = ctk.CTkFrame(master=self.frame, fg_color=configure.very_dark_gray)
        # Calling the password entry label
        self.password_entry = CustomWidgets.customEntry(parent=self.password_frame, placeholder='Password',
                                                        obfuscated=True)
        # Placing the password entry label
        self.password_entry.grid(row=0, column=0, columnspan=2)
        # Placing the password frame into the grid layout
        self.password_frame.grid(row=5, column=0, columnspan=2, pady=10)
        # Creating a frame for confirm password and error box label
        self.confirm_password_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        # Calling the show password button
        self.confirm_password_entry = CustomWidgets.customEntry(parent=self.confirm_password_frame,
                                                                placeholder='Confirm Password', obfuscated=True)
        # Placing the confirm password entry label
        self.confirm_password_entry.grid(row=0, column=0, columnspan=2)
        # Placing the confirm password frame into the grid layout
        self.confirm_password_frame.grid(row=6, column=0, columnspan=2, pady=10)
        # Binding the validate password function to the password entry label
        self.password_entry.bind('<FocusOut>', lambda event: validate_password(parent=self))

        def validate_confirm_password(event=None):
            """
            This function is used to validate the confirm password entered by the user
            :param event: event which is triggered when the user presses the enter key
            :return: None
            """
            # Validating the confirm password entered by the user
            if self.password_entry.get() == self.confirm_password_entry.get():
                if self.confirm_password_error_label.winfo_exists():
                    self.confirm_password_error_label.destroy()
                # If the confirm password is valid then the confirm password entry label is set to the default color
                self.confirm_password_entry.configure(border_color=configure.dark_gray)
                return True
            else:
                # checks if the error label is already present or not
                if self.confirm_password_error_label.winfo_exists():
                    # if the error label is already present then it destroys the error label
                    self.confirm_password_error_label.destroy()
                # Calling the custom error label function
                self.confirm_password_error_label = CustomWidgets.customErrorLabel(parent=self.confirm_password_frame,
                                                                                   error_text='Password does not match')
                # Placing the error label into the grid layout
                self.confirm_password_error_label.grid(row=1, column=0, columnspan=2)
                # If the confirm password is invalid then the confirm password entry label is set to the error color
                self.confirm_password_entry.configure(border_color=configure.light_cyan)
                return False

        self.confirm_password_entry.bind('<FocusOut>', validate_confirm_password)

        def show_password():
            """
            This function is used to show the password entered by the user
            :return: None
            """
            # If the password is obfuscated then the password is shown
            self.password_entry.configure(show='')
            # If the confirm password is obfuscated then the confirm password is shown
            self.confirm_password_entry.configure(show='')
            # Changing the show password button to the hide password button
            button.configure(image=self._show_icon, command=lambda: hide_password())

        def hide_password():
            """
            This function is used to hide the password entered by the user
            :return: None
            """
            # If the password is shown then the password is obfuscated
            self.password_entry.configure(show='•')
            # If the confirm password is shown then the confirm password is obfuscated
            self.confirm_password_entry.configure(show='•')
            # Changing the hide password button to the show password button
            button.configure(image=self._hide_icon, command=lambda: show_password())

        def _verifyReset():
            """
            This function is used to verify the sign-up details entered by the user
            :return:
            """
            # Validating the email address, password and confirm password entered by the user
            if validate_password(parent=self) and validate_confirm_password():
                password = encrypt(self.password_entry.get())
                try:
                    requests.get('https://google.com')
                    if self.obj.check_email_exists('Admin_details', ForgotPassword.credentials['Email']):
                        self.obj.dbUpdatePassword(ForgotPassword.credentials['Email'], password, True)
                        sendPasswordChanged(ForgotPassword.credentials['Email'])
                        self._controller.showFrame('Login', self)
                    elif self.obj.check_email_exists('User_details', ForgotPassword.credentials['Email']):
                        self.obj.dbUpdatePassword(ForgotPassword.credentials['Email'], password, False)
                        sendPasswordChanged(ForgotPassword.credentials['Email'])
                        self._controller.showFrame('Login')
                except requests.exceptions.ConnectionError:
                    self._controller.showFrame('NoInternet', self)
            else:
                # If the password is invalid then the error message is displayed
                if not validate_password(parent=self):
                    # If the password is invalid then the error message is displayed
                    validate_password(parent=self)
                # If the confirm password is invalid then the error message is displayed
                if validate_confirm_password():
                    # If the confirm password is invalid then the error message is displayed
                    validate_confirm_password()

        # Calling the show password button
        button = ctk.CTkButton(master=self.password_frame, image=self._hide_icon, width=20, height=20, text="",
                               fg_color=configure.dark_gray, corner_radius=180, cursor="hand2", border_width=0,
                               hover=False, command=lambda: show_password(), bg_color=configure.dark_gray)
        # Placing the show password button
        button.grid(row=0, column=1, sticky='e', padx=10)
        CustomWidgets.customButton(parent=self, text='RESET PASSWORD', command=lambda: _verifyReset()) \
            .grid(row=7, column=0, columnspan=2, pady=10)
