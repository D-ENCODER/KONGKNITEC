# Date    : 24/09/22 10:01 am
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import configure
from Helper_Functions.load_image import load_image


def header_gui(self):
    """
    This function is used to create the header of the application
    :param self: The object of the class
    :return: None
    """
    # Loading the image in the frame
    self._img = load_image(self, 'Icons/logo.png', 120)
    # Creating a label for placing the image that is loaded above
    ctk.CTkLabel(master=self, image=self._img, anchor='center').grid(row=0, column=0,
                                                                     columnspan=2)
    # Creating a label for the title of the application
    ctk.CTkLabel(master=self, text='Welcome To', anchor='e',
                 text_font=(configure.font, 10, "bold"), text_color=configure.non_dominant_color).grid(row=1,
                                                                                                       column=0)
    # Creating a label for the title of the application in different colour
    ctk.CTkLabel(master=self, text='KONGKNITEC', anchor='w',
                 text_font=(configure.font, 10, "bold"), text_color=configure.dominant_color).grid(row=1, column=1)
    # Creating a label for the subtitle of the application
    ctk.CTkLabel(master=self, text='', anchor='center').grid(row=2, column=0, columnspan=2)
