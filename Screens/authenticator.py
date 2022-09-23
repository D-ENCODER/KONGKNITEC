# Date    : 22/09/22 9:46 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
from tkinter import PhotoImage
import customtkinter as ctk
import configure
from Screens import login, signup


class Authenticator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._icon = PhotoImage(file="Icons/logo.png")
        self.title('Kongknitec')
        self.iconphoto(False, self._icon)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.configure(bg=configure.hover_color)
        configure.screen_width = self.winfo_screenwidth()
        configure.screen_height = self.winfo_screenheight()
        self.geometry("{}x{}+{}+{}".format(configure.screen_width, configure.screen_height, 0, 0))
        container = ctk.CTkFrame(self, fg_color=configure.hover_color)
        container.grid(row=0, column=0, sticky='nsew', pady=(configure.screen_height - 600) / 2,
                       padx=(configure.screen_width - 300) / 2)
        self.frames = {}
        for window in (login.Login, signup.Signup):
            page_name = window.__name__
            frame = window(parent=container, controller=self)
            self.frames[page_name] = frame
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
