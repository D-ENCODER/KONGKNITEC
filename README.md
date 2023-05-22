![Face Recognition Banner](https://user-images.githubusercontent.com/86153190/184497475-a5e6d0e4-5704-4f01-ad75-e69ea6556744.png)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
# KONGKNITEC

## What is Face Recognition?
- Facial recognition is a way of identifying or confirming an individual’s identity using their face. Facial recognition systems can be used to identify people in photos, videos, or in real-time. Facial recognition is a category of biometric security. Other forms of biometric software include voice recognition, fingerprint recognition, and eye retina or iris recognition. The technology is mostly used for security and law enforcement, though there is increasing interest in other areas of use.

## Why and How?
- Attendance marking in a classroom during a lecture is not only a onerous task but also a time consuming one at that. Due to an unusually high number of students present during the lecture there will always be a probability of proxy attendance(s). Attendance marking with conventional methods has been an area of challenge. The growing need of efficient and automatic techniques of marking attendance is a growing challenge in the area of face recognition. In recent years, the problem of automatic attendance marking has been widely addressed through the use of standard biometrics like fingerprint and Radio frequency Identification tags etc., However, these techniques lack the element of reliability. In this proposed project an automated attendance marking and management system is proposed by making use of face detection and recognition algorithms. The main objective of this work is to make the attendance marking and management system efficient, time saving, simple and easy. Here faces will be recognized using face recognition algorithms like HAAR classifiers. The processed image will then be compared against the existing stored record and then attendance is marked in the database accordingly. Compared to existing system traditional attendance marking system, this system reduces the workload of people. This proposed system will be implemented with 5 phases such as Database Creation, Image Capturing, Face Detection, Face comparison and Recognition, Updating of Attendance in database. Last but not least, saving the data in an excel format and mailing to the respective lecturer.

## Why Using Face For Recognition?
- Fingerprint based recognition system: - In the Fingerprint based existing attendance system, a portable fingerprint device needs to be configured with the students fingerprint earlier. Later either during the lecture hours or before, the student needs to record the fingerprint on the configured device to ensure their attendance for the day. The problem with this approach is that during the lecture time it may distract the attention of the students and also it needs physical touch.

- RFID(Radio Frequency Identification) Based recognition system: - In the RFID based existing system, the student needs to carry a Radio Frequency Identity Card with them and place the ID on the card reader to record their presence for the day. The system is capable of to connect to RS232 and record the attendance to the saved database. There are possibilities for the fraudulent access may occur. Some are students may make use of other students ID to ensure their presence when the particular student is absent or they even try to misuse it sometimes.

- Iris Based Recognition System: - In the Iris based student attendance system, the student needs to stand in front of a camera, so that the camera will scan the Iris of the student. The scanned iris is matched with data of student stored in the database and the attendance on their presence needs be updated. This reduces the paper and pen workload of the faculty member of the institute. This also reduces the chances of proxies in the class, and helps in maintaining the student records safe. It is a wireless biometric technique that solves the problem of spurious attendance and the trouble of laying the corresponding network. But it can’t use a regular camera, it requires IR light source and sensor. Visible light must be minimized for highest accuracy required for search. Generally, require close proximity to camera, which can cause discomfort for some.

## Technologies Used
- Python 3.10.6
- OpenCV 4.6.0.66
- Numpy 1.23.1
- Pillow 9.2.0
- customtkinter 4.5.10
- Pycharm(Community version) 2022.2

## How to use?
```bash
git clone https://github.com/D-ENCODER/ATTENDANCE-WITH-FACE-RECOGNITION.git
cd ATTENDANCE-WITH-FACE-RECOGNITION
pip install -r requirements.txt
python3 main.py
```

## Special Thanks To The Team
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr><b>Project led by<br></b></tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://het-joshi.web.app/"><img src="https://avatars.githubusercontent.com/u/86153190?v=4?s=100" width="100px;" alt="Het Joshi"/><br /><sub><b>Het Joshi</b></sub></a><br /><a href="https://github.com/D-ENCODER/KONGKNITEC/commits?author=D-ENCODER" title="Code">💻</a> <a href="#research-D-ENCODER" title="Research">🔬</a> <a href="#projectManagement-D-ENCODER" title="Project Management">📆</a> <a href="#ideas-D-ENCODER" title="Ideas, Planning, & Feedback">🤔</a></td></tr></tbody></table>
      <table>
  <tbody>
    <tr><b>Assisted by<br></b></tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Maulikatgit"><img src="https://avatars.githubusercontent.com/u/109577079?v=4?s=100" width="100px;" alt="Maulik Parmar"/><br /><sub><b>Maulik Parmar</b></sub></a><br /> <a href="#data-Maulikatgit" title="Data">🔣</a> <a href="https://github.com/D-ENCODER/KONGKNITEC/commits?author=Maulikatgit" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/saket0x07"><img src="https://avatars.githubusercontent.com/u/109578300?v=4?s=100" width="100px;" alt="saket0x07"/><br /><sub><b>saket0x07</b></sub></a><br /><a href="#design-saket0x07" title="Design">🎨</a> <a href="#ideas-saket0x07" title="Ideas, Planning, & Feedback">🤔</a> <a href="#content-saket0x07" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ShreyBParmar"><img src="https://avatars.githubusercontent.com/u/103874657?v=4?s=100" width="100px;" alt="ShreyBParmar"/><br /><sub><b>ShreyBParmar</b></sub></a><br /><a href="https://github.com/D-ENCODER/KONGKNITEC/commits?author=ShreyBParmar" title="Documentation">📖</a> <a href="#design-ShreyBParmar" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/SAHIL-099"><img src="https://avatars.githubusercontent.com/u/103878012?v=4?s=100" width="100px;" alt="SAHIL-099"/><br /><sub><b>SAHIL-099</b></sub></a><br /><a href="https://github.com/D-ENCODER/KONGKNITEC/commits?author=SAHIL-099" title="Code">💻</a> <a href="https://github.com/D-ENCODER/KONGKNITEC/issues?q=author%3ASAHIL-099" title="Bug reports">🐛</a> <a href="https://github.com/D-ENCODER/KONGKNITEC/commits?author=SAHIL-099" title="Tests">⚠️</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Khushi02Donga"><img src="https://avatars.githubusercontent.com/u/109589042?v=4?s=100" width="100px;" alt="Khushi Donga "/><br /><sub><b>Khushi Donga </b></sub></a><br /><a href="#design-Khushi02Donga" title="Design">🎨</a> <a href="#ideas-Khushi02Donga" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/D-ENCODER/KONGKNITEC/commits?author=Khushi02Donga" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->
