import string
import random
import tkinter as tk

# Function to generate password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function connected to button
def generate_password_interface():
    try:
        password_length = int(entry_length.get())

        if password_length < 6:
            result_label.config(
                text="Password length must be at least 6 characters."
            )
        else:
            generated_password = generate_password(password_length)
            result_label.config(
                text="Generated Password: " + generated_password
            )

    except ValueError:
        result_label.config(
            text="Please enter a valid number."
        )

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x200")

# Label
label_length = tk.Label(
    root,
    text="Enter desired password length:"
)
label_length.pack(pady=10)

# Entry
entry_length = tk.Entry(root)
entry_length.pack()

# Button
generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password_interface
)
generate_button.pack(pady=10)

# Result Label
result_label = tk.Label(
    root,
    text="",
    wraplength=450
)
result_label.pack(pady=10)

# Run application
root.mainloop()