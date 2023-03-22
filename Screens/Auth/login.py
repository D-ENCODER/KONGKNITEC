# Date    : 12/08/22 6:54 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import requests
from PIL import Image

import configure
from Backend.FirebaseServices.authenticationServices import AuthenticationServices
from Backend.SqliteServices.login_sqlite_services import LoginSqliteServices
from Backend.encryptor import encrypt
from Helper_Functions.customErrorBox import CustomBox
from Screens.Refactor.customWidgets import CustomWidgets
from Screens.Refactor.loginFooterGUI import loginFooterGUI
from Screens.Refactor.loginHeaderGUI import loginHeaderGUI
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
        self.__parent = kwargs['parent']
        self.obj = AuthenticationServices()
        # Initializing the error handlers
        self.enrollment_error_label = ctk.CTkLabel(master=self)
        self.password_error_label = ctk.CTkLabel(master=self)
        # Enlarging the scope og the controller variable
        self.__controller = kwargs['controller']
        # Load the show password icon and hide password icon
        self.__show_icon = loadImage(self, "Assets/hide.png", 17)
        self.__hide_icon = loadImage(self, "Assets/show.png", 17)
        # Local Database Object
        self._sql = LoginSqliteServices()
        # Call the login GUI
        self.__loginGUI()

    def __loginGUI(self):
        """
        This is the method which is used to create the login GUI and holds most values of the GUI
        """
        self.frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.frame.grid(row=0, column=0, padx=(configure.screen_width - 300) / 2,
                        pady=(configure.screen_height - 600) / 2)
        # Call the header GUI
        loginHeaderGUI(self.frame)
        # Create the header label
        CustomWidgets.customHeaderLabel(self, 'LOGIN').grid(row=3, column=0, sticky='w')
        # Creating a frame for email and error box label
        self.enrollment_frame = ctk.CTkFrame(master=self.frame, fg_color=configure.very_dark_gray)
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
        self.password_frame = ctk.CTkFrame(master=self.frame, fg_color=configure.very_dark_gray)
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
            button.configure(image=self.__show_icon, command=lambda: _hide_password())

        # This is the hide password button and this adds the functionality to the hide password button
        def _hide_password():
            """
            This is the function which is used to hide the password when the hide password button is clicked
            :return: None
            """
            self.password_entry.configure(show='•')
            # Change the image of the button to show password icon
            button.configure(image=self.__hide_icon, command=lambda: _show_password())

        # This is the verifyLogin function which is used to verify the login credentials and make sure that they
        # are valid and legit
        def _verifyLogin():
            # if email is valid and password is valid then login
            if validate_password(parent=self.frame) and validate_enrollment(parent=self.frame):
                try:
                    requests.get('https://google.com')
                    if self.enrollment_entry.get().startswith('314'):
                        dbpassword = self.obj.getLoginDetails(self.enrollment_entry.get(), True)
                    else:
                        dbpassword = self.obj.getLoginDetails(self.enrollment_entry.get(), False)
                    if dbpassword is None:
                        # Custom messagebox object
                        self.error = CustomBox()
                        self.error.errorBox('ERROR', 'No user found with this enrollment number')
                        file = open('KONGKNITEC', 'a')
                        file.write('No user found with this enrollment number')
                        file.close()
                    elif dbpassword == encrypt(self.password_entry.get()):
                        self.obj.dbLogin(int(self.enrollment_entry.get()))
                        self._sql.insertLoginDetails(self.enrollment_entry.get())
                        self.__parent.grid_configure(pady=0, padx=0)
                        self.__controller.showFrame('MainScreen', self)
                    else:
                        # Custom messagebox object
                        self.error = CustomBox()
                        self.error.errorBox('ERROR', 'Invalid credentials')
                        file = open('KONGKNITEC', 'a')
                        file.write('No user found with this enrollment number')
                        file.close()
                except requests.exceptions.ConnectionError:
                    self.__controller.showFrame('NoInternet', self)
            else:
                # if email is not valid then show the error message
                if not validate_password(parent=self):
                    # Invoke the error message
                    validate_password(parent=self)
                # if password is not valid then show the error message
                if not validate_enrollment(parent=self):
                    # Invoke the error message
                    validate_enrollment(parent=self.frame)

        # Create the show password button and placing on the same entry box
        button = ctk.CTkButton(master=self.password_frame, image=self.__hide_icon, width=20, height=20, text="",
                               fg_color=configure.dark_gray, corner_radius=180, cursor="hand2", border_width=0,
                               hover=False, command=lambda: _show_password(), bg_color=configure.dark_gray)
        button.grid(row=0, column=1, sticky='e', padx=10)
        # Creating the forgot password hyper label and placing it in the grid layout
        CustomWidgets.customHyperlinkLabel(parent=self.frame, text='FORGOT PASSWORD ?',
                                           command=lambda: self.__controller.showFrame("ForgotPassword", self)). \
            grid(row=6, column=1, sticky='e')
        # Creating the login button and placing it in the grid layout
        CustomWidgets.customButton(parent=self.frame, text='LOGIN', command=lambda: _verifyLogin()).grid(row=7,
                                                                                                         column=0,
                                                                                                         columnspan=2,
                                                                                                         pady=10)
        # Creating the signup hyper label and placing it in the grid layout
        loginFooterGUI(self.frame, "Don't have an account? ", self.__controller, "Sign-up", "Signup")
