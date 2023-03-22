# Date    : 15/02/23 6:52 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
from datetime import datetime
import customtkinter as ctk
from PIL.ImageTk import PhotoImage
import configure
from Backend.SqliteServices.attendance_sqlite_services import AttendanceSqliteServices
from Backend.SqliteServices.signup_sqlite_services import SignupSqliteServices
from Screens.Dashboard.FaceModules.facial_recognition import FacialRecognition
from Screens.Refactor.customWidgets import CustomWidgets


class Attendance(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.__parent = kwargs['parent']
        self.__controller = kwargs['controller']
        self.date = datetime.now().strftime("%d%m%Y")
        self.__signupSql = SignupSqliteServices()
        self.attendanceSql = AttendanceSqliteServices()
        self.attendanceSql.createTable(self.date)
        self.__attendanceGUI()

    def __attendanceGUI(self):
        ctk.CTkLabel(master=self, text='', height=15).grid(row=0, column=0)
        self.__option = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.__size = (configure.screen_width - (configure.screen_width / 4) - 250)

        def take():
            obj = FacialRecognition()

        ctk.CTkLabel(master=self.__option, text='', width=self.__size).grid(row=0, column=0)
        self.__takeAttendance = ctk.CTkButton(master=self.__option, text='Take',
                                              text_font=(configure.font, 13, "bold"), command=lambda: take(),
                                              text_color=configure.very_dark_gray, fg_color=configure.vivid_cyan,
                                              hover_color=configure.light_cyan, width=100, height=35, corner_radius=10)
        self.__takeAttendance.grid(row=0, column=1, sticky='e')
        self.__addAttendance = ctk.CTkButton(master=self.__option, text='Add', text_font=(configure.font, 13, "bold"),
                                             text_color=configure.very_dark_gray, command=lambda: self.add(),
                                             fg_color=configure.vivid_cyan,
                                             hover_color=configure.light_cyan, width=100, height=35, corner_radius=10)
        self.__addAttendance.grid(row=0, column=3, padx=25)
        self.__option.grid(row=1, column=0)
        enrolls = list(self.attendanceSql.getEnrollment(self.date))
        if not enrolls:
            self.__emptyAttendanceGUI()
        else:
            self.__tableAttendanceGUI()

    def __tableAttendanceGUI(self):
        ctk.CTkLabel(master=self, text='').grid(row=2, column=0)
        self.frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.frame.grid(row=3, column=0)
        data = list(self.attendanceSql.getAttendance(self.date))
        table_header = ['SR No.', 'Enrollment No.', 'Name', 'E-mail', 'Time']
        for i in range(len(table_header)):
            self.label = ctk.CTkLabel(master=self.frame, text=table_header[i], text_font=(configure.font, 18, "bold"),
                                      text_color=configure.vivid_cyan)
            self.label.grid(row=0, column=i, sticky='nsew')
        for details in range(len(data)):
            for fields in range(len(data[details])):
                self.label = ctk.CTkLabel(master=self.frame, text=data[details][fields], text_font=(configure.font, 15))
                self.label.grid(row=details + 1, column=fields, sticky='nsew', padx=10, pady=10)

    def __emptyAttendanceGUI(self):
        frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        frame.grid(row=2, column=0, sticky='nsew', padx=(((configure.screen_width / 4) * 3) - 140) / 2,
                   pady=(configure.screen_height - 191) / 2)
        label = ctk.CTkLabel(frame, text='No Data available!!', text_font=configure.welcome_fontstyle,
                             fg_color=configure.very_dark_gray)
        label.grid(row=1, column=1)

    def add(self):
        window = ctk.CTkToplevel()
        window.geometry("400x200+{}+{}".format((configure.screen_width / 2) - 200, (configure.screen_height / 2) - 150))
        window.title('Add Attendance')
        window.configure(bg=configure.very_dark_gray)
        icon = PhotoImage(file="Assets/logo.png")
        window.iconphoto(False, icon)
        window.focus()
        frame = ctk.CTkFrame(master=window, fg_color=configure.very_dark_gray)
        frame.grid(row=0, column=0)
        entry = CustomWidgets.customEntry(parent=frame, placeholder='Enrollment No')
        entry.grid(row=0, column=0, pady=50, padx=55)

        def addDataset(enrollment):
            if not enrollment:
                CustomWidgets.customErrorLabel(parent=frame,
                                               error_text='Empty Enrollment No', ).grid(row=1, column=0)
            elif not enrollment.isdigit():
                CustomWidgets.customErrorLabel(parent=frame,
                                               error_text='Enrollment No must be numeric', ).grid(row=1, column=0)
            elif len(enrollment) != 12:
                CustomWidgets.customErrorLabel(parent=frame,
                                               error_text='Enrollment No must be of 12 digits', ).grid(row=1, column=0)
            else:
                enrolls = list(self.__signupSql.fetch('Enrollno'))
                for i in enrolls:
                    enrolls[enrolls.index(i)] = i[0]
                if enrollment not in enrolls:
                    CustomWidgets.customErrorLabel(parent=frame,
                                                   error_text='Enrollment No does not exist', ).grid(row=1, column=0)
                else:
                    data = self.attendanceSql.getEnrollment(self.date)
                    for i in data:
                        if i[0] == enrollment:
                            data[data.index(i)] = i[0]
                    if enrollment in data:
                        CustomWidgets.customErrorLabel(parent=frame,
                                                       error_text='Attendance already added', ).grid(row=1, column=0)
                    else:
                        self.attendanceSql.insertAttendance(self.date, 'M' + enrollment)
                        window.destroy()

        button = CustomWidgets.customButton(parent=frame, text='Add', command=lambda: addDataset(entry.get()))
        button.grid(row=2, column=0)
