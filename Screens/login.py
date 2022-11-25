# Date    : 12/08/22 6:54 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import requests

import configure
from Backend.encryptor import encrypt
from Helper_Functions.custom_error_box import CustomBox
from Helper_Functions.load_image import load_image
from Screens.Refactor.custom_widgets import CustomWidgets
from Screens.Refactor.footer_gui import footer_gui
from Screens.Refactor.header_gui import header_gui
from Screens.Validator.validator import validate_enrollment, validate_password


class Login(ctk.CTkFrame):
    """
    This is the login frame which is used to log in into the application and holds all the widgets and functions
    """

    def __init__(self, **kwargs):
        """
        This is the constructor of the class which is used to initialize the class variables and call the login GUI
        :param parent: The parent of the frame which is the main frame
        :param controller: The controller of the frame
        """
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self._parent = kwargs['parent']
        # Initializing the error handlers
        self.enrollment_error_label = ctk.CTkLabel()
        self.password_error_label = ctk.CTkLabel()
        # Enlarging the scope og the controller variable
        self._controller = kwargs['controller']
        # Load the show password icon and hide password icon
        self._show_icon = load_image(self, "Icons/hide.png", 17)
        self._hide_icon = load_image(self, "Icons/show.png", 17)
        # Call the login GUI
        self._loginGUI()

    def _loginGUI(self):
        """
        This is the method which is used to create the login GUI and holds most values of the GUI
        """
        self._parent.grid_configure(pady=(configure.screen_height - 600) / 2,
                                    padx=(configure.screen_width - 300) / 2)
        # Call the header GUI
        header_gui(self)
        # Create the header label
        CustomWidgets.customHeaderLabel(self, 'LOGIN').grid(row=3, column=0, sticky='w')
        # Creating a frame for email and error box label
        self.enrollment_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        # Create the email entry
        self.enrollment_entry = CustomWidgets.customEntry(parent=self.enrollment_frame,
                                                          placeholder='Admin Code/Application No/Enrollment No')
        # Placing the email entry in the grid layout
        self.enrollment_entry.grid(row=0, column=0, columnspan=2)
        # Placing the email frame into the grid layout
        self.enrollment_frame.grid(row=4, column=0, columnspan=2, pady=10)

        # Binding the function to the entry widget to validate the email address
        self.enrollment_entry.bind('<FocusOut>', lambda event: validate_enrollment(parent=self))
        # Creating a frame for password and error box label
        self.password_frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        # Create the password entry
        self.password_entry = CustomWidgets.customEntry(parent=self.password_frame, placeholder='Password',
                                                        obfuscated=True)
        # Placing the password entry in the grid layout
        self.password_entry.grid(row=0, column=0, columnspan=2)
        # Placing the password entry in the grid layout
        self.password_frame.grid(row=5, column=0, columnspan=2, pady=10)

        self.password_entry.bind('<FocusOut>', lambda event: validate_password(parent=self))

        # This is the show password button and this adds the functionality to the show password button
        def _show_password():
            """
            This is the function which is used to show the password when the show password button is clicked
            :return: None
            """
            self.password_entry.configure(show='')
            # Change the image of the button to hide password icon
            button.configure(image=self._show_icon, command=lambda: _hide_password())

        # This is the hide password button and this adds the functionality to the hide password button
        def _hide_password():
            """
            This is the function which is used to hide the password when the hide password button is clicked
            :return: None
            """
            self.password_entry.configure(show='•')
            # Change the image of the button to show password icon
            button.configure(image=self._hide_icon, command=lambda: _show_password())

        # This is the verifyLogin function which is used to verify the login credentials and make sure that they
        # are valid and legit
        def _verifyLogin():
            # if email is valid and password is valid then login
            if validate_password(parent=self) and validate_enrollment(parent=self):
                try:
                    requests.get('https://google.com')
                    if self.enrollment_entry.get().startswith('314'):
                        dbpassword = configure.obj.getLoginDetails(self.enrollment_entry.get(), True)
                    else:
                        dbpassword = configure.obj.getLoginDetails(self.enrollment_entry.get(), False)
                    if dbpassword is None:
                        obj = CustomBox()
                        obj.error_box('ERROR', 'No user found with this enrollment number')
                    elif dbpassword == encrypt(self.password_entry.get()):
                        configure.obj.dbLogin(int(self.enrollment_entry.get()))
                        self._controller.show_frame('Dashboard', self)
                    else:
                        obj = CustomBox()
                        obj.error_box('ERROR', 'Invalid credentials')
                except requests.exceptions.ConnectionError:
                    self._controller.show_frame('NoInternet', self)
            else:
                # if email is not valid then show the error message
                if not validate_password(parent=self):
                    # Invoke the error message
                    validate_password(parent=self)
                # if password is not valid then show the error message
                if not validate_enrollment(parent=self):
                    # Invoke the error message
                    validate_enrollment(parent=self)

        # Create the show password button and placing on the same entry box
        button = ctk.CTkButton(master=self.password_frame, image=self._hide_icon, width=20, height=20, text="",
                               fg_color=configure.dark_gray, corner_radius=180, cursor="hand2", border=False,
                               hover=False, command=lambda: _show_password())
        button.grid(row=0, column=1, sticky='e', padx=10)
        # Creating the forgot password hyper label and placing it in the grid layout
        CustomWidgets.customHyperlinkLabel(parent=self, text='FORGOT PASSWORD ?',
                                           command=lambda: self._controller.show_frame("ForgotPassword", self)). \
            grid(row=6, column=1, sticky='e')
        # Creating the login button and placing it in the grid layout
        CustomWidgets.customButton(parent=self, text='LOGIN', command=lambda: _verifyLogin()).grid(row=7, column=0,
                                                                                                   columnspan=2,
                                                                                                   pady=10)
        # Creating the signup hyper label and placing it in the grid layout
        footer_gui(self, "Don't have an account? ", self._controller, "Sign-up", "Signup")
