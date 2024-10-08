import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.geometry("400x400")  # Increased the height to 400

        # Create input fields
        tk.Label(master, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=5)

        tk.Label(master, text="Platform").pack(pady=5)
        self.platform_entry = tk.Entry(master)
        self.platform_entry.pack(pady=5)

        tk.Label(master, text="Password Strength").pack(pady=5)
        self.password_strength_var = tk.StringVar(value="easy")
        tk.Radiobutton(master, text="Easy", variable=self.password_strength_var, value="easy").pack()
        tk.Radiobutton(master, text="Moderate", variable=self.password_strength_var, value="moderate").pack()
        tk.Radiobutton(master, text="Strong", variable=self.password_strength_var, value="strong").pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_preview_label = tk.Label(master, text="", font=('Helvetica', 12))
        self.password_preview_label.pack(pady=5)

        self.save_button = tk.Button(master, text="Save Entry", command=self.save_entry)
        self.save_button.pack(pady=10)  # Increased padding to give more space

    def generate_password(self):
        strength = self.password_strength_var.get()
        length = 0
        
        if strength == "easy":
            length = 8
            chars = string.ascii_lowercase
        elif strength == "moderate":
            length = 12
            chars = string.ascii_letters + string.digits
        elif strength == "strong":
            length = 16
            chars = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_preview_label.config(text=f"Generated Password: {password}")

        # Store the password for saving
        self.generated_password = password

    def save_entry(self):
        username = self.username_entry.get()
        platform = self.platform_entry.get()
        
        if not username or not platform:
            messagebox.showerror("Input Error", "Please fill in all fields")
            return

        # Use the previously generated password
        if hasattr(self, 'generated_password'):
            password = self.generated_password
        else:
            messagebox.showerror("Error", "No password generated to save.")
            return

        with open("passwords.txt", "a") as file:
            file.write(f"{platform} | {username} | {password}\n")

        messagebox.showinfo("Success", f"Details saved for {platform}!")
        self.username_entry.delete(0, tk.END)
        self.platform_entry.delete(0, tk.END)
        self.password_preview_label.config(text="")  # Clear the password preview


if __name__ == "__main__":
    root = tk.Tk()
    password_manager = PasswordManager(root)
    root.mainloop()
