# Date    : 26/08/22 6:55 pm
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
from Screens.Refactor.footer_gui import footer_gui
from Screens.Refactor.header_gui import header_gui
from Screens.Validator.validator import validate_email, validate_password


class Signup(ctk.CTkFrame):
    """
    This function is used to load the sign-up frame
    """

    def __init__(self, **kwargs):
        """
        This function is used to initialize the sign-up frame
        :param parent: parent frame which is the main frame
        :param controller: controller which is the main controller
        """
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.hover_color)
        # Enlarging the scope of the controller so that it can be used in other functions
        self._controller = kwargs['controller']
        # Initializing the error handlers
        self.email_error_label = ctk.CTkLabel()
        self.password_error_label = ctk.CTkLabel()
        self.confirm_password_error_label = ctk.CTkLabel()
        # Enlarging the scope of the database object so that it can be used in other functions
        self._obj = FirebaseDatabase()
        # Loading the show and hide icons so that it can be used further
        self._show_icon = load_image(self, "Icons/hide.png", 17)
        self._hide_icon = load_image(self, "Icons/show.png", 17)
        # Calling the sign-up GUI function
        self._signupGUI()

    def _signupGUI(self):
        """
        This function is used to load the sign-up GUI and holds the logic of the sign-up GUI
        :return: None
        """
        header_gui(self)
        # Calling the header label
        CustomWidgets.customHeaderLabel(self, 'SIGN-UP').grid(row=3, column=0)
        # Creating a frame for email and error box label
        self.email_frame = ctk.CTkFrame(master=self, fg_color=configure.hover_color)
        # Calling the email entry label
        self.email_entry = CustomWidgets.customEntry(parent=self.email_frame, placeholder='E-mail address')
        # Placing the email entry in the grid layout
        self.email_entry.grid(row=0, column=0, columnspan=2)
        # Placing the email frame into the grid layout
        self.email_frame.grid(row=4, column=0, columnspan=2, pady=10)
        # Binding the validate email function to the email entry label
        self.email_entry.bind('<FocusOut>', lambda event: validate_email(parent=self))
        # Creating a frame for password and error box label
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
        self.password_entry.bind('<FocusOut>', validate_password)

        def _validate_confirm_password(event=None):
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
                self.confirm_password_error_label = CustomWidgets.customErrorLabel(self.confirm_password_frame,
                                                                                   'Password does not match')
                # Placing the error label into the grid layout
                self.confirm_password_error_label.grid(row=1, column=0, columnspan=2)
                # If the confirm password is invalid then the confirm password entry label is set to the error color
                self.confirm_password_entry.configure(border_color=configure.dominant_color)

        # Binding the validate confirm password function to the confirm password entry label
        self.confirm_password_entry.bind('<FocusOut>', _validate_confirm_password)

        def _show_password():
            """
            This function is used to show the password entered by the user
            :return: None
            """
            # If the password is obfuscated then the password is shown
            self.password_entry.configure(show='')
            # If the confirm password is obfuscated then the confirm password is shown
            self.confirm_password_entry.configure(show='')
            # Changing the show password button to the hide password button
            button.configure(image=self._show_icon, command=lambda: _hide_password())

        def _hide_password():
            """
            This function is used to hide the password entered by the user
            :return: None
            """
            # If the password is shown then the password is obfuscated
            self.password_entry.configure(show='•')
            # If the confirm password is shown then the confirm password is obfuscated
            self.confirm_password_entry.configure(show='•')
            # Changing the hide password button to the show password button
            button.configure(image=self._hide_icon, command=lambda: _show_password())

        def _verifySignup():
            """
            This function is used to verify the sign-up details entered by the user
            :return:
            """
            # Validating the email address, password and confirm password entered by the user
            if validate_email() and validate_password() and _validate_confirm_password():
                password, key = encrypt(self.password_entry.get())
                self._obj.dbSignUp(self.email_entry.get(), password, key)
            else:
                # If the email address, password or confirm password is invalid then the error message is displayed
                if not validate_email():
                    # If the email address is invalid then the error message is displayed
                    validate_email()
                # If the password is invalid then the error message is displayed
                if not validate_password():
                    # If the password is invalid then the error message is displayed
                    validate_password()
                # If the confirm password is invalid then the error message is displayed
                if _validate_confirm_password():
                    # If the confirm password is invalid then the error message is displayed
                    _validate_confirm_password()

        # Calling the show password button
        button = ctk.CTkButton(master=self.password_frame, image=self._hide_icon, width=20, height=20, text="",
                               fg_color=configure.hyperlink_color, corner_radius=180, cursor="hand2", border=False,
                               hover=False, command=lambda: _show_password())
        # Placing the show password button
        button.grid(row=0, column=1, sticky='e', padx=10)
        # Calling the sign-up button and placing it in the grid layout
        CustomWidgets.customButton(self, 'SIGN-UP', lambda: _verifySignup()).grid(row=7, column=0, columnspan=2,
                                                                                  pady=10)
        # Calling the footer gui function to display the footer
        footer_gui(self, "Already have an account?", self._controller, "Login", "Login")
