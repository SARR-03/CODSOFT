import tkinter as tk
import random
import string


class RegistrationFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")

        self.first_name_label = tk.Label(root, text="First Name:", font=("Arial", 12))
        self.first_name_label.pack(pady=10)

        self.first_name_entry = tk.Entry(root, font=("Arial", 12))
        self.first_name_entry.pack(pady=10)

        self.last_name_label = tk.Label(root, text="Last Name:", font=("Arial", 12))
        self.last_name_label.pack(pady=10)

        self.last_name_entry = tk.Entry(root, font=("Arial", 12))
        self.last_name_entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12),
                                         command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(root, text="Generated Password:", font=("Arial", 12))
        self.password_label.pack(pady=5)

        self.password_display = tk.Label(root, text="", font=("Arial", 12))
        self.password_display.pack(pady=5)

        self.register_button = tk.Button(root, text="Register", font=("Arial", 12), command=self.register)
        self.register_button.pack(pady=10)

    def generate_password(self):
        password = self.generate_random_password()
        self.password_display.config(text=password)

    def generate_random_password(self, length=10):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def register(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        password = self.password_display.cget("text")

        if first_name and last_name and password:
            with open("user_data.txt", "a") as file:
                file.write(f"First Name: {first_name}\n")
                file.write(f"Last Name: {last_name}\n")
                file.write(f"Password: {password}\n\n")
            self.clear_fields()
        else:
            tk.messagebox.showwarning("Warning", "Please fill in all fields.")

    def clear_fields(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.password_display.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationFormApp(root)
    root.mainloop()
