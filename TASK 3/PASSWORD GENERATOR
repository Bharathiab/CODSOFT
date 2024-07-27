import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    length = int(entry_length.get())
    use_special_chars = var_special.get()
    
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

var_special = tk.BooleanVar()
check_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special)
check_special.pack(pady=5)

btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate.pack(pady=5)

entry_password = tk.Entry(root, width=50)
entry_password.pack(pady=5)

# Start the main event loop
root.mainloop()
