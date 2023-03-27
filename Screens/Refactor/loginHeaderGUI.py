# Date    : 24/09/22 10:01 am
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
from PIL import Image
import configure


def loginHeaderGUI(self):
    """
    This function is used to create the header of the application
    :param self: The object of the class
    :return: None
    """
    # Loading the image in the frame
    self._img = ctk.CTkImage(Image.open('Assets/logo.png'), size=(120, 120))
    # Creating a label for placing the image that is loaded above
    ctk.CTkLabel(master=self, image=self._img, anchor='center', text="").grid(row=0, column=0,
                                                                              columnspan=2)
    # Creating a label for the title of the application
    frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
    frame.grid(row=1, column=0, columnspan=2)
    ctk.CTkLabel(master=frame, text='Welcome To ', anchor='e',
                 font=configure.welcome_fontstyle, text_color=configure.white).grid(row=1,
                                                                                    column=0)
    # Creating a label for the title of the application in different colour
    ctk.CTkLabel(master=frame, text='KONGKNITEC', anchor='w',
                 font=configure.welcome_fontstyle, text_color=configure.light_cyan).grid(row=1, column=1)
    # Creating a label for the subtitle of the application
    ctk.CTkLabel(master=self, text='', anchor='center').grid(row=2, column=0, columnspan=2)
