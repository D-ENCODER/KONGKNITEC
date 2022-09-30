# Date    : 28/09/22 10:47 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import customtkinter as ctk
import configure
from Helper_Functions.otp_sender import sendOtp
from Screens.Refactor.custom_widgets import CustomWidgets
from Screens.Refactor.header_gui import header_gui
from Screens.forgot_password import ForgotPassword


class Verify(ForgotPassword):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.hover_color)
        self._controller = kwargs['controller']
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
        header_gui(self)
        CustomWidgets.customHeaderLabel(self, 'VERIFY').grid(row=3, column=0)
        self.otp_frame = ctk.CTkFrame(master=self, fg_color=configure.hover_color)
        self.otp_entry1 = CustomWidgets.customEntry(parent=self.otp_frame, placeholder='', width=20, height=45,
                                                    font_weight='bold', font_size=15,
                                                    border_color=configure.dominant_color)
        self.otp_entry1.grid(row=0, column=0, padx=10)
        self.otp_entry2 = CustomWidgets.customEntry(parent=self.otp_frame, placeholder='', width=20, height=45,
                                                    font_weight='bold', font_size=15,
                                                    border_color=configure.dominant_color)
        self.otp_entry2.grid(row=0, column=1)
        self.otp_entry3 = CustomWidgets.customEntry(parent=self.otp_frame, placeholder='', width=20, height=45,
                                                    font_weight='bold', font_size=15,
                                                    border_color=configure.dominant_color)
        self.otp_entry3.grid(row=0, column=2, padx=10)
        self.otp_entry4 = CustomWidgets.customEntry(parent=self.otp_frame, placeholder='', width=20, height=45,
                                                    font_weight='bold', font_size=15,
                                                    border_color=configure.dominant_color)
        self.otp_entry4.grid(row=0, column=3)
        self.otp_entry5 = CustomWidgets.customEntry(parent=self.otp_frame, placeholder='', width=20, height=45,
                                                    font_weight='bold', font_size=15,
                                                    border_color=configure.dominant_color)
        self.otp_entry5.grid(row=0, column=4, padx=10)
        self.otp_entry6 = CustomWidgets.customEntry(parent=self.otp_frame, placeholder='', width=20, height=45,
                                                    font_weight='bold', font_size=15,
                                                    border_color=configure.dominant_color)
        self.otp_entry6.grid(row=0, column=5)

        def verify(event=None):
            self.otp = self.otp_entry1.get() + self.otp_entry2.get() + self.otp_entry3.get() + self.otp_entry4.get() + \
                       self.otp_entry5.get() + self.otp_entry6.get()
            if ForgotPassword.otp == self.otp:
                self._controller.show_frame('ResetPassword')
            else:
                print('failed 400')

        self._switcher(0)
        self.otp_entry1.bind('<KeyRelease>', lambda event: self._switcher(1, event))
        self.otp_entry2.bind('<KeyRelease>', lambda event: self._switcher(2, event))
        self.otp_entry3.bind('<KeyRelease>', lambda event: self._switcher(3, event))
        self.otp_entry4.bind('<KeyRelease>', lambda event: self._switcher(4, event))
        self.otp_entry5.bind('<KeyRelease>', lambda event: self._switcher(5, event))
        self.otp_entry6.bind('<KeyRelease>', lambda event: self._switcher(6, event))
        self.otp_entry6.bind('<Return>', verify)
        self.otp_frame.grid(row=4, column=0, columnspan=2, pady=10)
        self.otp_frame = ctk.CTkFrame(master=self, fg_color=configure.hover_color)

        def countdown(time_sec):
            minutes, seconds = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(minutes, seconds)
            self.timer.configure(text=str(timeformat))

            def sender():
                resend.destroy()
                ForgotPassword.otp = sendOtp(ForgotPassword.email)
                countdown(90)

            if time_sec > 0:
                self.timer_frame.after(1000, countdown, time_sec - 1)
            else:
                resend = CustomWidgets.customHyperlinkLabel(self=self.timer_frame, text='Resend OTP',
                                                            color=configure.dominant_color,
                                                            command=lambda: sender())
                resend.grid(row=0, column=1)

        self.timer_frame = ctk.CTkFrame(self, fg_color=configure.hover_color)
        CustomWidgets.customErrorLabel(self=self.timer_frame, error_text='Resend OTP in ', anchor='e',
                                       color=configure.non_dominant_color).grid(row=0, column=0)
        self.timer = CustomWidgets.customErrorLabel(self=self.timer_frame, error_text='01:30')
        self.timer.grid(row=0, column=1)
        self.timer_frame.grid(row=6, column=0, columnspan=2)
        countdown(90)
        CustomWidgets.customButton(self, 'VERIFY', verify).grid(row=7, column=0, columnspan=2, pady=10)
