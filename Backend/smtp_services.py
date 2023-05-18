# Date    : 12/08/22 6:36 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import datetime
import math
import platform
import random
import smtplib
from email.mime.text import MIMEText

import requests


def sendVerifyOtp(email):
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]

    message = '<html><head><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" ' \
              'href="https://fonts.gstatic.com" crossorigin><link ' \
              'href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap" rel="stylesheet"><meta ' \
              'http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="viewport" ' \
              'content="width=device-width, initial-scale=1.0"><title>Verify your login</title></head><body ' \
              'style="font-family: "Ubuntu Mono", monospace; margin: 0px; padding: 0px; background-color: ' \
              '#1A1A1A;"><table ' \
              'role="presentation"style="width: 100%; border-collapse: collapse; border: 0px; border-spacing: 0px; ' \
              'font-family: "Ubuntu Mono", monospace; background-color: #1A1A1A;"><tbody><tr><td align="center" ' \
              'style="padding: ' \
              '1rem 2rem; vertical-align: top; width: 100%;"><table role="presentation" style="max-width: 600px; ' \
              'border-collapse: collapse; border: 0px; border-spacing: 0px; text-align: left;"><tbody><tr><td ' \
              'style="padding: 40px 0px 0px;"><div style="text-align: left;"><div style="padding-bottom: ' \
              '20px; background-color: #1A1A1A;"><center><img src="https://lh5.googleusercontent.com/-JwsfefO8lt' \
              '-Zt9y5SMEaA2LB4JEH6ng4FDjrrMAWYgLf6rwWgKm8m2lyCNhxKngPD4=w2400" alt="Kongknitec logo" style="width: ' \
              '120px;"></div></div><div ' \
              'style="padding: 20px; background-color: #1A1A1A;"><div style="color: #FFFFFF; text-align: left;"><h1 ' \
              'style="margin: 1rem 0">Verification code</h1><p style="padding-bottom: 16px">Please use the ' \
              'verification code below to sign in. Do not forward or give this code to anyone.</p><p ' \
              'style="padding-bottom: 16px; color: #64FFDA"><strong style="font-size: 150%">' + OTP + \
              '</strong></p><p style="padding-bottom: 16px">If you didn\'t request this, ' \
              'you can ignore this email. This is an auto generated email so please don\'t reply ' \
              'to this email.</p><p style="padding-bottom: 16px">Thanks,<br>The Kongknitec ' \
              'team</p></div><div style="padding-top: 20px; color: #1de9b6; text-align: ' \
              'center;"><p style="padding-bottom: 16px">Made with ♥ by Kongknitec ' \
              'Team</p></div></div></td></tr></tbody></table></td></tr></tbody></table></body></html> '
    message = MIMEText(message, "html")
    message = message.as_string()
    message = '''Subject:Email Verification OTP\n''' + message
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("kongknitec0000@gmail.com", "nfjbdunjcgxlwxue")
    s.sendmail("kongknitec0000@gmail.com", email, message)
    return OTP


def sendResetOtp(email):
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]

    message = '<html><head><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" ' \
              'href="https://fonts.gstatic.com" crossorigin><link ' \
              'href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap" rel="stylesheet"><meta ' \
              'http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="viewport" ' \
              'content="width=device-width, initial-scale=1.0"><title>Reset your password</title></head><body ' \
              'style="font-family: "Ubuntu Mono", monospace; margin: 0px; padding: 0px; background-color: ' \
              '#1A1A1A;"><table ' \
              'role="presentation"style="width: 100%; border-collapse: collapse; border: 0px; border-spacing: 0px; ' \
              'font-family: "Ubuntu Mono", monospace; background-color: #1A1A1A;"><tbody><tr><td align="center" ' \
              'style="padding: ' \
              '1rem 2rem; vertical-align: top; width: 100%;"><table role="presentation"style="max-width: 600px; ' \
              'border-collapse: collapse; border: 0px; border-spacing: 0px; text-align: left;"><tbody><tr><td ' \
              'style="padding: 40px 0px 0px;"><div style="text-align: left;"><div style="padding-bottom: ' \
              '20px; background-color: #1A1A1A;"><center><img ' \
              'src="https://lh5.googleusercontent.com/-JwsfefO8lt' \
              '-Zt9y5SMEaA2LB4JEH6ng4FDjrrMAWYgLf6rwWgKm8m2lyCNhxKngPD4=w2400" alt="Company"style="width: ' \
              '120px;"></div></div><div style="padding: 20px; background-color: #1A1A1A;"><div style="color: #FFFFFF; ' \
              'text-align: left;"><h1 style="margin: 1rem 0">Trouble signing in?</h1><p style="padding-bottom: ' \
              '16px">We\'ve received a request to reset the password for this user account. Do not forward or give ' \
              'this code to anyone.</p><p style="padding-bottom: 16px; color: #64FFDA"><strong style="font-size: ' \
              '150%;">' + OTP + \
              '</strong></p><p style="padding-bottom: 16px">If you didn\'t ask to reset your ' \
              'password, you can ignore this email.</p><p style="padding-bottom: 16px">Thanks,<br>The Kongknitec ' \
              'Team</p></div><div style="padding-top: 20px; color: #1de9b6; text-align: center;"><p ' \
              'style="padding-bottom: 16px">Made with ♥ by Kongknitec ' \
              'Team</p></div></div></td></tr></tbody></table></td></tr></tbody></table></body></html> '
    message = MIMEText(message, "html")
    message = message.as_string()
    message = '''Subject:Password Reset\n''' + message
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("kongknitec0000@gmail.com", "nfjbdunjcgxlwxue")
    s.sendmail("kongknitec0000@gmail.com", email, message)
    return OTP


def sendWelcome(email, name, bool):
    if bool:
        rolelist = '<ul><li>Add New Users</li><li>View Attendance</li><li>Take Attendance</li><li>Train ' \
                   'Dataset</li><li>Generate Report</li><li>Edit profile ' \
                   'details</li></ul> '
    else:
        rolelist = '<ul><li>View Attendance</li><li>Train Dataset(admin permission required)</li><li>Edit profile ' \
                   'details</li></ul> '
    message = '<html><head><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" ' \
              'href="https://fonts.gstatic.com" crossorigin><link ' \
              'href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap" rel="stylesheet"><meta ' \
              'http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="viewport" ' \
              'content="width=device-width, initial-scale=1.0"><title>Welcome to Kongknitec</title></head><body ' \
              'style="font-family: "Ubuntu Mono", monospace; margin: 0px; padding: 0px; background-color: ' \
              '#1A1A1A;"><table role="presentation"style="width: 100%; border-collapse: collapse; border: 0px; ' \
              'border-spacing: 0px; font-family: "Ubuntu Mono", monospace; background-color: #1A1A1A;"><tbody><tr><td ' \
              'align="center" style="padding: 1rem 2rem; vertical-align: top; width: 100%;"><table ' \
              'role="presentation"style="max-width: 600px; border-collapse: collapse; border: 0px; border-spacing: ' \
              '0px; text-align: left;"><tbody><tr><td style="padding: 40px 0px 0px;"><div style="text-align: ' \
              'left;"><div style="padding-bottom: 20px; background-color: #1A1A1A;"><center><img ' \
              'src="https://lh5.googleusercontent.com/-JwsfefO8lt' \
              '-Zt9y5SMEaA2LB4JEH6ng4FDjrrMAWYgLf6rwWgKm8m2lyCNhxKngPD4=w2400" alt="Company"style="width: ' \
              '120px;"></center></div></div><div style="padding: 20px; background-color: #1A1A1A;"><div style="color: ' \
              '#FFFFFF; text-align: left;"><h1 style="margin: 1rem 0">Welcome to Kongknitec</h1><p ' \
              'style="padding-bottom: 16px">Hello <font color="#64FFDA"><strong>' + name + \
              '</strong></font>,' \
              '</p><p style="padding' \
              '-bottom: 16px">Thank you for signing up to Kongknitec. We\'re really happy to ' \
              'have youonboard! </p><p style="padding-bottom: 16px">Roles that you got<br>' + rolelist + \
              '</p><p ' \
              'style="padding-bottom: 16px">The Kongknitec project is open source and 100% ' \
              'free to use(no subscription required). If you want the source code then link is down below, ' \
              'and do give it a star to support the project.</p><p style="padding-bottom: 16px"><a ' \
              'href="https://github.com/D-ENCODER/KONGKNITEC" style="color:#1de9b6">Link to source ' \
              'code</a></p><p>Warm regards,</p></span><br><span style="color: #999">The Kongknitec ' \
              'Team</span></p></div><div style="padding-top: 20px; color: #1de9b6; text-align: center;"><p ' \
              'style="padding-bottom: 16px">Made with ♥ by Kongknitec ' \
              'Team</p></div></div></td></tr></tbody></table></td></tr></tbody></table></body></html> '
    message = MIMEText(message, "html")
    message = '''Subject: Welcome to Kongknitec\n''' + message.as_string()
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("kongknitec0000@gmail.com", "nfjbdunjcgxlwxue")
    s.sendmail("kongknitec0000@gmail.com", email, message)


def sendAdminId(email):
    digits = "0123456789"
    AdminId = "314"
    for i in range(9):
        AdminId += digits[math.floor(random.random() * 10)]

    message = '<html><head><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" ' \
              'href="https://fonts.gstatic.com" crossorigin><link ' \
              'href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap" rel="stylesheet"><meta ' \
              'http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="viewport" ' \
              'content="width=device-width, initial-scale=1.0"><title>Admin Id Generated</title></head><body ' \
              'style="font-family: "Ubuntu Mono", monospace; margin: 0px; padding: 0px; background-color: ' \
              '#1a1a1a;"><table role="presentation"style="width: 100%; border-collapse: collapse; border: 0px; ' \
              'border-spacing: 0px; font-family: "Ubuntu Mono", monospace; background-color: #1a1a1a;"><tbody><tr><td ' \
              'align="center" style="padding: 1rem 2rem; vertical-align: top; width: 100%;"><table ' \
              'role="presentation"style="max-width: 600px; border-collapse: collapse; border: 0px; border-spacing: ' \
              '0px; text-align: left;"><tbody><tr><td style="padding: 40px 0px 0px;"><div style="text-align: ' \
              'left;"><div style="padding-bottom: 20px; background-color: #1A1A1A;"><center><img ' \
              'src="https://lh5.googleusercontent.com/-JwsfefO8lt' \
              '-Zt9y5SMEaA2LB4JEH6ng4FDjrrMAWYgLf6rwWgKm8m2lyCNhxKngPD4=w2400" alt="Company"style="width: ' \
              '120px;"></div></div><div style="padding: 20px; background-color: #1A1A1A;"><div style="color: #FFFFFF; ' \
              'text-align: left;"><h1 style="margin: 1rem 0">Admin Id generated</h1><p style="padding-bottom: ' \
              '16px">Please use the Admin Id below to login to your account. Please do not share your Admin Id to ' \
              'anyone</p><p style="padding-bottom: 16px; color: #64FFDA"><strong style="font-size: ' \
              '130%">' + AdminId + \
              '</strong></p><p style="padding-bottom: 16px">This is an auto generated email so ' \
              'please don\'t reply to this email. For queries please contact <a ' \
              'href="mailto:kongknitec0000@gmail.com" style="color: ' \
              '#1de9b6;">kongknitec0000@gmail.com</a></p><p ' \
              'style="padding-bottom: 16px">Thanks,<br>The Kongknitec Team</p></div><div style="padding-top: 20px; ' \
              'color: #1de9b6; text-align: center;"><p style="padding-bottom: 16px">Made with ♥ by Kongknitec ' \
              'Team</p></div></div></td></tr></tbody></table></td></tr></tbody></table></body></html> '
    message = MIMEText(message, "html")
    message = '''Subject: Your Admin Id is generated\n''' + message.as_string()
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("kongknitec0000@gmail.com", "nfjbdunjcgxlwxue")
    s.sendmail("kongknitec0000@gmail.com", email, message)
    return int(AdminId)


def sendemail():
    digits = "0123456789"
    AdminId = "314"
    for i in range(9):
        AdminId += digits[math.floor(random.random() * 10)]

    message = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="viewport" ' \
              'content="width=device-width, initial-scale=1.0"><title>Verify your login</title></head><body ' \
              'style="font-family: "Ubuntu Mono"; margin: 0px; padding: 0px; background-color: #1A1A1A;"><table ' \
              'role="presentation"style="width: 100%; border-collapse: collapse; border: 0px; border-spacing: 0px; ' \
              'font-family: "Ubuntu Mono"; background-color: #1A1A1A;"><tbody><tr><td align="center" style="padding: ' \
              '1rem 2rem; vertical-align: top; width: 100%;"><table role="presentation" style="max-width: 600px; ' \
              'border-collapse: collapse; border: 0px; border-spacing: 0px; text-align: left;"><tbody><tr><td ' \
              'style="padding: 40px 0px 0px;"><div style="text-align: left;"><div style="padding-bottom: ' \
              '20px; background-color: #1A1A1A;"><center><img src="https://lh5.googleusercontent.com/-JwsfefO8lt' \
              '-Zt9y5SMEaA2LB4JEH6ng4FDjrrMAWYgLf6rwWgKm8m2lyCNhxKngPD4=w2400" alt="Kongknitec logo" style="width: ' \
              '120px;"></div></div><div ' \
              'style="padding: 20px; background-color: #1A1A1A;"><div style="color: #FFFFFF; text-align: left;"><h1 ' \
              'style="margin: 1rem 0">Verification code</h1><p style="padding-bottom: 16px">Please use the ' \
              'verification code below to sign in.</p><p style="padding-bottom: 16px; color: #64FFDA"><strong ' \
              'style="font-size: 130%">' + AdminId + \
              '</strong></p><p style="padding-bottom: 16px">If you didn\'t request this, ' \
              'you can ignore this email. This is an auto generated email so please don\'t reply ' \
              'to this email.</p><p style="padding-bottom: 16px">Thanks,<br>The Kongknitec ' \
              'team</p></div><div style="padding-top: 20px; color: #1de9b6; text-align: ' \
              'center;"><p style="padding-bottom: 16px">Made with ♥ by Kongknitec ' \
              'Team</p></div></div></td></tr></tbody></table></td></tr></tbody></table></body></html> '
    email_message = MIMEText(message, "html")
    email_message = email_message.as_string()
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("kongknitec0000@gmail.com", "nfjbdunjcgxlwxue")
    s.sendmail("kongknitec0000@gmail.com", 'hetcjoshi1684@gmail.com', email_message)


def sendPasswordChanged(email):
    def get_ip():
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]

    def get_location():
        ip_address = get_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        location_data = {
            "ip": ip_address,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name")
        }
        return location_data

    location = get_location()
    message = '<html><head><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" ' \
              'href="https://fonts.gstatic.com" crossorigin><link ' \
              'href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap" rel="stylesheet"><meta ' \
              'http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="viewport" ' \
              'content="width=device-width, initial-scale=1.0"><title>Password changed</title></head><body ' \
              'style="font-family: "Ubuntu Mono", monospace; margin: 0px; padding: 0px; background-color: ' \
              '#1a1a1a;"><table role="presentation"style="width: 100%; border-collapse: collapse; border: 0px; ' \
              'border-spacing: 0px; font-family: "Ubuntu Mono", monospace; background-color: #1a1a1a;"><tbody><tr><td ' \
              'align="center" style="padding: 1rem 2rem; vertical-align: top; width: 100%;"><table ' \
              'role="presentation" style="max-width: 600px; border-collapse: collapse; border: 0px; border-spacing: ' \
              '0px; text-align: left;"><tbody><tr><td style="padding: 40px 0px 0px;"><div style="text-align: ' \
              'left;"><div style="padding-bottom: 20px; background-color: #1a1a1a;"><center><img ' \
              'src="https://lh5.googleusercontent.com/-JwsfefO8lt' \
              '-Zt9y5SMEaA2LB4JEH6ng4FDjrrMAWYgLf6rwWgKm8m2lyCNhxKngPD4=w2400" alt="Company" style="width: ' \
              '120px;"></center></div></div><div style="padding: 20px; background-color: #1a1a1a;"><div style="color: ' \
              '#ffffff; text-align: left;"><h2 style="margin: 1rem 0">Did you change your password?</h2><p ' \
              'style="padding-bottom: 16px">We noticed the password for your Kongknitec account was recently changed. ' \
              'If it was you, you can safely disregard this email.</p><p style="padding-bottom: 16px">When: ' \
              + str(datetime.datetime.now()) + '<br>' + \
              'Where: ' + location['city'] + ' ' + location['region'] + ' ' + location['country'] + '<br>' + \
              'Device-type: ' + platform.system() + ' ' + platform.release() + '<br>' + \
              '</p><p style="padding-bottom: 16px">If you didn\'t change your password, please reach out to us ' \
              'at <a href="mailto:kongknitec0000@gmail.com" style="color: ' \
              '#64FFDA;">kongknitec0000@gmail.com</a>.</p><p style="padding-bottom: 16px">Thanks,<br>The Kongknitec ' \
              'Team</p></div><div style="padding-top: 20px; color: #1de9b6; text-align: center;"><p ' \
              'style="padding-bottom: 16px">Made with ♥ by Kongknitec ' \
              'Team</p></div></div></td></tr></tbody></table></td></tr></tbody></table></body></html> '
    message = MIMEText(message, "html")
    message = '''Subject: Your password has been changed\n''' + message.as_string()
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("kongknitec0000@gmail.com", "nfjbdunjcgxlwxue")
    s.sendmail("kongknitec0000@gmail.com", email, message)


