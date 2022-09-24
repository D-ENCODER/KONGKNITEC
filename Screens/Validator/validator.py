# Date    : 24/09/22 11:02 am
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

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
        if '@' in email and '.' in email:
            # return True if email is valid else False
            return True
        print('invalid email')
        return False

    @staticmethod
    def validate_password(password):
        """
        This function is used to validate the password.
        :param password: password that is to be validated
        :return: True if password is valid else False
        """
        # check if password contains at least one special character
        SpecialSym = ['$', '@', '#', '%', '!', '^', '&', '*', '(', ')', '-', '_', '+', '=']
        val = True
        # check if password contains at least 6 digit
        if len(password) < 6:
            print('length should be at least 6')
            val = False
        # check if password contains less than 20 digit
        if len(password) > 20:
            print('length should be not be greater than 20')
            val = False
        # check if password contains at least one number
        if not any(char.isdigit() for char in password):
            print('Password should have at least one numeral')
            val = False
        # check if password contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            print('Password should have at least one uppercase letter')
            val = False
        # check if password contains at least one lowercase letter
        if not any(char.islower() for char in password):
            print('Password should have at least one lowercase letter')
            val = False
        # check if password contains at least one special character
        if not any(char in SpecialSym for char in password):
            print('Password should have at least one of the symbols $@#')
            val = False
        if val:
            return val
