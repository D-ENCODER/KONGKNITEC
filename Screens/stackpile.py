# Date    : 22/09/22 9:46 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
from tkinter import PhotoImage
import customtkinter as ctk
import firebase_admin
from firebase_admin import credentials

import configure
from Screens.Auth import login, signup, forgotPassword, verify, resetPassword, personalInfo
from Screens import splashScreen, noInternet
from Screens.Dashboard import mainscreen


class StackPile(ctk.CTk):
    """
    main frame of the application used to switch between different frames and hold the frames in a stack
    """

    def __init__(self):
        """
        constructor of the class to initialize the main frame and configure main settings like app name and icon
        """
        super().__init__()
        # load the icon of the application
        self._icon = PhotoImage(file="Assets/logo.png")
        # set the title of the application
        self.title('Kongknitec')
        # set the icon of the application
        self.iconphoto(True, self._icon)
        # to disable the maximise button
        self.resizable(False, False)
        # To deactivate scaling effect on software
        # ctk.deactivate_automatic_dpi_awareness()
        # to call the function when the close button is pressed
        self.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.cred = credentials.Certificate("Backend/FirebaseServices/serviceAccountKey.json")
        firebase_admin.initialize_app(self.cred)
        # to set the background color of the application
        self.configure(bg=configure.very_dark_gray)
        # to save the size of the current screen in global variable to use it later
        configure.screen_width = self.winfo_screenwidth()
        configure.screen_height = self.winfo_screenheight()
        # to set the size of the application and so set the invoking location of the window
        self.geometry("{}x{}+{}+{}".format(configure.screen_width, configure.screen_height, 0, 0))
        # to initialise the stacking frame to hold the frames
        container = ctk.CTkFrame(self, fg_color=configure.very_dark_gray)
        # placing the stacking frame on the main frame
        container.grid(row=0, column=0, sticky='nsew')
        self.frames = {}
        self.previous = ''
        self.frame_stack = (
            noInternet.NoInternet, login.Login, signup.Signup, forgotPassword.ForgotPassword, verify.Verify,
            resetPassword.ResetPassword, personalInfo.UserDetailsStack, mainscreen.MainScreen,
            splashScreen.SplashScreen
        )
        # to add the frames to the stack
        for window in self.frame_stack:
            page_name = window.__name__
            # to take the first frame and place it on the main frame
            frame = window(parent=container, controller=self)
            # to add the frame to the stack
            self.frames[page_name] = frame
            # to place the frame on the main frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.showFrame("MainScreen", self)

    def showFrame(self, page_name, previous):
        """
        Show a frame for the given page name
        """
        self.previous = previous.__class__.__name__
        frame = self.frames[page_name]
        frame.tkraise()

    def gotoPrevious(self):
        frame = self.frames[self.previous]
        frame.tkraise()

    def getPrevious(self):
        return self.previous

    def onClosing(self):
        self.destroy()
