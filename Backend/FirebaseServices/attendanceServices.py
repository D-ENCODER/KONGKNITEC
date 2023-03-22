# Date    : 22-03-2023 15:04
# Author  : DENCODER (hetcjoshi1684@gmail.com)
# GitHub    : (https://github.com/D-ENCODER)
# Twitter    : (https://twitter.com/Hetjoshi1684)
# Version : 1.0.0

from firebase_admin import firestore


class AttendanceServices:

    def __init__(self):
        self.db = firestore.client()

    def insertAttendance(self, date, data):
        try:
            doc = self.db.collection('Attendance').document(date)
            if not doc.get().exists:
                self.db.collection('Attendance').document(date).set({'Date': date, 'Enrollment': data})
            else:
                enrolls = self.getAttendance(date)
                enrolls = enrolls['Enrollment']
                for enroll in data:
                    if enroll not in enrolls:
                        enrolls.append(enroll)
                print(enrolls)
                self.db.collection('Attendance').document(date).update({'Enrollment': enrolls})
        except Exception as e:
            file = open('KONGKNITEC.log', 'a')
            file.write(str(e))
            file.close()

    def getAttendance(self, date):
        try:
            doc = self.db.collection('Attendance').document(date)
            if not doc.get().exists:
                return None
            else:
                return doc.get().to_dict()
        except Exception as e:
            file = open('KONGKNITEC.log', 'a')
            file.write(str(e))
            file.close()
