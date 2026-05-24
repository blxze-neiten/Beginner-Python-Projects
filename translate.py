import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

# =========================
# TRANSLATE FUNCTION
# =========================

def translate_text():

    text_de_tradus = input_text.get("1.0", tk.END).strip()
    limba_destinatie = limba_destinatie_var.get()

    # Check if text box is empty
    if text_de_tradus == "":
        messagebox.showwarning(
            "Input Error",
            "Please enter text to translate!"
        )
        return

    try:

        translator = Translator()

        # Translate text
        translated = translator.translate(
            text_de_tradus,
            dest=languages[limba_destinatie]
        )

        # Clear old translated text
        output_text.delete("1.0", tk.END)

        # Insert translated text
        output_text.insert(
            tk.END,
            translated.text
        )

    except Exception as e:

        messagebox.showerror(
            "Translation Error",
            f"Something went wrong:\n{e}"
        )


# =========================
# CLEAR FUNCTION
# =========================

def clear_text():

    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()

root.title("🌍 Google Translate App")
root.geometry("850x650")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# =========================
# TITLE
# =========================

title_label = tk.Label(
    root,
    text="🌍 Python Translator",
    font=("Arial", 30, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title_label.pack(pady=20)

# =========================
# INPUT LABEL
# =========================

input_label = tk.Label(
    root,
    text="Enter Text",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white"
)

input_label.pack()

# =========================
# INPUT TEXT BOX
# =========================

input_text = tk.Text(
    root,
    height=8,
    width=70,
    font=("Arial", 14),
    bd=3,
    relief=tk.GROOVE
)

input_text.pack(pady=15)

# =========================
# LANGUAGES
# =========================

languages = {

    "Swahili": "sw",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Arabic": "ar",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Hindi": "hi",
    "Turkish": "tr"

}

# =========================
# LANGUAGE LABEL
# =========================

language_label = tk.Label(
    root,
    text="Choose Language",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white"
)

language_label.pack(pady=5)

# =========================
# LANGUAGE DROPDOWN
# =========================

limba_destinatie_var = tk.StringVar()

language_combo = ttk.Combobox(
    root,
    textvariable=limba_destinatie_var,
    values=list(languages.keys()),
    state="readonly",
    font=("Arial", 12),
    width=25
)

language_combo.pack(pady=10)

language_combo.current(0)

# =========================
# BUTTON FRAME
# =========================

button_frame = tk.Frame(
    root,
    bg="#1e1e1e"
)

button_frame.pack(pady=20)

# =========================
# TRANSLATE BUTTON
# =========================

translate_button = tk.Button(
    button_frame,
    text="Translate",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2",
    command=translate_text
)

translate_button.grid(row=0, column=0, padx=10)

# =========================
# CLEAR BUTTON
# =========================

clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 14, "bold"),
    bg="#f44336",
    fg="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2",
    command=clear_text
)

clear_button.grid(row=0, column=1, padx=10)

# =========================
# OUTPUT LABEL
# =========================

output_label = tk.Label(
    root,
    text="Translated Text",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white"
)

output_label.pack(pady=10)

# =========================
# OUTPUT TEXT BOX
# =========================

output_text = tk.Text(
    root,
    height=8,
    width=70,
    font=("Arial", 14),
    bd=3,
    relief=tk.GROOVE
)

output_text.pack(pady=15)

# =========================
# FOOTER
# =========================

footer = tk.Label(
    root,
    text="Powered by Python & Google Translate",
    font=("Arial", 10),
    bg="#1e1e1e",
    fg="gray"
)

footer.pack(side=tk.BOTTOM, pady=10)

# =========================
# RUN APPLICATION
# =========================

root.mainloop()