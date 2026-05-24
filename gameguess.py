import random
import tkinter as tk
from tkinter import messagebox

# =========================
# FUNCTIONS
# =========================

def new_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    output_label.config(
        text="🎯 Guess a number between 1 and 100!",
        fg="#333333"
    )

    attempts_label.config(
        text="Attempts: 0",
        fg="black"
    )

    entry_guess.config(state="normal")
    entry_guess.delete(0, tk.END)

    submit_button.config(state="normal")


def check_guess():
    global attempts

    guess_text = entry_guess.get()

    # Check if input is empty
    if guess_text == "":
        messagebox.showwarning("Input Error", "Please enter a number!")
        return

    # Check if input is a valid number
    try:
        guess = int(guess_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Only numbers are allowed!")
        return

    # Check range
    if guess < 1 or guess > 100:
        messagebox.showwarning(
            "Out of Range",
            "Enter a number between 1 and 100!"
        )
        return

    attempts += 1

    attempts_label.config(
        text=f"Attempts: {attempts}"
    )

    # Compare guess
    if guess < secret_number:
        output_label.config(
            text="📉 Too low! Try again.",
            fg="blue"
        )

    elif guess > secret_number:
        output_label.config(
            text="📈 Too high! Try again.",
            fg="orange"
        )

    else:
        output_label.config(
            text=f"🎉 Correct! The number was {secret_number}",
            fg="green"
        )

        attempts_label.config(
            text=f"You guessed it in {attempts} attempts!",
            fg="green"
        )

        submit_button.config(state="disabled")
        entry_guess.config(state="disabled")


# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()
root.title("🎮 Number Guessing Game")
root.geometry("500x400")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# =========================
# GAME VARIABLES
# =========================

secret_number = 0
attempts = 0

# =========================
# TITLE
# =========================

title_label = tk.Label(
    root,
    text="🎯 Guess The Number",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title_label.pack(pady=20)

# =========================
# INSTRUCTIONS
# =========================

output_label = tk.Label(
    root,
    text="Guess a number between 1 and 100!",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="#dddddd"
)

output_label.pack(pady=10)

# =========================
# ENTRY BOX
# =========================

entry_guess = tk.Entry(
    root,
    font=("Arial", 18),
    justify="center",
    width=10,
    bd=3
)

entry_guess.pack(pady=15)

# =========================
# BUTTONS
# =========================

submit_button = tk.Button(
    root,
    text="Submit Guess",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=15,
    pady=8,
    command=check_guess
)

submit_button.pack(pady=10)

new_game_button = tk.Button(
    root,
    text="New Game",
    font=("Arial", 12, "bold"),
    bg="#2196F3",
    fg="white",
    padx=15,
    pady=8,
    command=new_game
)

new_game_button.pack(pady=10)

# =========================
# ATTEMPTS LABEL
# =========================

attempts_label = tk.Label(
    root,
    text="Attempts: 0",
    font=("Arial", 13),
    bg="#1e1e1e",
    fg="white"
)

attempts_label.pack(pady=15)

# =========================
# START GAME
# =========================

new_game()

# =========================
# RUN PROGRAM
# =========================

root.mainloop()