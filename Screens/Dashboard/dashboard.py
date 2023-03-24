# Date    : 15/02/23 6:56 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import datetime

import customtkinter as ctk
import configure
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Backend.SqliteServices.attendance_sqlite_services import AttendanceSqliteServices
from Backend.SqliteServices.signup_sqlite_services import SignupSqliteServices


class Dashboard(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.__parent = kwargs['parent']
        self.__controller = kwargs['controller']
        self.signupsql = SignupSqliteServices()
        self.attendanceSql = AttendanceSqliteServices()
        self.__dashboardGUI()

    def __pieGraph(self, master, data):
        with plt.rc_context({'figure.facecolor': '#1a1a1a', 'text.color': '#ffffff'}):
            fig = Figure(figsize=(4, 4), dpi=100)
            plot1 = fig.add_subplot(111)
            plot1.set_facecolor('#1a1a1a')
            plot1.pie(x=data, labels=['Automatic', 'Mannual'], colors=['#1de9b6', '#eeeeee'], shadow=True,
                      explode=[0.1, 0])
            canvas = FigureCanvasTkAgg(fig,
                                       master=master)
            canvas._tkcanvas.config(bg='#1a1a1a')
            canvas.draw()
            canvas.get_tk_widget().pack()

    def __lineGraph(self, master, present, absent, dates):
        with plt.rc_context({'axes.edgecolor': '#1de9b6', 'xtick.color': '#ffffff', 'ytick.color': '#ffffff',
                             'figure.facecolor': '#1a1a1a'}):
            fig = Figure(figsize=(6, 4), dpi=100)
            plot1 = fig.add_subplot(111)
            plot1.set_facecolor('#1a1a1a')
            plot1.plot(present, color='#1de9b6')
            plot1.plot(absent, color='#eeeeee')
            plot1.set_xticks(list(range(len(dates))))
            plot1.set_xticklabels(dates, rotation=45)
            canvas = FigureCanvasTkAgg(fig,
                                       master=master)
            canvas._tkcanvas.config(bg='#1a1a1a')
            canvas.draw()
            canvas.get_tk_widget().pack()

    def __emptyData(self, master):
        self.__empty = ctk.CTkLabel(master, text='No Data Found', fg_color=configure.very_dark_gray)
        self.__empty.grid(row=0, column=0)

    def __dashboardGUI(self):
        self.__frame = ctk.CTkScrollableFrame(self, fg_color=configure.very_dark_gray,
                                              width=(configure.screen_width / 4) * 3,
                                              height=configure.screen_height-150)
        self.__frame.grid(pady=0, padx=0)

        self.__lineFrame = ctk.CTkScrollableFrame(self.__frame, fg_color=configure.very_dark_gray,
                                                  orientation='horizontal', width=(configure.screen_width-100)/2, height=300)
        self.__lineFrame.grid(row=1, column=0, pady=0, padx=0)
        present = []
        dates = []
        absent = []
        tables = list(self.attendanceSql.getTableDetails())
        if not tables:
            self.__emptyData(self.__lineFrame)
        else:
            for date in tables:
                dates.append(date[0][1:3])
                enrolls = list(self.attendanceSql.getEnrollment(date[0][1:]))
                if not enrolls:
                    self.__emptyData(self.__lineFrame)
                else:
                    totalUsers = list(self.signupsql.fetch('Enrollno'))
                    present.append(len(enrolls))
                    for j in totalUsers:
                        totalUsers[totalUsers.index(j)] = j[0]
                    for i in enrolls:
                        if i[0][1:] in totalUsers:
                            totalUsers.remove(i[0][1:])
                    absent.append(len(totalUsers))

        self.__lineGraph(master=self.__lineFrame, present=present, absent=absent, dates=dates)
        self.__pieFrame = ctk.CTkScrollableFrame(self.__frame, fg_color=configure.very_dark_gray,
                                                 orientation='horizontal', width=(configure.screen_width+100)/4, height=300)
        self.__pieFrame.grid(row=1, column=1, pady=0, padx=0)
        enrolls = list(self.attendanceSql.getEnrollment(datetime.datetime.now().strftime('%d%m%Y')))
        if not enrolls:
            self.__emptyData(self.__pieFrame)
        else:
            mode = [0, 0]
            for i in enrolls:
                if i[0].startswith('A'):
                    mode[0] += 1
                else:
                    mode[1] += 1
            self.__pieGraph(master=self.__pieFrame, data=mode)
