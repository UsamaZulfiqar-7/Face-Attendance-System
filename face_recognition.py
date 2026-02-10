# face_recognition.py
import cv2
import os
import numpy as np
from mtcnn.mtcnn import MTCNN
from keras_facenet import FaceNet
from scipy.spatial.distance import cosine
from datetime import datetime

# ============================
# INITIALIZE
# ============================
detector = MTCNN()
embedder = FaceNet()

dataset_path = "dataset"
embeddings_db = {}
attendance_marked = []

THRESHOLD = 0.45

# ============================
# LOAD DATASET & CREATE EMBEDDINGS
# ============================
for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)
    if not os.path.isdir(person_path):
        continue

    person_embeddings = []

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        img = cv2.imread(img_path)

        if img is None:
            continue

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faces = detector.detect_faces(rgb)

        if len(faces) == 0:
            continue

        x, y, w, h = faces[0]['box']
        face = rgb[y:y+h, x:x+w]
        face = cv2.resize(face, (160, 160))

        embedding = embedder.embeddings([face])[0]
        person_embeddings.append(embedding)

    if person_embeddings:
        embeddings_db[person] = np.mean(person_embeddings, axis=0)

print("✅ Dataset Loaded Successfully")

# ============================
# FACE RECOGNITION FUNCTION
# ============================
def recognize_face(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = detector.detect_faces(rgb_frame)
    results = []

    for face_data in faces:
        x, y, w, h = face_data['box']
        face_img = rgb_frame[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (160, 160))

        face_embedding = embedder.embeddings([face_img])[0]

        name = "UNKNOWN"
        status = ""
        min_dist = 1.0

        for person, db_embedding in embeddings_db.items():
            dist = cosine(face_embedding, db_embedding)
            if dist < min_dist:
                min_dist = dist
                name = person

        if min_dist > THRESHOLD:
            name = "UNKNOWN"
        else:
            status = "PRESENT"
            if name not in attendance_marked:
                attendance_marked.append(name)
                with open("attendance.csv", "a") as f:
                    f.write(f"{name},{datetime.now().strftime('%H:%M:%S')}\n")

        results.append({"name": name, "status": status, "box": [x, y, w, h]})

    return results
