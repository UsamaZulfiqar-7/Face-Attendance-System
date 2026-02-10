Face Attendance System (Computer Vision Project)
📌 Project Overview

This project is a Face Recognition Based Attendance System built using Computer Vision. The system detects faces in real-time using a live camera, recognizes registered students, and automatically marks their attendance in an Excel file along with the current date and time.

🚀 How the System Works

Dataset Setup (Before Running the Project)

There is a folder named dataset in the project directory.

Inside this folder, create a separate folder for each student using their name (e.g., Ali, Ayesha, Usama).

Add multiple clear face images of each student inside their respective folder.

Example folder structure:

dataset/
├── Aliyan/
│   ├── img1.jpg
│   ├── img2.jpg
├── Noor/
│   ├── img1.jpg
│   ├── img2.jpg
└── Usama/
    ├── img1.jpg
    └── img2.jpg

Training the Model

The system reads images from the dataset folder and extracts facial features.

These features are stored and used later for recognition.

Live Face Detection & Recognition

When the camera starts, it detects faces in real-time.

If the detected face matches a registered student, the system recognizes the name.

Automatic Attendance Marking

Once a student is recognized, their:

Name

Date

Time
are automatically recorded in an Excel file (attendance.xlsx).

🛠️ Technologies Used

Python

OpenCV

NumPy

Face Recognition Library

Pandas

Excel for attendance storage

📁 Output File

Attendance is saved in:

attendance.xlsx

Example format:

Name	Date	Time
Aliyan	2025-02-10	09:15 AM
Usama	2025-02-10	09:17 AM
✅ Note

The dataset is not included in this repository for privacy reasons.

You must create your own dataset inside the dataset folder as described above.

👨‍💻 Developed By

[Your Name]
