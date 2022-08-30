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
        self.configure(bg='#1d2951')
        image = Image.open('Icons/logo.png')
        resized_img = image.resize((90, 90), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(master=self, image=resized_img)
        logo = ctk.CTkLabel(master=self, image=self.img, anchor='center')
        # logo.grid(row=0, column=1, columnspan=4,  padx=10)
        logo.place(relx=0, x=150, y=20, anchor='n')
        login_label = ctk.CTkLabel(master=self, text='SIGN IN', text_font=("Microsoft YaHei UI Light", 13, "bold"),
                                   text_color='#dbe9f4')
        login_label.place(x=146, relx=0, y=110, anchor='n')
        login_sublabel = ctk.CTkLabel(master=self, text='USE YOUR KONGKNITEC ACCOUNT',
                                      text_font=("Microsoft YaHei UI Light", 9, "bold"), text_color='#dbe9f4', )
        login_sublabel.place(x=150, relx=0, y=137, anchor='n')
        email_frame = ctk.CTkFrame(master=self, fg_color='#1d2951')
        email_entry = ctk.CTkEntry(master=email_frame, placeholder_text='E-Mail', fg_color='#1d2951',
                                   border_width=0,
                                   text_font=("Microsoft YaHei UI Light", 11, 'bold'), text_color='white', width=210, height=30)
        ctk.CTkFrame(master=self, width=250, height=3, fg_color='white').place(x=15, y=205)
        email_entry.pack(side='left')
        email_frame.place(x=120, relx=0, y=175, anchor='n')
        password_frame = ctk.CTkFrame(master=self, fg_color='#1d2951')
        password_entry = ctk.CTkEntry(master=password_frame, placeholder_text='Password ', fg_color='#1d2951',
                                      border_width=0,
                                      text_font=("Microsoft YaHei UI Light", 11, 'bold'), text_color='#dbe9f4', width=210, height=30)
        ctk.CTkFrame(master=self, width=250, height=3, fg_color='white').place(x=15, y=250)
        password_entry.pack(side='left')
        password_frame.place(x=118, relx=0, y=220, anchor='n')

        def pressed(string):
            print(string)

        forgot_password = ctk.CTkButton(master=self, text='FORGOT PASSWORD ?', text_font=("Microsoft YaHei UI Light", 9, "bold"),
                                        text_color='#60b6f0', cursor="hand2", fg_color='#1d2951', hover_color='#1d2951',
                                        command=lambda: pressed('hello'))
        forgot_password.place(x=76, relx=0, y=270, anchor='n')
        some_text = ctk.CTkLabel(master=self, text='SOME TEXT LIKE LEARN MORE AND ETC.',
                                 text_font=("Microsoft YaHei UI Light", 9, "bold"), text_color='#dbe9f4', )
        some_text.place(x=130, relx=0, y=305, anchor='n')
        button_frame = ctk.CTkFrame(master=self, fg_color='#1d2951')
        create_button = ctk.CTkButton(master=button_frame, text='CREATE ACCOUNT', text_color='#1d2951', fg_color='#dbe9f4',
                                      width=70, height=35, hover_color='white', text_font=("Microsoft YaHei UI Light", 10, "bold"))
        create_button.pack(side='left', padx=45)
        login_button = ctk.CTkButton(master=button_frame, text='LOGIN', text_color='#1d2951', fg_color='#dbe9f4', width=70,
                                     hover_color='white', height=35, text_font=("Microsoft YaHei UI Light", 10, "bold"))
        login_button.pack(side='left', padx=30)
        button_frame.place(x=140, relx=0, y=350, anchor='n')

    def on_closing(self):
        self.destroy()
