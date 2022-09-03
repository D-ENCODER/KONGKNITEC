# Date    : 12/08/22 6:54 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
from PIL import Image, ImageTk
from Helper_Functions import otp_sender, custom_error_box
from Facial_Recognition import generate_dataset, recognize, train_model
from configure import *


class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Kongknitec')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.configure(bg=hover_color)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry("{}x{}+{}+{}".format(screen_width, screen_height, 0, 0))
        mainframe = ctk.CTkFrame(master=self, fg_color=hover_color)
        image = Image.open('Icons/logo.png')
        resized_img = image.resize((120, 120), Image.ANTIALIAS)
        mainframe.img = ImageTk.PhotoImage(master=mainframe, image=resized_img)
        ctk.CTkLabel(master=mainframe, image=mainframe.img, anchor='center').grid(row=0, column=0, columnspan=2)
        ctk.CTkLabel(master=mainframe, text='Welcome to', anchor='e',
                     text_font=(font, 10, "bold"), text_color=non_dominant_color).grid(row=1, column=0)
        ctk.CTkLabel(master=mainframe, text='KONGKNITEC', anchor='w',
                     text_font=(font, 10, "bold"), text_color=dominant_color).grid(row=1, column=1)
        ctk.CTkLabel(master=mainframe, text='', anchor='center').grid(row=2, column=0, columnspan=2)
        ctk.CTkLabel(master=mainframe, text='LOGIN', text_font=(font, 14, "bold"),
                     anchor='w', text_color=dominant_color).grid(row=3, column=0)
        email_entry = ctk.CTkEntry(master=mainframe, placeholder_text='Enter your email', fg_color=hyperlink_color,
                                   border_width=0, corner_radius=10, text_font=(font, 10), width=250, height=35)
        email_entry.grid(row=4, column=0, columnspan=2, pady=10)
        password_entry = ctk.CTkEntry(master=mainframe, placeholder_text='Password', fg_color=hyperlink_color,
                                      height=35, border_width=0, text_font=(font, 10), corner_radius=10, width=250)
        password_entry.grid(row=5, column=0, columnspan=2, pady=10)

        def pressed(string):
            print(string)

        forgot_password = ctk.CTkButton(master=mainframe, text='FORGOT PASSWORD ?', cursor="hand2",
                                        fg_color=hover_color, text_font=(font, 7, "bold"),
                                        hover_color=hover_color, command=lambda: pressed('hello'),
                                        text_color=dominant_color)
        forgot_password.grid(row=6, column=1, sticky='e')
        login_button = ctk.CTkButton(master=mainframe, text='LOGIN', width=100, height=35, fg_color=dominant_color,
                                     text_font=(font, 10, "bold"), hover_color=dominant_color, corner_radius=15,
                                     text_color=hover_color, command=lambda: pressed("Welcome to Kongknitech \nYou're successfully Log in."))
        login_button.grid(row=7, column=0, columnspan=2, pady=10)
        ctk.CTkLabel(master=mainframe, text='Dont have an account?',
                     text_font=(font, 9), text_color=non_dominant_color).grid(row=8, column=0, sticky='e')
        create_button = ctk.CTkButton(master=mainframe, text='Sign-up', width=70, height=35,
                                      cursor="hand2", fg_color=hover_color, hover_color=hover_color,
                                      text_color=dominant_color, text_font=(font, 10, "bold"))
        create_button.grid(row=8, column=1, sticky='w')
        ctk.CTkLabel(master=mainframe, text='--OR--',
                     text_font=(font, 9, "bold"), text_color=dominant_color).grid(row=9, column=0, columnspan=2)
        # TODO: here comes the third party login button.
        mainframe.grid(row=0, column=0, pady=(screen_height - 500) / 2, padx=(screen_width - 300) / 2)

    def on_closing(self):
        self.destroy()
