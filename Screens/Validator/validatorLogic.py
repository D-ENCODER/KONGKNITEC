# Date    : 24/09/22 11:02 am
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
from numpy.core.defchararray import strip
import configure


class Validator:
    """
    This class is used to validate the user input.
    this contains many functions like validate email and password and so on.
    """

    @staticmethod
    def validate_email(email):
        """
        This function is used to validate the email address.
        :param email: email address that is to be validated.
        :return: True if email is valid else False
        """
        # check if email contains @ and . or not
        if strip(email) == '':
            return [False, 'Email cannot be empty']
        elif '@' not in email or '.' not in email:
            # return True if email is valid else False
            return [False, 'Invalid email address']
        elif email.count("@") > 1:
            return [False, 'Email address cannot contain \nmore than one @']
        else:
            return [True]

    @staticmethod
    def validate_password(password):
        """
        This function is used to validate the password.
        :param password: password that is to be validated
        :return: True if password is valid else False
        """
        # check if password contains at least one special character
        SpecialSym = ['$', '@', '#', '%', '!', '^', '&', '*', '(', ')', '-', '_', '+', '=']
        val = [True]
        # check if password is not empty
        if strip(password) == '':
            return [False, 'Password cannot be empty']
        # check if password contains at least 8 digit
        elif len(password) < 8:
            return [False, 'Length should be at least 8']
        # check if password contains less than 20 digit
        elif len(password) > 20:
            return [False, 'Length should be not be greater \nthan 20']
        # check if password contains at least one number
        elif not any(char.isdigit() for char in password):
            return [False, 'Password should have at least \none numeral']
        # check if password contains at least one uppercase letter
        elif not any(char.isupper() for char in password):
            return [False, 'Password should have at least \none uppercase letter']
        # check if password contains at least one lowercase letter
        elif not any(char.islower() for char in password):
            return [False, 'Password should have at least \none lowercase letter']
        # check if password contains at least one special character
        elif not any(char in SpecialSym for char in password):
            return [False, 'Password should have at least \none of the symbols $@#%!^&*()-_+=']
        else:
            return [val, '']
