# Date    : 30/09/22 6:12 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import configure
from Backend.auth import FirebaseDatabase
from Backend.encryptor import encrypt
from Helper_Functions.load_image import load_image
from Screens.Refactor.custom_widgets import CustomWidgets
from Screens.Refactor.header_gui import header_gui
from Screens.Validator.validator import validate_password


class ResetPassword(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.hover_color)
        self._controller = kwargs['controller']
        self.password_error_label = ctk.CTkLabel()
        self._show_icon = load_image(self, "Icons/hide.png", 17)
        self._hide_icon = load_image(self, "Icons/show.png", 17)
        self._obj = FirebaseDatabase(name='reset')
        self.confirm_password_error_label = ctk.CTkLabel()
        self._resetPasswordGUI()

    def _resetPasswordGUI(self):
        header_gui(self)
        CustomWidgets.customHeaderLabel(self, 'RESET').grid(row=3, column=0)
        self.password_frame = ctk.CTkFrame(master=self, fg_color=configure.hover_color)
        # Calling the password entry label
        self.password_entry = CustomWidgets.customEntry(parent=self.password_frame, placeholder='Password',
                                                        obfuscated=True)
        # Placing the password entry label
        self.password_entry.grid(row=0, column=0, columnspan=2)
        # Placing the password frame into the grid layout
        self.password_frame.grid(row=5, column=0, columnspan=2, pady=10)
        # Creating a frame for confirm password and error box label
        self.confirm_password_frame = ctk.CTkFrame(master=self, fg_color=configure.hover_color)
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
                self.confirm_password_error_label.destroy()
                # If the confirm password is valid then the confirm password entry label is set to the default color
                self.confirm_password_entry.configure(border_color=configure.hyperlink_color)
            else:
                # checks if the error label is already present or not
                if self.confirm_password_error_label.winfo_exists():
                    # if the error label is already present then it destroys the error label
                    self.confirm_password_error_label.destroy()
                # Calling the custom error label function
                self.confirm_password_error_label = CustomWidgets.customErrorLabel(self=self.confirm_password_frame,
                                                                                   error_text='Password does not match')
                # Placing the error label into the grid layout
                self.confirm_password_error_label.grid(row=1, column=0, columnspan=2)
                # If the confirm password is invalid then the confirm password entry label is set to the error color
                self.confirm_password_entry.configure(border_color=configure.dominant_color)

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
                # password, key = encrypt(self.password_entry.get())
                print('hello')
                # self._obj.dbSignUp(password, key)
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
                               fg_color=configure.hyperlink_color, corner_radius=180, cursor="hand2", border=False,
                               hover=False, command=lambda: show_password())
        # Placing the show password button
        button.grid(row=0, column=1, sticky='e', padx=10)
        CustomWidgets.customButton(self, 'RESET PASSWORD', lambda: _verifyReset()).grid(row=7, column=0, columnspan=2,
                                                                                        pady=10)
