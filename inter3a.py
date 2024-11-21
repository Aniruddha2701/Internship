import tkinter as tk
import random
import string
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.label = tk.Label(root, text="Enter desired password length:")
        self.label.pack(pady=10)

        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        self.use_uppercase = tk.BooleanVar()
        self.use_uppercase.set(True)
        self.uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=self.use_uppercase)
        self.uppercase_checkbox.pack(pady=5)

        self.use_numbers = tk.BooleanVar()
        self.use_numbers.set(True)
        self.numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=self.use_numbers)
        self.numbers_checkbox.pack(pady=5)

        self.use_symbols = tk.BooleanVar()
        self.use_symbols.set(True)
        self.symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=self.use_symbols)
        self.symbols_checkbox.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                self.result_label.config(text="Length must be at least 1.")
                return

            # Define the character sets to use
            lowercase = string.ascii_lowercase
            uppercase = string.ascii_uppercase
            digits = string.digits
            symbols = string.punctuation

            # Combine all character sets based on user input
            all_characters = lowercase
            if self.use_uppercase.get():
                all_characters += uppercase
            if self.use_numbers.get():
                all_characters += digits
            if self.use_symbols.get():
                all_characters += symbols

            # Generate a random password
            password = ''.join(random.choice(all_characters) for _ in range(length))
            self.result_label.config(text=f"Generated Password: {password}")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
