# Date    : 15/02/23 6:52 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
from datetime import datetime
import customtkinter as ctk
from PIL import Image
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
        self.__JAVAframe = ctk.CTkScrollableFrame(master=self, fg_color=configure.very_dark_gray,
                                              width=(configure.screen_width / 4) * 3,
                                              height=(configure.screen_height - 200))
        self.__DBMSframe = ctk.CTkScrollableFrame(master=self, fg_color=configure.very_dark_gray,
                                                  width=(configure.screen_width / 4) * 3,
                                                  height=(configure.screen_height - 200))
        self.__emptyFrame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.__emptyFrame.grid(row=2, column=0, sticky='nsew', padx=(((configure.screen_width / 4) * 3) - 140) / 2,
                               pady=(configure.screen_height - 191) / 2)
        self.attendanceSql = AttendanceSqliteServices()
        self.attendanceSql.createTable(self.date)
        self.sub = 'DBMS'
        self.__attendanceGUI()

    def __attendanceGUI(self):
        ctk.CTkLabel(master=self, text='', height=15).grid(row=0, column=0)
        self.__option = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.__size = (configure.screen_width - (configure.screen_width / 4) - 500)

        def take(self):
            obj = FacialRecognition(self.sub)

        ctk.CTkLabel(master=self.__option, text='', width=self.__size).grid(row=0, column=0)
        image = ctk.CTkImage(Image.open('Assets/sync.png'), size=(25, 25))
        self.__refreshTable = ctk.CTkButton(master=self.__option, text='', command=lambda: self.refresh(), hover=False,
                                            fg_color=configure.very_dark_gray, image=image, width=35, height=35,
                                            corner_radius=180)
        self.__refreshTable.grid(row=0, column=1, sticky='e')
        self.subjects = ctk.CTkComboBox(master=self.__option, width=100, height=35, corner_radius=10,
                                        values=['DBMS', 'JAVA', 'MCAD', 'NMA', 'PPUD'], fg_color=configure.dark_gray,
                                        command=lambda event: self.subject())
        self.subjects.grid(row=0, column=2, sticky='e', padx=25)
        self.__takeAttendance = ctk.CTkButton(master=self.__option, text='Take',
                                              font=(configure.font, 18, "bold"), command=lambda: take(self),
                                              text_color=configure.very_dark_gray, fg_color=configure.vivid_cyan,
                                              hover_color=configure.light_cyan, width=100, height=35, corner_radius=10)
        self.__takeAttendance.grid(row=0, column=3, sticky='e')
        self.__addAttendance = ctk.CTkButton(master=self.__option, text='Add', font=(configure.font, 18, "bold"),
                                             text_color=configure.very_dark_gray, command=lambda: self.add(),
                                             fg_color=configure.vivid_cyan,
                                             hover_color=configure.light_cyan, width=100, height=35, corner_radius=10)
        self.__addAttendance.grid(row=0, column=4, padx=25)
        self.__option.grid(row=1, column=0)

        enrolls = list(self.attendanceSql.getEnrollment(self.date))
        if not enrolls:
            self.__emptyAttendanceGUI()
        else:
            self.subject()

    def refresh(self):
        enrolls = list(self.attendanceSql.getEnrollment(self.date))
        if not enrolls:
            self.__emptyFrame.destroy()
            self.__emptyAttendanceGUI()
        else:
            self.__frame.destroy()
            self.__tableDBMSAttendanceGUI()

    def subject(self):
        print(self.subjects.get())
        if self.subjects.get() == 'DBMS':
            self.sub = 'DBMS'
            self.__emptyFrame.destroy()
            self.__JAVAframe.destroy()
            self.__tableDBMSAttendanceGUI()
        elif self.subjects.get() == 'JAVA':
            self.sub = 'JAVA'
            self.__emptyFrame.destroy()
            self.__DBMSframe.destroy()
            self.__tableJAVAAttendanceGUI()
        elif self.subjects.get() == 'MCAD':
            self.sub = 'MCAD'
            pass
        elif self.subjects.get() == 'NMA':
            self.sub = 'NMA'
            pass
        elif self.subjects.get() == 'PPUD':
            self.sub = 'PPUD'
            pass

    def __tableDBMSAttendanceGUI(self):
        self.__DBMSframe = ctk.CTkScrollableFrame(master=self, fg_color=configure.very_dark_gray,
                                                  width=(configure.screen_width / 4) * 3,
                                                  height=(configure.screen_height - 200))
        self.__DBMSframe.grid(row=3, column=0)
        self.__DBMSframe.tkraise()
        ctk.CTkLabel(master=self, text='').grid(row=2, column=0)
        data = list(self.attendanceSql.getAttendanceWithSubject(self.date, "DBMS"))
        table_header = ['SR No.', 'Enrollment No.', 'Name', 'E-mail', 'Time']
        for i in range(len(table_header)):
            self.label = ctk.CTkLabel(master=self.__DBMSframe, text=table_header[i], font=(configure.font, 23, "bold"),
                                      text_color=configure.vivid_cyan)
            self.label.grid(row=0, column=i, sticky='nsew', padx=20)

        info = []
        for i in range(len(data)):
            data[i] = list(data[i])
            info.append([])
            for j in range(len(data[i])):
                if j == 0:
                    info[i].append(data[i][0])
                if j == 1:
                    enroll = str(data[i][1])[1:]
                    info[i].append(enroll)
                    userdata = list(self.__signupSql.fetchCondition('Fname, Lname, Email', enroll))
                    for user in userdata:
                        info[i].append(user[0] + ' ' + user[1])
                        info[i].append(user[2])
                if j == 2:
                    info[i].append(data[i][2])
        data = info
        for details in range(len(data)):
            for fields in range(len(data[details])):
                self.label = ctk.CTkLabel(master=self.__DBMSframe, text=data[details][fields],
                                          font=(configure.font, 20))
                self.label.grid(row=details + 1, column=fields, sticky='nsew', padx=20, pady=10)

    def __tableJAVAAttendanceGUI(self):
        self.__JAVAframe = ctk.CTkScrollableFrame(master=self, fg_color=configure.very_dark_gray,
                                              width=(configure.screen_width / 4) * 3,
                                              height=(configure.screen_height - 200))
        self.__JAVAframe.grid(row=3, column=0)
        self.__JAVAframe.tkraise()
        ctk.CTkLabel(master=self, text='').grid(row=2, column=0)
        data = list(self.attendanceSql.getAttendanceWithSubject(self.date, "JAVA"))
        if not data:
            self.__emptyAttendanceGUI()
        table_header = ['SR No.', 'Enrollment No.', 'Name', 'E-mail', 'Time']
        for i in range(len(table_header)):
            self.label = ctk.CTkLabel(master=self.__JAVAframe, text=table_header[i], font=(configure.font, 23, "bold"),
                                      text_color=configure.vivid_cyan)
            self.label.grid(row=0, column=i, sticky='nsew', padx=20)

        info = []
        for i in range(len(data)):
            data[i] = list(data[i])
            info.append([])
            for j in range(len(data[i])):
                if j == 0:
                    info[i].append(data[i][0])
                if j == 1:
                    enroll = str(data[i][1])[1:]
                    info[i].append(enroll)
                    userdata = list(self.__signupSql.fetchCondition('Fname, Lname, Email', enroll))
                    for user in userdata:
                        info[i].append(user[0] + ' ' + user[1])
                        info[i].append(user[2])
                if j == 2:
                    info[i].append(data[i][2])
        data = info
        for details in range(len(data)):
            for fields in range(len(data[details])):
                self.label = ctk.CTkLabel(master=self.__JAVAframe, text=data[details][fields], font=(configure.font, 20))
                self.label.grid(row=details + 1, column=fields, sticky='nsew', padx=20, pady=10)

    def __emptyAttendanceGUI(self):
        self.__emptyFrame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.__emptyFrame.grid(row=2, column=0, sticky='nsew', padx=(((configure.screen_width / 4) * 3) - 140) / 2,
                               pady=(configure.screen_height - 191) / 2)
        self.__emptyFrame.tkraise()
        label = ctk.CTkLabel(self.__emptyFrame, text='No Data available!!', font=configure.welcome_fontstyle,
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
