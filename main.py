from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from attendance import Attendance
import os
from train import Train
from face_recognition import Face_Recognition
from tkinter import messagebox 

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition_system")

        # IMG1
        img = Image.open(r"C:\Users\Saif Shaikh\Downloads\New folder (2)\images\side.jpg")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        # IMG2
        img1 = Image.open(r"C:\Users\Saif Shaikh\Downloads\New folder (2)\images\face.jpeg")
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # IMG3
        img2 = Image.open(r"C:\Users\Saif Shaikh\Downloads\New folder (2)\images\side.jpg")
        img2 = img2.resize((550, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        img3 = Image.open(r"C:\Users\Saif Shaikh\Downloads\New folder (2)\images\bg.jpg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDENCE SYSTEM ", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Student button
        img4 = Image.open(r"C:\Users\Saif Shaikh\Downloads\New folder (2)\images\emp img.jpg")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg4, command=self.employee_info, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.employee_info, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Face Detector
        img5 = Image.open(r"C:\Users\Saif Shaikh\Downloads\New folder (2)\images\face detect.jpg")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)  # Changed variable name to b2
        b2.place(x=500, y=100, width=220, height=220)

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)

        # Attendence
        img6 = Image.open(r"C:\Users\Saif Shaikh\Downloads\New folder (2)\images\Attendence.jpg")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b3.place(x=800, y=100, width=220, height=220)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=800, y=300, width=220, height=40)

        # Photos
        img7 = Image.open(r"C:\Users\Saif Shaikh\Downloads\New folder (2)\images\emp.jpg")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.open_img)
        b4.place(x=1100, y=100, width=220, height=220)

        b4_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=1100, y=300, width=220, height=40)

        # Train data
        img8 = Image.open(r"C:\Users\Saif Shaikh\Downloads\New folder (2)\images\train.jpeg")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b5.place(x=500, y=380, width=220, height=220)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=500, y=580, width=220, height=40)

        # Exit
        img9 = Image.open(r"C:\Users\Saif Shaikh\Downloads\New folder (2)\images\Exit.jpg")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.iExit)
        b6.place(x=800, y=380, width=220, height=220)

        b6_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=800, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("Data")

    def employee_info(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def iExit(self):
        iExit = messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root)
        if iExit > 0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()