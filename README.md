🎯 Face Attendance System (Computer Vision)






📌 About the Project

This is a Face Recognition Based Attendance System developed using Computer Vision and Python.
The system:

Detects faces using a live camera

Recognizes registered students from a local dataset

Automatically marks attendance in an Excel file

Saves Name, Date, and Time of each recognized student

🚫 No dataset is included in this repository for privacy reasons. You must add your own images.

📂 Dataset Structure

A folder named datasets already exists in the project. Inside it, you need to create separate folders for each student and add their images.

Required structure:
datasets/
│
├── Aliyan/
│   ├── img1.jpg
│   ├── img2.jpg
│
├── Noor/
│   ├── img1.jpg
│   ├── img2.jpg
│
└── Usama/
    ├── img1.jpg
    └── img2.jpg

👉 Each folder name must be the student's exact name, as this name will be used in the attendance file.

⚙️ How It Works

1️⃣ The system loads images from the datasets folder
2️⃣ Extracts face features of each student
3️⃣ Turns on the live camera
4️⃣ Detects and recognizes faces in real time
5️⃣ If matched, attendance is automatically marked

📊 Attendance Output

Attendance is saved in an Excel file:

attendance.xlsx

Example format:

Name	Date	Time
Aliyan	2025-02-10	09:15 AM
Noor	2025-02-10	09:17 AM
Usama	2025-02-10	09:20 AM
🛠️ Technologies Used

Python

OpenCV

NumPy

face_recognition library

Pandas

Excel

🚀 How to Run

Install dependencies:

pip install opencv-python numpy pandas face-recognition

Add student images inside:

datasets/

Run the main file:

python attendance.py

Camera will open and start marking attendance automatically.

👨‍💻 Developed By

Rana Usama
