# Date    : 25/11/22 11:43 am
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import customtkinter as ctk
import configure
from Helper_Functions.load_image import load_image


class Dashboard(ctk.CTkFrame):

    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self._parent = kwargs['parent']
        # Initializing the error handlers
        self.enrollment_error_label = ctk.CTkLabel()
        self.password_error_label = ctk.CTkLabel()
        # Enlarging the scope og the controller variable
        self._controller = kwargs['controller']
        # Load the show password icon and hide password icon
        self._show_icon = load_image(self, "Icons/hide.png", 17)
        self._hide_icon = load_image(self, "Icons/show.png", 17)
        # Call the login GUI
        self._dashboardGUI()

    def _dashboardGUI(self):
        pass
