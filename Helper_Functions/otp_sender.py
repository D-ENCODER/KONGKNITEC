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

    m1 = "Dear Customer,\n\nYou request for change password for your KONGKNITEC account.\nYour One Time Password " \
         "(OTP) is:\n\n"
    m2 = "\n\nNote: This is an auto-generated email; \n So please do not reply to this mail\n\nThank you,\n\n" \
         "KONGKNITEC Team"
    message = '''Subject:Recovery Password OTP\n''' + m1 + OTP + m2

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("kongknitec0000@gmail.com", "icmakjglgfgwmgcj")
    s.sendmail("kongknitec0000@gmail.com", emailid, message)
    return OTP
