# Date    : 12/08/22 6:36 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import math
import random
import smtplib


def sendOtp(emailid):
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    message = OTP + " use this otp to login"
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("facioaide2022@gmail.com", "zajtyiewzpnokcrd")
    s.sendmail("facioaide2022@gmail.com", emailid, message)
    return OTP
