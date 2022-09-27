# Date    : 12/08/22 6:54 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import configure
from Helper_Functions.load_image import load_image
from Screens.Refactor.custom_widgets import CustomWidgets
from Screens.Refactor.footer_gui import footer_gui
from Screens.Refactor.header_gui import header_gui
from Screens.Validator.validator import Validator


class Login(ctk.CTkFrame):
    """
    This is the login frame which is used to log in into the application and holds all the widgets and functions
    """

    def __init__(self, parent, controller):
        """
        This is the constructor of the class which is used to initialize the class variables and call the login GUI
        :param parent: The parent of the frame which is the main frame
        :param controller: The controller of the frame
        """
        ctk.CTkFrame.__init__(self, parent, fg_color=configure.hover_color)
        # Initializing the error handlers
        self.email_error_label = ctk.CTkLabel()
        self.password_error_label = ctk.CTkLabel()
        # Enlarging the scope og the controller variable
        self._controller = controller
        # Load the show password icon and hide password icon
        self._show_icon = load_image(self, "Icons/hide.png", 17)
        self._hide_icon = load_image(self, "Icons/show.png", 17)
        # Call the login GUI
        self._loginGUI()

    def _loginGUI(self):
        """
        This is the method which is used to create the login GUI and holds most values of the GUI
        """
        # Call the header GUI
        header_gui(self)
        # Create the header label
        CustomWidgets.customHeaderLabel(self, 'LOGIN').grid(row=3, column=0)
        # Creating a frame for email and error box label
        email_frame = ctk.CTkFrame(master=self, fg_color=configure.hover_color)
        # Create the email entry
        email_entry = CustomWidgets.customEntry(email_frame, 'E-mail address')
        # Placing the email entry in the grid layout
        email_entry.grid(row=0, column=0, columnspan=2)
        # Placing the email frame into the grid layout
        email_frame.grid(row=4, column=0, columnspan=2, pady=10)

        # This function is used to validate the email address when the focus pops out of the entry
        def _validate_email(event=None):
            """
            This is the function which is used to validate the email address when the focus pops out of the entry
            :param event: The event which is used to get the focus out of the entry
            :return: None
            """
            if Validator.validate_email(email_entry.get())[0]:
                # If the email is valid then remove the error label
                self.email_error_label.destroy()
                # reset the color of the entry to default
                email_entry.configure(border_color=configure.hyperlink_color)
                return True
            else:
                # checks if the error label is already present or not
                if self.email_error_label.winfo_exists():
                    # If the error label is already present then destroy it
                    self.email_error_label.destroy()
                # Create the custom error label
                self.email_error_label = CustomWidgets.customErrorLabel(email_frame,
                                                                        Validator.validate_email(email_entry.get())[1])
                # Place the error label in the grid layout
                self.email_error_label.grid(row=1, column=0, columnspan=2)
                # Change the color of the entry to dominant color
                email_entry.configure(border_color=configure.dominant_color)
                return False

        # Binding the function to the entry widget to validate the email address
        email_entry.bind('<FocusOut>', _validate_email)
        # Creating a frame for password and error box label
        password_frame = ctk.CTkFrame(master=self, fg_color=configure.hover_color)
        # Create the password entry
        password_entry = CustomWidgets.customEntry(password_frame, 'Password', obfuscated=True)
        # Placing the password entry in the grid layout
        password_entry.grid(row=0, column=0, columnspan=2)
        # Placing the password entry in the grid layout
        password_frame.grid(row=5, column=0, columnspan=2, pady=10)

        def _validate_password(event=None):
            """
            This is the function which is used to validate the password when the focus pops out of the entry
            :param event: The event which is used to get the focus out of the entry
            :return: None
            """
            if Validator.validate_password(password_entry.get())[0]:
                # If the password is valid then remove the error label
                self.password_error_label.destroy()
                # reset the color of the entry to default
                password_entry.configure(border_color=configure.hyperlink_color)
                return True
            else:
                # checks if the error label is already present or not
                if self.password_error_label.winfo_exists():
                    # If the error label is already present then destroy it
                    self.password_error_label.destroy()
                # Create the custom error label
                self.password_error_label = CustomWidgets.customErrorLabel(password_frame,
                                                                           Validator.validate_password(
                                                                               password_entry.get())[1])
                # Place the error label in the grid layout
                self.password_error_label.grid(row=1, column=0, columnspan=2)
                # Change the color of the entry to dominant color
                password_entry.configure(border_color=configure.dominant_color)
                return False

        password_entry.bind('<FocusOut>', _validate_password)

        # This is the show password button and this adds the functionality to the show password button
        def _show_password():
            """
            This is the function which is used to show the password when the show password button is clicked
            :return: None
            """
            password_entry.configure(show='')
            # Change the image of the button to hide password icon
            button.configure(image=self._show_icon, command=lambda: _hide_password())

        # This is the hide password button and this adds the functionality to the hide password button
        def _hide_password():
            """
            This is the function which is used to hide the password when the hide password button is clicked
            :return: None
            """
            password_entry.configure(show='•')
            # Change the image of the button to show password icon
            button.configure(image=self._hide_icon, command=lambda: _show_password())

        # This is the verifyLogin function which is used to verify the login credentials and make sure that they
        # are valid and legit
        def _verifyLogin():
            # if email is valid and password is valid then login
            if _validate_password() and _validate_email():
                self._controller.show_frame("Home")
            else:
                # if email is not valid then show the error message
                if not _validate_password():
                    # Invoke the error message
                    _validate_password()
                # if password is not valid then show the error message
                if not _validate_email():
                    # Invoke the error message
                    _validate_email()

        # Create the show password button and placing on the same entry box
        button = ctk.CTkButton(master=password_frame, image=self._hide_icon, width=20, height=20, text="",
                               fg_color=configure.hyperlink_color, corner_radius=180, cursor="hand2", border=False,
                               hover=False, command=lambda: _show_password())
        button.grid(row=0, column=1, sticky='e', padx=10)
        # Creating the forgot password hyper label and placing it in the grid layout
        ctk.CTkButton(master=self, text='FORGOT PASSWORD ?', cursor="hand2",
                      fg_color=configure.hover_color, text_font=(configure.font, 8, "bold"),
                      hover_color=configure.hover_color,
                      text_color=configure.dominant_color).grid(row=6, column=1, sticky='e')
        # Creating the login button and placing it in the grid layout
        CustomWidgets.customButton(self, 'LOGIN', lambda: _verifyLogin()).grid(row=7, column=0, columnspan=2, pady=10)
        # Creating the signup hyper label and placing it in the grid layout
        footer_gui(self, "Don't have an account? ", self._controller, "Sign-up", "Signup")
