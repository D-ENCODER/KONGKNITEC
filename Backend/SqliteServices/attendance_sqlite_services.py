# Date    : 20-03-2023 17:39
# Author  : DENCODER (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

import sqlite3 as sql
from datetime import datetime


class AttendanceSqliteServices:
    """
    This class is used to create a table for attendance and insert the attendance details
    """
    def __init__(self):
        """
        This is the constructor of AttendanceSqliteServices class. It creates a connection with the local database.
        """
        self.conn = sql.connect("Backend/Database/attendance.db")
        self.cursor = self.conn.cursor()

    def createTable(self, name):
        """
        This method creates a table for attendance if it doesn't exist.
        :param name: The name of the table
        :return: None
        """
        name = "A" + name
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Attendance(Id INTEGER, TableName TEXT)")
        self.cursor.execute("SELECT TableName FROM Attendance")
        results = list(self.cursor.fetchall())
        for i in range(len(results)):
            results[i] = results[i][0]
        if name not in results:
            Id = len(results) + 1
            self.cursor.execute("INSERT INTO Attendance (Id, TableName) VALUES ({}, '{}')".format(Id, name))

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS {} (Id INTEGER, EnrollmentNo TEXT, Time TEXT)".format(name))
        self.conn.commit()

    def insertAttendance(self, name, enrollno):
        """
        This method inserts the attendance details into the table.
        :param name: The name of the table
        :param enrollno: The Enrollment of the student
        :return: None
        """
        self.cursor.execute("SELECT Id FROM {}".format("A" + name))
        Id = len(list(self.cursor.fetchall())) + 1
        self.cursor.execute(
            "INSERT INTO {} (Id, EnrollmentNo, Time) VALUES ({}, '{}', datetime('now', 'localtime'))".format("A" + name, Id,
                                                                                                             enrollno))
        self.conn.commit()

    def getAttendance(self, name):
        """
        This method returns the attendance details of the table.
        :param name: The name of the table
        :return: List of tuples containing the attendance details of the table.
        """
        self.cursor.execute("SELECT * FROM {}".format("A" + name))
        return self.cursor.fetchall()

    def getEnrollment(self, name):
        """
        This method returns the enrollment numbers of the students.
        :param name: The name of the table
        :return: List of tuples containing the enrollment numbers of the students.
        """
        self.cursor.execute("SELECT EnrollmentNo FROM {}".format("A" + name))
        return self.cursor.fetchall()

    def getTableDetails(self):
        """
        This method returns the details of the tables.
        :return: List of tuples containing the details of the tables.
        """
        self.cursor.execute("SELECT TableName FROM Attendance")
        return self.cursor.fetchall()

    def __del__(self):
        """
        This is the destructor of AttendanceSqliteServices class. It closes the connection with the database.
        """
        date = datetime.now().strftime("%d%m%Y")
        date = "A" + date
        data = self.getEnrollment(date)
        if not data:
            self.cursor.execute("DELETE FROM Attendance WHERE TableName='{}'".format(date))
            self.cursor.execute("DROP TABLE {}".format(date))
        self.cursor.close()
        self.conn.close()
