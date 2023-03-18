# Date    : 18-03-2023 11:52
# Author  : DENCODER (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0
import os
import sqlite3 as sql


class DatasetSqliteServices:
    def __init__(self):
        self.conn = sql.connect('Backend/Database/local_user.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Dataset (id INTEGER PRIMARY KEY AUTOINCREMENT, EnrollmentNo "
                            "TEXT, Name TEXT, Email TEXT, Date DATETIME DEFAULT CURRENT_TIMESTAMP)")
        self.conn.commit()

    def insertDatasetDetails(self, enrollno, name, email):
        self.cursor.execute("INSERT INTO Dataset (EnrollmentNo, Name, Email) VALUES (?, ?, ?)", (enrollno, name, email))
        self.conn.commit()
        self.cursor.close()

    def getDatasetDetails(self):
        self.cursor.execute("SELECT * FROM Dataset")
        return self.cursor.fetchall()

    def updateDatasetDetails(self, enrollno, name, email, id):
        self.cursor.execute("UPDATE Dataset SET EnrollmentNo=?, Name=?, Email=? WHERE id=?", (enrollno, name, email, id))
        self.conn.commit()
        self.cursor.close()

    def getId(self):
        self.cursor.execute("SELECT id FROM Dataset")
        return self.cursor.fetchone()
