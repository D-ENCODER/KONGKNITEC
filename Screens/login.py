# Date    : 12/08/22 6:54 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import webbrowser

import customtkinter as ctk
from PIL import Image, ImageTk
from Helper_Functions import otp_sender, custom_error_box
from Facial_Recognition import generate_dataset, recognize, train_model


class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x400+850+280")
        self.title('Kongknitec')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.configure(bg='#eeeeee')
        image = Image.open('Icons/logo.png')
        resized_img = image.resize((85, 85), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(master=self, image=resized_img)
        logo = ctk.CTkLabel(master=self, image=self.img, anchor='center')
        # logo.grid(row=0, column=1, columnspan=4,  padx=10)
        logo.place(relx=0, x=150, y=40, anchor='n')
        login_label = ctk.CTkLabel(master=self, text='SIGN IN', text_font=("Times New Roman", 11, "bold"),
                                   text_color='black')
        login_label.place(x=150, relx=0, y=126, anchor='n')
        login_sublabel = ctk.CTkLabel(master=self, text='USE YOUR KONGKNITEC ACCOUNT',
                                      text_font=("Times New Roman", 9, "bold"), text_color='black', )
        login_sublabel.place(x=150, relx=0, y=145, anchor='n')
        email_frame = ctk.CTkFrame(master=self, fg_color='#eeeeee')
        email_label = ctk.CTkLabel(master=email_frame, text='E-MAIL',
                                   text_font=("Times New Roman", 9, "bold"), text_color='black', width=75)
        email_label.pack(side='left')
        email_entry = ctk.CTkEntry(master=email_frame, placeholder_text='Enter email here', fg_color='#eeeeee',
                                   border_width=1,
                                   text_font=("Times New Roman", 12), text_color='black', width=210, height=30)
        email_entry.pack(side='left')
        email_frame.place(x=140, relx=0, y=175, anchor='n')
        password_frame = ctk.CTkFrame(master=self, fg_color='#eeeeee')
        password_label = ctk.CTkLabel(master=password_frame, text='Password',
                                      text_font=("Times New Roman", 9, "bold"), text_color='black', width=75)
        password_label.pack(side='left', pady=15)
        password_entry = ctk.CTkEntry(master=password_frame, placeholder_text='Enter password here', fg_color='#eeeeee',
                                      border_width=1,
                                      text_font=("Times New Roman", 12), text_color='black', width=210, height=30)
        password_entry.pack(side='left')
        password_frame.place(x=140, relx=0, y=210, anchor='n')

        def pressed(string):
            print(string)

        forgot_password = ctk.CTkButton(master=self, text='FORGOT PASSWORD ?', text_font=("Times New Roman", 9, "bold"),
                                        text_color='#60b6f0', cursor="hand2", fg_color='#eeeeee', hover_color='#eeeeee',
                                        command=lambda: pressed('hello'))
        forgot_password.place(x=76, relx=0, y=260, anchor='n')
        some_text = ctk.CTkLabel(master=self, text='SOME TEXT LIKE LEARN MORE AND ETC.',
                                 text_font=("Times New Roman", 8, "bold"), text_color='black', )
        some_text.place(x=122, relx=0, y=290, anchor='n')
        button_frame = ctk.CTkFrame(master=self, fg_color='#eeeeee')
        create_button = ctk.CTkButton(master=button_frame, text='CREATE\nACCOUNT', text_color='black', fg_color='white',
                                      width=50, hover_color='white', text_font=("Times New Roman", 10, "bold"))
        create_button.pack(side='left', padx=45)
        login_button = ctk.CTkButton(master=button_frame, text='LOGIN', text_color='white', fg_color='black', width=70,
                                     hover_color='black', height=35, text_font=("Times New Roman", 10, "bold"))
        login_button.pack(side='left', padx=45)
        button_frame.place(x=140, relx=0, y=340, anchor='n')

    def on_closing(self):
        self.destroy()
