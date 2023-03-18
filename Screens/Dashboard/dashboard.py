# Date    : 15/02/23 6:56 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import configure
from Backend.signup_sqlite_services import SignupSqliteServices


class Dashboard(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.__parent = kwargs['parent']
        self.__controller = kwargs['controller']
        self.sql = SignupSqliteServices()
        self.__dashboardGUI()

    def __dashboardGUI(self):
        pass
