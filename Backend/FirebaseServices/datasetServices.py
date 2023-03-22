# Date    : 22-03-2023 12:07
# Author  : DENCODER (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import datetime
from firebase_admin import firestore
from Helper_Functions.imgToString import imgToStringConverter, stringToImgConverter


class DatasetServices:
    """
    class for executing backend queries and database related functions for Dataset.
    """

    def __init__(self):
        self.db = firestore.client()

    def addDataset(self, enroll, img):
        """
        Adds the user's images to the database if the user does not already exist or updates if it exists.
        :param enroll: Enrollment no of the user
        :param img: Base64 string of the image
        :return: None
        """
        img = imgToStringConverter(img)
        doc = self.db.collection('Dataset').document(enroll)
        if not doc.get().exists:
            self.db.collection('Dataset').document(enroll).set({'Enrollment': enroll, 'Image': img, 'DateTime': datetime.datetime.now(tz=datetime.timezone.utc)})
        else:
            self.db.collection('Dataset').document(enroll).update({'Image': img, 'DateTime': datetime.datetime.now(datetime.timezone.utc)})

    def getDataset(self):
        """
        Gets the dataset from the database.
        :return: None
        """
        docs = self.db.collection('Dataset').stream()
        for doc in docs:
            result = self.db.collection('Dataset').document(doc.id).get()
            img = result.to_dict()['Image']
            enroll = result.to_dict()['Enrollment']
            stringToImgConverter(img, enroll)
