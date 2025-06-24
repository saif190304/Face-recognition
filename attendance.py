from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition_system")

        # 1st img
        img = Image.open(r"images\face 111111.jpg")
        img = img.resize((800, 200))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # IMG2
        img1 = Image.open(r"images\face222.jpg")
        img1 = img1.resize((800, 200))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        # bg
        img3 = Image.open(r"images\bg.jpg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=5, y=55, width=1500, height=600)

        # left lable
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance  Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)

        img_left = Image.open(r"images\emp3.jpg")
        img_left = img_left.resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=180, width=750, height=370)

        # label &entry
        attendanceId_label = Label(left_inside_frame, text="Attendance Id :", font=("times new roman", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.attendanceID_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        self.attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll
        rollLabel = Label(left_inside_frame, text="Roll :", font=("times new roman", 13, "bold"), bg="white")
        rollLabel.grid(row=0, column=2, padx=4, pady=8, sticky=W)

        self.atten_roll = ttk.Entry(left_inside_frame, width=22, font=("times new roman", 13, "bold"))
        self.atten_roll.grid(row=0, column=3, padx=8, sticky=W)

        # Name
        nameLabel = Label(left_inside_frame, text="Name :", font=("times new roman", 13, "bold"), bg="white")
        nameLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        self.name_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        self.name_entry.grid(row=1, column=1, padx=8, sticky=W)

        # Department
        depLabel = Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"), bg="white")
        depLabel.grid(row=1, column=2)

        self.atten_dep = ttk.Entry(left_inside_frame, width=22, font=("times new roman", 13, "bold"))
        self.atten_dep.grid(row=1, column=3, pady=8, sticky=W)

        # time
        timeLabel = Label(left_inside_frame, text="Time :", font=("times new roman", 13, "bold"), bg="white")
        timeLabel.grid(row=2, column=0)

        self.atten_time = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        self.atten_time.grid(row=2, column=1, pady=8, sticky=W)

        # date
        dateLabel = Label(left_inside_frame, text="Date :", font=("times new roman", 13, "bold"), bg="white")
        dateLabel.grid(row=2, column=2)

        self.atten_date = ttk.Entry(left_inside_frame, width=22, font=("times new roman", 13, "bold"))
        self.atten_date.grid(row=2, column=3, pady=8)

        # attendance
        attendanceLabel = Label(left_inside_frame, text="Attendance Status :", font=("times new roman", 13, "bold"), bg="white")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame, width=20, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)
        # Button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=35)
        # save
        save_btn = Button(btn_frame, text="Import CSV", command=self.importCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, )
        # export
        export_btn = Button(btn_frame, text="Export CSV", command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1, )
        # update
        update_btn = Button(btn_frame, text="Update", command=self.updateData, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2, )
        # reset
        reset_btn = Button(btn_frame, text="Reset", command=self.resetData, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, )

        # right label
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=780, y=10, width=690, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=670, height=455)

        # scroll bar & table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        # Bind double-click event to the Treeview for selecting data
        self.AttendanceReportTable.bind("<Double-1>", self.on_treeview_select)

    # fetch data
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        filetypes = (("CSV File", "*.csv"), ("All File", "*.*"))
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=filetypes, parent=self.root)
        try:
            with open(fln) as myfile:
                csvread = csv.reader(myfile)
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data to export", parent=self.root)
                return
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), defaultextension=".csv")
            with open(fln, mode="w", newline="") as myfile:
                csvwrite = csv.writer(myfile)
                for i in mydata:
                    csvwrite.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def on_treeview_select(self, event):
        item = self.AttendanceReportTable.selection()
        if item:
            record = self.AttendanceReportTable.item(item, 'values')
            self.attendanceID_entry.delete(0, END)
            self.attendanceID_entry.insert(END, record[0])
            self.atten_roll.delete(0, END)
            self.atten_roll.insert(END, record[1])
            self.name_entry.delete(0, END)
            self.name_entry.insert(END, record[2])
            self.atten_dep.delete(0, END)
            self.atten_dep.insert(END, record[3])
            self.atten_time.delete(0, END)
            self.atten_time.insert(END, record[4])
            self.atten_date.delete(0, END)
            self.atten_date.insert(END, record[5])
            self.atten_status.set(record[6])

    def updateData(self):
        selected = self.AttendanceReportTable.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a record to update.", parent=self.root)
            return

        try:
            index = self.AttendanceReportTable.index(selected)
            mydata[index] = [
                self.attendanceID_entry.get(),
                self.atten_roll.get(),
                self.name_entry.get(),
                self.atten_dep.get(),
                self.atten_time.get(),
                self.atten_date.get(),
                self.atten_status.get()
            ]
            self.fetchData(mydata)
            messagebox.showinfo("Success", "Record updated successfully.", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def resetData(self):
        self.attendanceID_entry.delete(0, END)
        self.atten_roll.delete(0, END)
        self.name_entry.delete(0, END)
        self.atten_dep.delete(0, END)
        self.atten_time.delete(0, END)
        self.atten_date.delete(0, END)
        self.atten_status.set("Status")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()