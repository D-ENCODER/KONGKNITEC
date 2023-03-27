# Date    : 18-03-2023 11:52
# Author  : DENCODER (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import os
import sqlite3 as sql
from Backend.SqliteServices.signup_sqlite_services import SignupSqliteServices


class DatasetSqliteServices:
    def __init__(self):
        self.conn = sql.connect('Backend/Database/local_user.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Dataset (Id INTEGER, EnrollmentNo "
                            "TEXT, Name TEXT, Email TEXT, Date TEXT)")
        self.conn.commit()

    def insertDatasetDetails(self, enrollno, name, email):
        self.cursor.execute("INSERT INTO Dataset (Id, EnrollmentNo, Name, Email, Date) VALUES ({}, {}, '{}', '{}', datetime("
                            "'now', 'localtime'))".format(len(self.getId())+1, enrollno, name, email))
        self.conn.commit()

    def getDatasetDetails(self):
        self.cursor.execute("SELECT * FROM Dataset")
        return self.cursor.fetchall()

    def getEnrollment(self, id):
        self.cursor.execute(
            "SELECT EnrollmentNo FROM Dataset WHERE Id={}".format(id))
        return self.cursor.fetchall()

    def fetchSpecificDataset(self, column):
        self.cursor.execute("SELECT {} FROM Dataset".format(column))
        return self.cursor.fetchall()

    def massInsert(self, enrollList):
        obj = SignupSqliteServices()
        registered = list(self.fetchSpecificDataset('EnrollmentNo'))
        for enroll in enrollList:
            if enroll not in registered:
                data = list(obj.fetchCondition('FName, Lname, Email', enroll)[0])
                if not data:
                    continue
                else:
                    names = list(self.fetchSpecificDataset('Name'))
                    for i in range(len(names)):
                        names[i] = names[i][0]
                    name = data[0] + ' ' + data[1]
                    if name not in names:
                        self.insertDatasetDetails(enroll, name, data[2])

    def getId(self):
        self.cursor.execute("SELECT Id FROM Dataset")
        return self.cursor.fetchall()
