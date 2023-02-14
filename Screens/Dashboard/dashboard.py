# Date    : 25/11/22 11:43 am
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import customtkinter as ctk
import configure
from Backend.sqlite_services import SqliteServices
from Helper_Functions.load_image import load_image
from Screens.Refactor.dashboardHeaderGUI import dashboardHeaderGUI


class Dashboard(ctk.CTkFrame):

    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self._parent = kwargs['parent']
        self._parent.grid_configure(pady=0, padx=0)
        self._controller = kwargs['controller']
        self.sql = SqliteServices()
        self._dashboardGUI()

    def _dashboardGUI(self):
        dashboardHeaderGUI(self, self._controller)
        navigator = ctk.CTkFrame(master=self, width=configure.screen_width / 4, fg_color=configure.very_dark_gray,
                                 height=configure.screen_height - 100)
        navigator.dashboardImg = load_image(navigator, 'Assets/dashboard.png', 20)
        navigator.datasetImg = load_image(navigator, 'Assets/dataset.png', 20)
        navigator.attendanceImg = load_image(navigator, 'Assets/attendance.png', 20)
        navigator.profileImg = load_image(navigator, 'Assets/profile.png', 20)
        ctk.CTkLabel(master=navigator, text='', height=30).grid(row=0, column=0)
        ctk.CTkButton(master=navigator, text='Dashboard', image=navigator.dashboardImg, hover=False,
                      fg_color=configure.very_dark_gray, width=configure.screen_width / 4, height=50,
                      text_font=(configure.font, 17, 'bold'), text_color=configure.white).grid(row=1, column=0, pady=20)
        ctk.CTkButton(master=navigator, text='Dataset', image=navigator.datasetImg, hover=False,
                      fg_color=configure.very_dark_gray, width=configure.screen_width / 4, height=50,
                      text_font=(configure.font, 17, 'bold'), text_color=configure.white).grid(row=2, column=0)
        ctk.CTkButton(master=navigator, text='Attendance', image=navigator.attendanceImg, hover=False,
                      fg_color=configure.very_dark_gray, width=configure.screen_width / 4, height=50,
                      text_font=(configure.font, 17, 'bold'), text_color=configure.white).grid(row=3, column=0, pady=20)
        ctk.CTkButton(master=navigator, text='Profile', image=navigator.profileImg, hover=False,
                      fg_color=configure.very_dark_gray, width=configure.screen_width / 4, height=50,
                      text_font=(configure.font, 17, 'bold'), text_color=configure.white).grid(row=4, column=0)
        navigator.grid(row=1, column=0, sticky='n')
        dashboardStack = ctk.CTkFrame(master=self, width=(configure.screen_width / 4) * 3)
        ctk.CTkLabel(master=dashboardStack, height=configure.screen_height-100,width=(configure.screen_width/4)*3, text='').grid(row=0, column=0)
        dashboardStack.grid(row=1, column=1, sticky='n')
