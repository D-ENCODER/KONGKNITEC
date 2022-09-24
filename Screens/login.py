# Date    : 12/08/22 6:54 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
from PIL import Image, ImageTk
import configure
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
        # Enlarging the scope og the controller variable
        self._controller = controller
        # Load the show password icon and hide password icon
        self._show_icon = Login._load_image(self, "Icons/hide.png", 17)
        self._hide_icon = Login._load_image(self, "Icons/show.png", 17)
        # Call the login GUI
        self._loginGUI()

    @staticmethod
    def _load_image(frame, path, image_size):
        """
        This is the static method which is used to load the image and resize it
        :param frame: The frame in which the image is to be loaded
        :param path: The path of the image
        :param image_size: The size of the image
        :return: The resized image
        """
        return ImageTk.PhotoImage(master=frame, image=Image.open(path).resize((image_size, image_size)))

    def _loginGUI(self):
        """
        This is the method which is used to create the login GUI and holds most values of the GUI
        """
        # Call the header GUI
        header_gui(self)
        # Create the header label
        CustomWidgets.customHeaderLabel(self, 'LOGIN').grid(row=3, column=0)
        # Create the email entry
        email_entry = CustomWidgets.customEntry(self, 'E-mail address')
        # Placing the email entry in the grid layout
        email_entry.grid(row=4, column=0, columnspan=2, pady=10)

        # This function is used to validate the email address when the focus pops out of the entry
        def _validate_email(event):
            """
            This is the function which is used to validate the email address when the focus pops out of the entry
            :param event: The event which is used to get the focus out of the entry
            :return: None
            """
            if Validator.validate_email(email_entry.get()):
                email_entry.configure(border_color=configure.hyperlink_color)
            else:
                email_entry.configure(border_color=configure.dominant_color)

        # Binding the function to the entry widget to validate the email address
        email_entry.bind('<FocusOut>', _validate_email)
        # Create the password entry
        password_entry = CustomWidgets.customEntry(self, 'Password', obfuscated=True)
        # Placing the password entry in the grid layout
        password_entry.grid(row=5, column=0, columnspan=2, pady=10)

        def _validate_password(event):
            """
            This is the function which is used to validate the password when the focus pops out of the entry
            :param event: The event which is used to get the focus out of the entry
            :return: None
            """
            if Validator.validate_password(password_entry.get()):
                password_entry.configure(border_color=configure.hyperlink_color)
            else:
                password_entry.configure(border_color=configure.dominant_color)

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
            if Validator.validate_email(email_entry.get()) and Validator.validate_password(password_entry.get()):
                self._controller.show_frame("Home")
            else:
                # if email is not valid then show the error message
                if not Validator.validate_email(email_entry.get()):
                    # Invoke the error message
                    email_entry.configure(border_color=configure.dominant_color)
                # if password is not valid then show the error message
                if not Validator.validate_password(password_entry.get()):
                    # Invoke the error message
                    password_entry.configure(border_color=configure.dominant_color)
        # Create the show password button and placing on the same entry box
        button = ctk.CTkButton(master=self, image=self._hide_icon, width=20, height=20, text="",
                               fg_color=configure.hyperlink_color, corner_radius=180, cursor="hand2", border=False,
                               hover=False, command=lambda: _show_password())
        button.grid(row=5, column=1, sticky='e', padx=10)
        # Creating the forgot password hyper label and placing it in the grid layout
        ctk.CTkButton(master=self, text='FORGOT PASSWORD ?', cursor="hand2",
                      fg_color=configure.hover_color, text_font=(configure.font, 8, "bold"),
                      hover_color=configure.hover_color,
                      text_color=configure.dominant_color).grid(row=6, column=1, sticky='e')
        # Creating the login button and placing it in the grid layout
        CustomWidgets.customButton(self, 'LOGIN', lambda: _verifyLogin()).grid(row=7, column=0, columnspan=2, pady=10)
        # Creating the signup hyper label and placing it in the grid layout
        footer_gui(self, "Don't have an account? ", self._controller, "Sign-up", "Signup")
