# Date    : 28/09/22 10:47 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import requests
import configure
from Backend.FirebaseServices.authenticationServices import AuthenticationServices
from Helper_Functions.customErrorBox import CustomBox
from Backend.smtp_services import sendVerifyOtp, sendAdminId, sendWelcome, sendResetOtp
from Screens.Refactor.customWidgets import CustomWidgets
from Screens.Refactor.loginHeaderGUI import loginHeaderGUI
from Screens.Auth.forgotPassword import ForgotPassword
from Screens.Auth.personalInfo import ContactInfo


class Verify(ForgotPassword, ContactInfo):
    credentials = {}

    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self._controller = kwargs['controller']
        self.obj = AuthenticationServices()
        self._verifyGUI()

    def _switcher(self, index, event=None):
        match index:
            case 0:
                self.otp_entry1.focus()
            case 1:
                if event.keysym != 'BackSpace':
                    if event.keysym.isnumeric():
                        if len(self.otp_entry1.get()) > 1:
                            self.otp_entry1.delete(1)
                        self.otp_entry2.focus()
                    else:
                        self.otp_entry1.delete(0)
                        self.otp_entry1.insert(0, '')
            case 2:
                if event.keysym != 'BackSpace':
                    if event.keysym.isnumeric():
                        if len(self.otp_entry2.get()) > 1:
                            self.otp_entry2.delete(1)
                        self.otp_entry3.focus()
                    else:
                        self.otp_entry2.delete(0)
                        self.otp_entry2.insert(0, '')
                else:
                    self.otp_entry2.delete(0)
                    self.otp_entry1.focus()
            case 3:
                if event.keysym != 'BackSpace':
                    if event.keysym.isnumeric():
                        if len(self.otp_entry3.get()) > 1:
                            self.otp_entry3.delete(1)
                        self.otp_entry4.focus()
                    else:
                        self.otp_entry3.delete(0)
                        self.otp_entry3.insert(0, '')
                else:
                    self.otp_entry3.delete(0)
                    self.otp_entry2.focus()
            case 4:
                if event.keysym != 'BackSpace':
                    if event.keysym.isnumeric():
                        if len(self.otp_entry4.get()) > 1:
                            self.otp_entry4.delete(1)
                        self.otp_entry5.focus()
                    else:
                        self.otp_entry4.delete(0)
                        self.otp_entry4.insert(0, '')
                else:
                    self.otp_entry4.delete(0)
                    self.otp_entry3.focus()
            case 5:
                if event.keysym != 'BackSpace':
                    if event.keysym.isnumeric():
                        if len(self.otp_entry5.get()) > 1:
                            self.otp_entry5.delete(1)
                        self.otp_entry6.focus()
                    else:
                        self.otp_entry5.delete(0)
                        self.otp_entry5.insert(0, '')
                else:
                    self.otp_entry5.delete(0)
                    self.otp_entry4.focus()
            case 6:
                if event.keysym != 'BackSpace' and event.keysym != 'Return':
                    if event.keysym.isnumeric():
                        if len(self.otp_entry6.get()) > 1:
                            self.otp_entry6.delete(1)
                    else:
                        self.otp_entry6.delete(0)
                        self.otp_entry6.insert(0, '')
                elif event.keysym == 'BackSpace':
                    self.otp_entry6.delete(0)
                    self.otp_entry5.focus()

    def _verifyGUI(self):
        self.frame = ctk.CTkFrame(master=self, fg_color=configure.very_dark_gray)
        self.frame.grid(row=0, column=0, sticky='nsew', padx=(configure.screen_width - 300) / 2, pady=(configure.screen_height - 600) / 2)
        loginHeaderGUI(self.frame)
        CustomWidgets.customHeaderLabel(self.frame, 'VERIFY').grid(row=3, column=0, sticky='w')
        self.otp_frame = ctk.CTkFrame(master=self.frame, fg_color=configure.very_dark_gray)
        self.otp_entry1 = CustomWidgets.customEntry(parent=self.otp_frame, placeholder='', width=20, height=45,
                                                    font_weight='bold', font_size=17)
        self.otp_entry1.grid(row=0, column=0, padx=10)
        self.otp_entry2 = CustomWidgets.customEntry(parent=self.otp_frame, placeholder='', width=20, height=45,
                                                    font_weight='bold', font_size=17)
        self.otp_entry2.grid(row=0, column=1)
        self.otp_entry3 = CustomWidgets.customEntry(parent=self.otp_frame, placeholder='', width=20, height=45,
                                                    font_weight='bold', font_size=17)
        self.otp_entry3.grid(row=0, column=2, padx=10)
        self.otp_entry4 = CustomWidgets.customEntry(parent=self.otp_frame, placeholder='', width=20, height=45,
                                                    font_weight='bold', font_size=17)
        self.otp_entry4.grid(row=0, column=3)
        self.otp_entry5 = CustomWidgets.customEntry(parent=self.otp_frame, placeholder='', width=20, height=45,
                                                    font_weight='bold', font_size=17)
        self.otp_entry5.grid(row=0, column=4, padx=10)
        self.otp_entry6 = CustomWidgets.customEntry(parent=self.otp_frame, placeholder='', width=20, height=45,
                                                    font_weight='bold', font_size=17)
        self.otp_entry6.grid(row=0, column=5)

        def verify(event=None):
            self.otp = self.otp_entry1.get() + self.otp_entry2.get() + self.otp_entry3.get() + self.otp_entry4.get() + \
                       self.otp_entry5.get() + self.otp_entry6.get()
            if self._controller.getPrevious() == 'ForgotPassword':
                Verify.credentials = ForgotPassword.credentials
                if Verify.credentials['otp'] == self.otp:
                    self._controller.showFrame('ResetPassword', self)
            else:
                Verify.credentials = ContactInfo.credentials
                if Verify.credentials['otp'] == self.otp:
                    try:
                        requests.get('https://google.com')
                        try:
                            Verify.credentials.pop('otp')
                            if len(Verify.credentials['Enrollment']) == 6:
                                Verify.credentials['Enrollment'] = sendAdminId(Verify.credentials['Email'])
                                sendWelcome(Verify.credentials['Email'], Verify.credentials['First Name'] +
                                            ' ' + Verify.credentials['Last Name'], True)
                                self.obj.dbSignUp(Verify.credentials, 'Admin_details')
                            else:
                                Verify.credentials['Enrollment'] = int(Verify.credentials['Enrollment'])
                                sendWelcome(Verify.credentials['Email'], Verify.credentials['First Name'] +
                                            ' ' + Verify.credentials['Last Name'], False)
                                self.obj.dbSignUp(Verify.credentials, 'User_details')
                            self._controller.showFrame('Login', self)
                        except Exception as e:
                            obj = CustomBox()
                            obj.errorBox('Error', 'Something went wrong' + '(' + e.args[0] + ')')
                    except requests.exceptions.ConnectionError as e:
                        self._controller.showFrame('NoInternet', self)
                else:
                    obj = CustomBox()
                    obj.errorBox('Error', 'Invalid OTP')

        self._switcher(0)
        self.otp_entry1.bind('<KeyRelease>', lambda event: self._switcher(1, event))
        self.otp_entry2.bind('<KeyRelease>', lambda event: self._switcher(2, event))
        self.otp_entry3.bind('<KeyRelease>', lambda event: self._switcher(3, event))
        self.otp_entry4.bind('<KeyRelease>', lambda event: self._switcher(4, event))
        self.otp_entry5.bind('<KeyRelease>', lambda event: self._switcher(5, event))
        self.otp_entry6.bind('<KeyRelease>', lambda event: self._switcher(6, event))
        self.otp_entry6.bind('<Return>', verify)
        self.otp_frame.grid(row=4, column=0, columnspan=2, pady=10)
        self.otp_frame = ctk.CTkFrame(master=self.frame, fg_color=configure.very_dark_gray)

        def countdown(time_sec):
            minutes, seconds = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(minutes, seconds)
            self.timer.configure(text=str(timeformat))

            def sender():
                resend.destroy()
                try:
                    requests.get('https://google.com')
                    try:
                        if self._controller.getPrevious() == 'ForgotPassword':
                            ForgotPassword.credentials['otp'] = sendResetOtp(Verify.credentials['Email'])
                        else:
                            ContactInfo.credentials['otp'] = sendVerifyOtp(Verify.credentials['Email'])
                    except Exception as e:
                        obj = CustomBox()
                        obj.errorBox('Error', 'Something went wrong. Please try again later' + e.args[0])
                        self._controller.showFrame('Login', self)
                    countdown(90)
                except requests.exceptions.ConnectionError as e:
                    self._controller.showFrame('NoInternet', self)

            if time_sec > 0:
                self.timer_frame.after(1000, countdown, time_sec - 1)
            else:
                resend = CustomWidgets.customHyperlinkLabel(parent=self.timer_frame, text='Resend OTP',
                                                            color=configure.light_cyan,
                                                            command=lambda: sender())
                resend.grid(row=0, column=1)

        self.timer_frame = ctk.CTkFrame(self.frame, fg_color=configure.very_dark_gray)
        CustomWidgets.customErrorLabel(parent=self.timer_frame, error_text='Resend OTP in ', anchor='e',
                                       color=configure.white).grid(row=0, column=0)
        self.timer = CustomWidgets.customErrorLabel(parent=self.timer_frame, error_text='01:30')
        self.timer.grid(row=0, column=1)
        self.timer_frame.grid(row=6, column=0, columnspan=2)
        countdown(90)
        CustomWidgets.customButton(parent=self.frame, text='VERIFY', command=verify).grid(row=7, column=0, columnspan=2,
                                                                                    pady=10)
