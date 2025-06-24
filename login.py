import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
import subprocess
from PIL import Image, ImageTk

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.state('zoomed')
        self.root.configure(bg="#E0F2F7") 

        user_icon = Image.open("images\gemi.png")
        user_icon = user_icon.resize((80, 80))
        self.user_icon_img = ImageTk.PhotoImage(user_icon)

        self.user_icon_label = tk.Label(root, image=self.user_icon_img, bg="#E0F2F7")
        self.user_icon_label.pack(pady=20)

        self.username_label = tk.Label(root, text="Username", bg="#E0F2F7", font=("Arial", 12))
        self.username_label.pack()
        self.username_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(root, text="Password", bg="#E0F2F7", font=("Arial", 12))
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
        self.password_entry.pack(pady=5)

        self.remember_var = tk.IntVar()
        self.remember_check = tk.Checkbutton(root, text="Remember me", variable=self.remember_var, bg="#E0F2F7")
        self.remember_check.pack(side="left", padx=20)

        self.forgot_pass_link = tk.Label(root, text="Forgot password?", bg="#E0F2F7", fg="blue", cursor="hand2")
        self.forgot_pass_link.pack(side="right", padx=20)
        self.forgot_pass_link.bind("<Button-1>", lambda e: self.forgot_password())

        self.login_button = tk.Button(root, text="LOGIN", bg="#1976D2", fg="white", font=("Arial", 14), width=20, command=self.login)
        self.login_button.pack(pady=20)

        self.register_button = tk.Button(root, text="Register", bg="#1976D2", fg="white", font=("Arial", 12), command=self.register)
        self.register_button.pack(pady=10)

        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """)
        self.conn.commit()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        hashed_password = self.hash_password(password)

        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        user = self.cursor.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()
            self.open_main_program()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def register(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Register")
        register_window.state('zoomed')
        register_window.configure(bg="#E0F2F7")

        username_label = tk.Label(register_window, text="Username:", bg="#E0F2F7")
        username_label.pack()
        username_entry = tk.Entry(register_window)
        username_entry.pack()

        password_label = tk.Label(register_window, text="Password:", bg="#E0F2F7")
        password_label.pack()
        password_entry = tk.Entry(register_window, show="*")
        password_entry.pack()

        def register_user():
            username = username_entry.get()
            password = password_entry.get()
            hashed_password = self.hash_password(password)

            try:
                self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
                self.conn.commit()
                messagebox.showinfo("Success", "Registration successful!")
                register_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists.")

        register_button = tk.Button(register_window, text="Register", command=register_user)
        register_button.pack()

    def forgot_password(self):
        forgot_window = tk.Toplevel(self.root)
        forgot_window.title("Forgot Password")
        forgot_window.state('zoomed')
        forgot_window.configure(bg="#E0F2F7")

        username_label = tk.Label(forgot_window, text="Username:", bg="#E0F2F7")
        username_label.pack()
        username_entry = tk.Entry(forgot_window)
        username_entry.pack()

        new_password_label = tk.Label(forgot_window, text="New Password:", bg="#E0F2F7")
        new_password_label.pack()
        new_password_entry = tk.Entry(forgot_window, show="*")
        new_password_entry.pack()

        def reset_password():
            username = username_entry.get()
            new_password = new_password_entry.get()
            hashed_password = self.hash_password(new_password)

            self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            user = self.cursor.fetchone()

            if user:
                self.cursor.execute("UPDATE users SET password=? WHERE username=?", (hashed_password, username))
                self.conn.commit()
                messagebox.showinfo("Success", "Password reset successful!")
                forgot_window.destroy()
            else:
                messagebox.showerror("Error", "Username not found.")

        reset_button = tk.Button(forgot_window, text="Reset Password", command=reset_password)
        reset_button.pack()

    def open_main_program(self):
        try:
            subprocess.Popen(["python", "main.py"])
        except FileNotFoundError:
            messagebox.showerror("Error", "main.py not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginSystem(root)
    root.mainloop()