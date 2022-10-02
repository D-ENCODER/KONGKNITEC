# Date    : 02/09/22 10:30 pm
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
from firebase_admin import firestore, credentials
import firebase_admin


class FirebaseDatabase:
    """
    class for executing backend queries and database related functions.
    """
    def __init__(self):
        # Using jason file to initialize an app instance in the constructor
        cred = credentials.Certificate("Backend/serviceAccountKey.json")
        firebase_admin.initialize_app(cred)

    @staticmethod
    def _check_exists(collection, email):
        """
        checks if the user already exists in the database.
        returns False if not found and True otherwise.
        """
        db = firestore.client()
        # get all the documents in the collection
        doc = db.collection(collection).get()
        # iterate through the documents
        for i in range(len(doc)):
            # check if the email is already present in the database
            if doc[i].to_dict()['email'] == email:
                return True
        return False

    def dbSignUp(self, email, password):
        """
        adds the user to the database if the user does not already exist.
        takes email password and key as arguments.
        """
        db = firestore.client()
        # check if the user already exists
        if not self._check_exists('users', email):
            # add the user to the database
            db.collection('users').document().set({
                'email': email, 'password': password})
        else:
            print('already exists')
