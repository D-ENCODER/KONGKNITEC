# Date    : 26/08/22 6:55 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
from PIL import ImageTk, Image
import configure
from Backend.auth import FirebaseDatabase
from Backend.encryptor import encrypt
from Screens.Refactor.custom_widgets import CustomWidgets
from Screens.Refactor.footer_gui import footer_gui
from Screens.Refactor.header_gui import header_gui
from Screens.Validator.validator import Validator


class Signup(ctk.CTkFrame):
    """
    This function is used to load the sign-up frame
    """

    def __init__(self, parent, controller):
        """
        This function is used to initialize the sign-up frame
        :param parent: parent frame which is the main frame
        :param controller: controller which is the main controller
        """
        ctk.CTkFrame.__init__(self, parent, fg_color=configure.hover_color)
        # Enlarging the scope of the controller so that it can be used in other functions
        self._controller = controller
        # Enlarging the scope of the database object so that it can be used in other functions
        self._obj = FirebaseDatabase()
        # Loading the show and hide icons so that it can be used further
        self._show_icon = self._load_image(self, "Icons/hide.png", 17)
        self._hide_icon = self._load_image(self, "Icons/show.png", 17)
        # Calling the sign-up GUI function
        self._signupGUI()

    @staticmethod
    def _load_image(frame, path, image_size):
        """
        This function is used to load the image
        :param frame: frame in which the image is to be loaded
        :param path: path of the image
        :param image_size: size of the image
        :return: image
        """
        # TODO: to refactor this function as this function is present in multiple files(login and signup)
        return ImageTk.PhotoImage(master=frame, image=Image.open(path).resize((image_size, image_size)))

    def _signupGUI(self):
        """
        This function is used to load the sign-up GUI and holds the logic of the sign-up GUI
        :return: None
        """
        header_gui(self)
        # Calling the header label
        CustomWidgets.customHeaderLabel(self, 'SIGN UP').grid(row=3, column=0)
        # Calling the email entry label
        email_entry = CustomWidgets.customEntry(self, 'E-mail address')
        # Placing the email entry label
        email_entry.grid(row=4, column=0, columnspan=2, pady=10)

        def _validate_email(event):
            """
            This function is used to validate the email address entered by the user
            :param event: event which is triggered when the user presses the enter key
            :return: None
            """
            # Validating the email address entered by the user
            if Validator.validate_email(email_entry.get()):
                # If the email address is valid then the email entry label is set to the default color
                email_entry.configure(border_color=configure.hyperlink_color)
            else:
                # If the email address is invalid then the email entry label is set to the error color
                email_entry.configure(border_color=configure.dominant_color)

        # Binding the validate email function to the email entry label
        email_entry.bind('<FocusOut>', _validate_email)
        # Calling the password entry label
        password_entry = CustomWidgets.customEntry(self, 'Password', obfuscated=True)
        # Placing the password entry label
        password_entry.grid(row=5, column=0, columnspan=2, pady=10)
        # Calling the show password button
        confirm_password_entry = CustomWidgets.customEntry(self, 'Confirm Password', obfuscated=True)
        # Placing the confirm password entry label
        confirm_password_entry.grid(row=6, column=0, columnspan=2, pady=10)

        def _validate_password(event):
            """
            This function is used to validate the password entered by the user
            :param event: event which is triggered when the user presses the enter key
            :return: None
            """
            # Validating the password entered by the user
            if Validator.validate_password(password_entry.get()):
                # If the password is valid then the password entry label is set to the default color
                password_entry.configure(border_color=configure.hyperlink_color)
            else:
                # If the password is invalid then the password entry label is set to the error color
                password_entry.configure(border_color=configure.dominant_color)

        # Binding the validate password function to the password entry label
        password_entry.bind('<FocusOut>', _validate_password)

        def _validate_confirm_password(event):
            """
            This function is used to validate the confirm password entered by the user
            :param event: event which is triggered when the user presses the enter key
            :return: None
            """
            # Validating the confirm password entered by the user
            if password_entry.get() == confirm_password_entry.get():
                # If the confirm password is valid then the confirm password entry label is set to the default color
                confirm_password_entry.configure(border_color=configure.hyperlink_color)
            else:
                # If the confirm password is invalid then the confirm password entry label is set to the error color
                confirm_password_entry.configure(border_color=configure.dominant_color)
        # Binding the validate confirm password function to the confirm password entry label
        confirm_password_entry.bind('<FocusOut>', _validate_confirm_password)

        def _show_password():
            """
            This function is used to show the password entered by the user
            :return: None
            """
            # If the password is obfuscated then the password is shown
            password_entry.configure(show='')
            # If the confirm password is obfuscated then the confirm password is shown
            confirm_password_entry.configure(show='')
            # Changing the show password button to the hide password button
            button.configure(image=self._show_icon, command=lambda: _hide_password())

        def _hide_password():
            """
            This function is used to hide the password entered by the user
            :return: None
            """
            # If the password is shown then the password is obfuscated
            password_entry.configure(show='•')
            # If the confirm password is shown then the confirm password is obfuscated
            confirm_password_entry.configure(show='•')
            # Changing the hide password button to the show password button
            button.configure(image=self._hide_icon, command=lambda: _show_password())

        def _verifySignup():
            """
            This function is used to verify the sign-up details entered by the user
            :return:
            """
            # Validating the email address, password and confirm password entered by the user
            if Validator.validate_email(email_entry.get()) and Validator.validate_password(password_entry.get()) \
                    and password_entry.get() == confirm_password_entry.get() and password_entry.get() != '':
                password, key = encrypt(password_entry.get())
                self._obj.dbSignUp(email_entry.get(), password, key)
            else:
                # If the email address, password or confirm password is invalid then the error message is displayed
                if not Validator.validate_email(email_entry.get()):
                    # If the email address is invalid then the error message is displayed
                    email_entry.configure(border_color=configure.dominant_color)
                # If the password is invalid then the error message is displayed
                if not Validator.validate_password(password_entry.get()):
                    # If the password is invalid then the error message is displayed
                    password_entry.configure(border_color=configure.dominant_color)
                # If the confirm password is invalid then the error message is displayed
                if password_entry.get() != confirm_password_entry.get() or password_entry.get() == '':
                    # If the confirm password is invalid then the error message is displayed
                    confirm_password_entry.configure(border_color=configure.dominant_color)
        # Calling the show password button
        button = ctk.CTkButton(master=self, image=self._hide_icon, width=20, height=20, text="",
                               fg_color=configure.hyperlink_color, corner_radius=180, cursor="hand2", border=False,
                               hover=False, command=lambda: _show_password())
        # Placing the show password button
        button.grid(row=5, column=1, sticky='e', padx=10)
        # Calling the sign-up button and placing it in the grid layout
        CustomWidgets.customButton(self, 'SIGN-UP', lambda: _verifySignup()).grid(row=7, column=0, columnspan=2,
                                                                                  pady=10)
        # Calling the footer gui function to display the footer
        footer_gui(self, "Already have an account?", self._controller, "Login", "Login")
