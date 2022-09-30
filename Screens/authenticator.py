# Date    : 22/09/22 9:46 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
from tkinter import PhotoImage
import customtkinter as ctk
import configure
from Screens import login, signup, forgot_password, verify, reset_password


class Authenticator(ctk.CTk):
    """
    main frame of the application used to switch between different frames and hold the frames in a stack
    """
    def __init__(self):
        """
        constructor of the class to initialize the main frame and configure main settings like app name and icon
        """
        super().__init__()
        # load the icon of the application
        self._icon = PhotoImage(file="Icons/logo.png")
        # set the title of the application
        self.title('Kongknitec')
        # set the icon of the application
        self.iconphoto(False, self._icon)
        # to disable the maximise button
        self.resizable(False, False)
        # to call the function when the close button is pressed
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        # to set the background color of the application
        self.configure(bg=configure.hover_color)
        # to save the size of the current screen in global variable to use it later
        configure.screen_width = self.winfo_screenwidth()
        configure.screen_height = self.winfo_screenheight()
        # to set the size of the application and so set the invoking location of the window
        self.geometry("{}x{}+{}+{}".format(configure.screen_width, configure.screen_height, 0, 0))
        # to initialise the stacking frame to hold the frames
        container = ctk.CTkFrame(self, fg_color=configure.hover_color)
        # placing the stacking frame on the main frame
        container.grid(row=0, column=0, sticky='nsew', pady=(configure.screen_height - 600) / 2,
                       padx=(configure.screen_width - 300) / 2)
        self.frames = {}
        self.frame_stack = (login.Login, signup.Signup, forgot_password.ForgotPassword, verify.Verify,
                            reset_password.ResetPassword)
        # to add the frames to the stack
        for window in self.frame_stack:
            page_name = window.__name__
            # to take the first frame and place it on the main frame
            frame = window(parent=container, controller=self)
            # to add the frame to the stack
            self.frames[page_name] = frame
            # to place the frame on the main frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame("Login")

    def show_frame(self, page_name):
        """
        Show a frame for the given page name
        """
        frame = self.frames[page_name]
        frame.tkraise()

    def on_closing(self):
        self.destroy()
