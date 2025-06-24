from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np
import csv

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition_system")

        title_lbl = Label(self.root, text="FACE RECOGNITION ", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"images\face detect.jpg")
        img_top = img_top.resize((650, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open(r"images\gemi.png")
        img_bottom = img_bottom.resize((950, 700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        b4_1 = Button(f_lbl, text="Face Recognize", cursor="hand2", font=("times new roman", 18, "bold"), bg="white", fg="blue", command=self.face_recog)
        b4_1.place(x=380, y=600, width=200, height=40)

        self.marked_attendance = set() # Store already marked IDs

    def mark_attendance(self, i, r, n, d):
        if i not in self.marked_attendance:
            try:
                with open("attendence.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    dtString = now.strftime("%H:%M:%S")
                    writer.writerow([i, r, n, d, dtString, d1, "Present"])
                    self.marked_attendance.add(i) # Add ID to marked set
            except Exception as e:
                print(f"Error marking attendance: {e}")
        else:
            print(f"Attendance already marked for ID: {i}")

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 225, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Saif@123", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where `Student Id`=" + str(id))
                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown"

                my_cursor.execute("select Roll from student where `Student Id`=" + str(id))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"

                my_cursor.execute("select Dep from student where `Student Id`=" + str(id))
                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"

                i = str(id)

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To face recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()