# Date    : 02/09/22 10:30 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

from firebase_admin import firestore
from datetime import datetime


class AuthenticationServices:
    """
    class for executing backend queries and database related functions.
    """

    def __init__(self):
        """
        constructor of the class to initialize the database.
        """
        self.db = firestore.client()

    def check_email_exists(self, collection, email):
        """
        checks if the user already exists in the database.
        returns False if not found and True otherwise.
        """
        # get all the documents in the collection
        doc = self.db.collection(collection).where('Email', '==', email).get()
        if len(doc) > 0:
            return True
        return False

    def check_enrollment_exists(self, collection, enrollment):
        """
        checks if the user already exists in the database.
        returns False if not found and True otherwise.
        """
        # get all the documents in the collection
        doc = self.db.collection(collection).where('Enrollment', '==', enrollment).get()
        if len(doc) > 0:
            return True
        return False

    def dbSignUp(self, credential, db_collection):
        """
        adds the user to the database if the user does not already exist.
        takes email password and key as arguments.
        """
        # check if the user already exists
        # add the user to the database
        self.db.collection(db_collection).document().set(credential)

    def getAdminCode(self):
        """
        returns the admin code from the database.
        """
        # get the admin code from the database
        doc = self.db.collection('AdminCode').document('ADMINCODE').get()
        return doc.to_dict()['code']

    def getLoginDetails(self, enroll, boolean):
        """
        returns the login details from the database.
        """
        # get the login details from the database
        if boolean:
            query = self.db.collection('Admin_details').where('Enrollment', '==', int(enroll))
        else:
            query = self.db.collection('User_details').where('Enrollment', '==', int(enroll))

        for doc in query.stream():
            return doc.to_dict()['password']
        return None

    def dbLogin(self, enrollment):
        """
        updates the last login date of the user.
        """
        # get the login details from the database
        self.db.collection('Login').document().set({'Enrollment': enrollment, 'DateTime': datetime.now()})

    def dbUpdatePassword(self, email, password, bool):
        """
        updates the password of the user.
        """
        # get the login details from the database
        if bool:
            query = self.db.collection('Admin_details').where('Email', '==', email).stream()
            for doc in query:
                self.db.collection('Admin_details').document(doc.id).update({'Password': password})
        else:
            query = self.db.collection('User_details').where('Email', '==', email).stream()
            for doc in query:
                self.db.collection('User_details').document(doc.id).update({'Password': password})
