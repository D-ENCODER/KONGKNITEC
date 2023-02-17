# Date    : 28/01/23 11:00 am
# Author  : dencoder (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import sqlite3 as sql

class SqliteServices:
    """
        Main class of SqliteServices. Handles all the sqlite database operations.
    """

    def __init__(self):
        self.conn = sql.connect("Backend/Database/local_user.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS UserDetails (Email TEXT, Password TEXT, Fname TEXT, "
                            "Lname TEXT, Gender TEXT, Dob INTEGER, Phoneno TEXT, Enrollno TEXT)")
        self.conn.commit()

    def insertSignupDetails(self, email, password):
        """
            :param email Email-Id of the User
            :param password Encrypted password of the User
            :returns None

            Inserts Email and Password into the local database.
        """
        self.cursor.execute('''INSERT INTO UserDetails(Email, Password, Fname, Lname, Gender, Dob, Phoneno, Enrollno)
                            VALUES ("{}", "{}", NULL, NULL, NULL, NULL, NULL, NULL)'''.format(email, password))
        self.conn.commit()

    def insertPersonalDetails(self, fname, lname, gender, dob):
        """
            :param fname First Name of the User
            :param lname Last Name of the User
            :param gender Gender of the User
            :param dob Date of Birth of the User
            :returns None

            Inserts Personal details into the local database.
        """
        self.cursor.execute('''UPDATE UserDetails SET Fname="{}", Lname="{}", Gender="{}", Dob="{}"'''
                            .format(fname, lname, gender, dob))
        self.conn.commit()

    def insertContactDetails(self, phoneno, enrollno):
        """
            :param phoneno Contact Number of User
            :param enrollno Enrollment Number of User
            :returns None

            Inserts Contact details into the local database.
        """
        self.cursor.execute('''UPDATE UserDetails SET Phoneno={}, Enrollno="{}"'''.format(phoneno, enrollno))
        self.conn.commit()

    def fetch(self, columnName):
        """
            :param columnName this contains column name that is to be fetched
            :returns None

            Fetches specific column wise data from the database.
        """
        self.cursor.execute("SELECT " + columnName + " FROM UserDetails")
        return self.cursor.fetchall()

    def fetchall(self):
        """
            Fetches all the data from the database.
        """
        self.cursor.execute("SELECT * FROM UserDetails")
        return self.cursor.fetchall()

    def login(self, enrollmentNo, dateTime):
        """
        :param enrollmentNo: Enrollment number of the user that logs in.
        :param dateTime: Date and Time of the session creation
        :returns: None
        """
        self.cursor.execute("CREATE TABLE IF NOT EXISTS LoginDetails(enrollNo TEXT, dateTime INTEGER)")
        self.cursor.execute('''INSERT INTO LoginDetails(enrollNo, dateTime) VALUES ("{}", "{}")'''.format(enrollmentNo,
                                                                                                          dateTime))
        self.conn.commit()

    def checkLogin(self):
        result = self.cursor.execute('''SELECT count(*) FROM sqlite_master WHERE type="table" AND 
        name="LoginDetails"''')
        self.conn.commit()
        return result.fetchall()

    # def remove(self, name):
    #     """
    #         Removes the data from the database.
    #     """
    #     self.cursor.execute("DELETE FROM contacts WHERE name=?", (name,))
    #     self.conn.commit()
    #
    # def update(self, name, phone, email, address):
    #     """
    #         Updates the data in the database.
    #     """
    #     self.cursor.execute("UPDATE contacts SET phone=?, email=?, address=? WHERE name=?",
    #                         (phone, email, address, name))
    #     self.conn.commit()
    def complete(self):
        self.cursor.execute("DROP TABLE UserDetails")

    def __del__(self):
        self.conn.close()
