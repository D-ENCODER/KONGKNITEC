# Date    : 11/02/23 7:47 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import configure
from Helper_Functions.load_image import load_image
from Screens.Refactor.custom_widgets import CustomWidgets


def dashboardHeaderGUI(parent, grandparent):
    headerFrame = ctk.CTkFrame(parent, fg_color=configure.very_dark_gray)
    # Loading the image in the frame
    headerFrame.img = load_image(headerFrame, 'Assets/logo.png', 80)
    # Creating a label for placing the image that is loaded above
    image = ctk.CTkLabel(master=headerFrame, image=headerFrame.img, anchor='center', width=100)
    image.grid(row=0, column=0)
    headerText = CustomWidgets.customHeaderLabel(headerFrame, 'KONGKNITEC')
    headerText.configure(text_font=(configure.font, 20, 'bold'))
    headerText.grid(row=0, column=1)
    welcomeText = ctk.CTkLabel(master=headerFrame, text='Welcome ', text_color=configure.white,
                               text_font=configure.welcome_fontstyle, justify='center', width=0)
    welcomeText.grid(row=0, column=3)
    name = list(parent.sql.fetch('Fname, Lname')[0])
    userText = ctk.CTkLabel(master=headerFrame, width=0, text=" ".join([name[0], name[1]]),
                            text_color=configure.light_cyan, text_font=configure.welcome_fontstyle, justify='center')
    userText.grid(row=0, column=4)
    grandparent.withdraw()
    grandparent.update()
    size = (image.winfo_width()
            + welcomeText.winfo_width()
            + headerText.winfo_width()
            + userText.winfo_width()
            + 20)
    grandparent.deiconify()
    ctk.CTkLabel(master=headerFrame, text='',
                 width=configure.screen_width - size).grid(row=0, column=2)
    headerFrame.grid(row=0, column=0, columnspan=2, sticky='nsew')
