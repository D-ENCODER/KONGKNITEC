# Date    : 02/09/22 10:30 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

from firebase_admin import firestore, credentials
import firebase_admin
from datetime import datetime

import configure
from Backend.encryptor import encrypt
from Helper_Functions.custom_error_box import CustomBox


class FirebaseDatabase:
    """
    class for executing backend queries and database related functions.
    """

    def __init__(self):
        # Using jason file to initialize an app instance in the constructor
        cred = credentials.Certificate("Backend/serviceAccountKey.json")
        firebase_admin.initialize_app(cred)

    @staticmethod
    def check_email_exists(collection, email):
        """
        checks if the user already exists in the database.
        returns False if not found and True otherwise.
        """
        db = firestore.client()
        # get all the documents in the collection
        doc = db.collection(collection).where('email', '==', email).get()
        if len(doc) > 0:
            return True
        return False

    @staticmethod
    def check_enrollment_exists(collection, enrollment):
        """
        checks if the user already exists in the database.
        returns False if not found and True otherwise.
        """
        db = firestore.client()
        # get all the documents in the collection
        doc = db.collection(collection).where('enrollment', '==', enrollment).get()
        if len(doc) > 0:
            return True
        return False

    def dbSignUp(self, credential, db_collection):
        """
        adds the user to the database if the user does not already exist.
        takes email password and key as arguments.
        """
        db = firestore.client()
        # check if the user already exists
        # add the user to the database
        db.collection(db_collection).document().set(credential)

    def getAdminCode(self):
        """
        returns the admin code from the database.
        """
        db = firestore.client()
        # get the admin code from the database
        doc = db.collection('AdminCode').document('ADMINCODE').get()
        return doc.to_dict()['code']

    def getLoginDetails(self, enroll, bool):
        """
        returns the login details from the database.
        """
        db = firestore.client()
        # get the login details from the database
        if bool:
            query = db.collection('Admin_details').where('enrollment', '==', int(enroll))
        else:
            query = db.collection('User_details').where('enrollment', '==', int(enroll))

        for doc in query.stream():
            return doc.to_dict()['password']
        return None

    def dbLogin(self, enrollment):
        """
        updates the last login date of the user.
        """
        db = firestore.client()
        # get the login details from the database
        db.collection('Login').document().set({'enrollment': enrollment, 'date': datetime.now()})

    def dbUpdatePassword(self, email, password, bool):
        """
        updates the password of the user.
        """
        db = firestore.client()
        # get the login details from the database
        if bool:
            query = db.collection('Admin_details').where('email', '==', email).stream()
            for doc in query:
                doc_id = doc.id
            print('helllo world')
            db.collection('Admin_details').document(doc_id).update({'password': password})
        else:
            query = db.collection('User_details').where('email', '==', email).stream()
            for doc in query:
                doc_id = doc.id
            print('helllo world')
            db.collection('User_details').document(doc_id).update({'password': password})
