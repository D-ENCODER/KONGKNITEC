# Date    : 20/11/22 5:56 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import customtkinter as ctk
import requests
from PIL import Image

import configure
from Helper_Functions.loadImage import loadImage
from Screens.Refactor.customWidgets import CustomWidgets


class NoInternet(ctk.CTkFrame):
    """
    class for the no internet screen.
    """

    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self._parent = kwargs['parent']
        self._parent.grid_configure(pady=(configure.screen_height - 400) / 2,
                                    padx=(configure.screen_width - 400) / 2)
        self._controller = kwargs['controller']
        self._noInternetGUI()

    def _noInternetGUI(self):
        """
        This is the method which is used to create the no internet GUI and holds most values of the GUI
        """
        frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self._img = ctk.CTkImage(Image.open('Assets/no_internet.png'), size=(220, 220))
        # Creating a label for placing the image that is loaded above
        ctk.CTkLabel(master=frame, image=self._img, anchor='center', text="").grid(row=0, column=0,
                                                                                   columnspan=2)
        ctk.CTkLabel(master=frame, text='No Internet Connection', anchor='center', font=configure.header_fontstyle) \
            .grid(row=1, column=0, columnspan=2)
        ctk.CTkLabel(master=frame, text='Please check your internet connection and\nmake sure you are connected to '
                                        'stable\ninternet connection ', anchor='center',
                     font=configure.welcome_fontstyle).grid(row=1, column=0, columnspan=2)
        CustomWidgets.customButton(parent=frame, text='Retry', command=self._retry).grid(row=2, column=0, columnspan=2,
                                                                                         pady=10)
        frame.grid(row=0, column=0, padx=(configure.screen_width-370)/2, pady=(configure.screen_height-320)/2)

    def _retry(self):
        """
        This is the method which is used to retry the connection
        """
        try:
            requests.get('https://google.com')
            self._parent.grid_configure(pady=(configure.screen_height - 600) / 2,
                                        padx=(configure.screen_width - 300) / 2)
            self._controller.gotoPrevious()
        except requests.exceptions.ConnectionError:
            pass
