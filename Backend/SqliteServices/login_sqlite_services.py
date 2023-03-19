# Date    : 19-03-2023 10:09
# Author  : DENCODER (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import sqlite3 as sql


class LoginSqliteServices:
    """
    Main class of LoginSqliteServices. Handles all the login related sqlite database operations.
    """
    def __init__(self):
        """
        This is the constructor of LoginSqliteServices class. It creates a connection with the local database and creates
        a table if it doesn't exist.
        """
        self.conn = sql.connect('Backend/Database/local_user.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS LoginDetails(enrollNo TEXT, date TEXT)")
        self.conn.commit()

    def insertLoginDetails(self, enrollno):
        """
        This method inserts the login details of the user into the database.
        :param enrollno: Enrollment No of the user
        :param datetime: Date and time of login
        :return: None
        """
        self.cursor.execute("INSERT INTO LoginDetails(enrollNo, date) VALUES ({}, datetime('now', 'localtime'))".format(enrollno))
        self.conn.commit()

    def getLoginDetails(self):
        """
        This method returns the login details of the user.
        :return: List of tuples containing the login details of the user.
        """
        self.cursor.execute("SELECT * FROM LoginDetails")
        return self.cursor.fetchall()

    def updateLoginDetails(self, enrollno):
        """
        This method updates the login details of the user. Used when the user logs out or session expires.
        :param enrollno: Enrollment No of the user
        :param datetime: Date and time of new login or session
        :return: None
        """
        self.cursor.execute("UPDATE LoginDetails SET date=datetime('now', 'localtime'), enrollNo={}".format(enrollno))
        self.conn.commit()

    def __del__(self):
        """
        This is the destructor of LoginSqliteServices class. It closes the connection with the database.
        """
        self.conn.close()
