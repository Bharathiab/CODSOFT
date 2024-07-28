import tkinter as tk

def click_button(value):
    current_text = display.get()
    display.set(current_text + value)

def clear_display():
    display.set("")

def calculate():
    try:
        result = eval(display.get())
        display.set(result)
    except Exception as e:
        display.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a StringVar to hold the display text
display = tk.StringVar()

# Create the display and buttons in a single box (frame)
frame = tk.Frame(root, padx=10, pady=10)
frame.grid(row=0, column=0)

# Create the display
entry = tk.Entry(frame, textvariable=display, font=('Arial', 20), bd=8, insertwidth=4, width=14, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0, 1), ('8', 1, 1, 1), ('9', 1, 2, 1), ('/', 1, 3, 1),
    ('4', 2, 0, 1), ('5', 2, 1, 1), ('6', 2, 2, 1), ('*', 2, 3, 1),
    ('1', 3, 0, 1), ('2', 3, 1, 1), ('3', 3, 2, 1), ('-', 3, 3, 1),
    ('C', 4, 0, 1), ('0', 4, 1, 1), ('.', 4, 2, 1), ('+', 4, 3, 1),
    ('=', 5, 0, 4)
]

for (text, row, column, colspan) in buttons:
    if text == '=':
        button = tk.Button(frame, text=text, padx=20, pady=20, font=('Arial', 20), command=calculate)
        button.grid(row=row, column=column, columnspan=colspan, sticky="nsew")
    elif text == 'C':
        button = tk.Button(frame, text=text, padx=20, pady=20, font=('Arial', 20), command=clear_display)
        button.grid(row=row, column=column, sticky="nsew")
    else:
        button = tk.Button(frame, text=text, padx=20, pady=20, font=('Arial', 20), command=lambda t=text: click_button(t))
        button.grid(row=row, column=column, sticky="nsew")

# Adjust column and row weights
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
    frame.grid_rowconfigure(i, weight=1)

# Start the main event loop
root.mainloop()
