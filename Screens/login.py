# Date    : 12/08/22 6:54 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
from PIL import Image, ImageTk
from Helper_Functions import auth
import configure


class Login(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color=configure.hover_color)
        self._controller = controller
        self._login_frame = ctk.CTkFrame(master=self, fg_color=configure.hyperlink_color, corner_radius=180)
        self._img = Login._load_image(self, 'Icons/logo.png', 120)
        self._show_icon = Login._load_image(self, "Icons/hide.png", 17)
        self._hide_icon = Login._load_image(self, "Icons/show.png", 17)
        self._google_icon = Login._load_image(self._login_frame, "Icons/google.png", 27)
        self._git_icon = Login._load_image(self._login_frame, "Icons/git.png", 27)
        self._twitter_icon = Login._load_image(self._login_frame, "Icons/twitter.png", 27)
        self._loginGUI()

    @staticmethod
    def _load_image(frame, path, image_size):
        return ImageTk.PhotoImage(master=frame, image=Image.open(path).resize((image_size, image_size)))

    def _loginGUI(self):
        ctk.CTkLabel(master=self, image=self._img, anchor='center').grid(row=0, column=0,
                                                                         columnspan=2)
        ctk.CTkLabel(master=self, text='Welcome to ', anchor='e',
                     text_font=(configure.font, 10, "bold"), text_color=configure.non_dominant_color).grid(row=1,
                                                                                                           column=0)
        ctk.CTkLabel(master=self, text='KONGKNITEC', anchor='w',
                     text_font=(configure.font, 10, "bold"), text_color=configure.dominant_color).grid(row=1, column=1)
        ctk.CTkLabel(master=self, text='', anchor='center').grid(row=2, column=0, columnspan=2)
        ctk.CTkLabel(master=self, text='LOGIN', text_font=(configure.font, 18, "bold"),
                     anchor='w', text_color=configure.dominant_color).grid(row=3, column=0)
        email_entry = ctk.CTkEntry(master=self, placeholder_text='Enter your email',
                                   fg_color=configure.hyperlink_color,
                                   border_width=0, corner_radius=10, text_font=(configure.font, 10), width=290,
                                   height=35)
        email_entry.grid(row=4, column=0, columnspan=2, pady=10)
        password_entry = ctk.CTkEntry(master=self, placeholder_text='Password',
                                      fg_color=configure.hyperlink_color,
                                      height=35, border_width=0, text_font=(configure.font, 10), corner_radius=10,
                                      width=290,
                                      show='•')
        password_entry.grid(row=5, column=0, columnspan=2, pady=10)

        def show_password():
            password_entry.configure(show='')
            button.configure(image=self._show_icon, command=lambda: hide_password())

        def hide_password():
            password_entry.configure(show='•')
            button.configure(image=self._hide_icon, command=lambda: show_password())

        def pressed(string):
            print(string)

        ctk.CTkButton(master=self, text='FORGOT PASSWORD ?', cursor="hand2",
                      fg_color=configure.hover_color, text_font=(configure.font, 8, "bold"),
                      hover_color=configure.hover_color, command=lambda: pressed('hello'),
                      text_color=configure.dominant_color).grid(row=6, column=1, sticky='e')

        button = ctk.CTkButton(master=self, image=self._hide_icon, width=20, height=20, text="",
                               fg_color=configure.hyperlink_color, corner_radius=180, cursor="hand2", border=False,
                               hover=False, command=lambda: show_password())
        button.grid(row=5, column=1, sticky='e', padx=10)
        ctk.CTkButton(master=self, text='LOGIN', width=100, height=35, fg_color=configure.dominant_color,
                      text_font=(configure.font, 10, "bold"), hover=False, corner_radius=15,
                      text_color=configure.hover_color,
                      command=lambda: pressed("Welcome to Kongknitec \nYou're successfully Log in.")).grid(row=7,
                                                                                                           column=0,
                                                                                                           columnspan=2,
                                                                                                           pady=10)
        ctk.CTkLabel(master=self, text="Don't have an account? ",
                     text_font=(configure.font, 9), text_color=configure.non_dominant_color).grid(row=8, column=0,
                                                                                                  sticky='e')
        ctk.CTkButton(master=self, text='Sign-up', width=70, height=35, text_font=(configure.font, 10,
                                                                                   "bold"),
                      cursor="hand2", fg_color=configure.hover_color, hover=False,
                      command=lambda: self._controller.show_frame('Signup'),
                      text_color=configure.dominant_color).grid(row=8, column=1, sticky='w')
        ctk.CTkLabel(master=self, text='--OR--',
                     text_font=(configure.font, 9, "bold"), text_color=configure.dominant_color).grid(row=9, column=0,
                                                                                                      columnspan=2)

        def caller():
            authobj = auth.FirebaseFunc
            authobj.fireAuth()

        ctk.CTkButton(master=self._login_frame, image=self._google_icon, text="", width=30, hover=False, cursor='hand2',
                      fg_color=configure.hyperlink_color, command=caller, ).grid(row=0, column=0, padx=7, pady=10)

        ctk.CTkButton(master=self._login_frame, image=self._git_icon, text="", width=30, hover=False, cursor='hand2',
                      fg_color=configure.hyperlink_color, command=caller).grid(row=0, column=1, padx=50, pady=10)

        ctk.CTkButton(master=self._login_frame, image=self._twitter_icon, text="", width=30, hover=False, cursor='hand2'
                      , fg_color=configure.hyperlink_color, command=caller).grid(row=0, column=2, padx=7, pady=10)
        self._login_frame.grid(row=10, column=0, columnspan=2)
