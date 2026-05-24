import tkinter as tk
import time

# Update clock function
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y")

    clock_label.config(text=current_time)
    date_label.config(text=current_date)

    app.after(1000, update_clock)

# Main window
app = tk.Tk()
app.title("Ultimate Digital Clock")
app.geometry("900x400")
app.configure(bg="black")

# Make window fullscreen optional
# app.attributes("-fullscreen", True)

# Title
title_label = tk.Label(
    app,
    text="DIGITAL CLOCK",
    font=("Helvetica", 24, "bold"),
    fg="cyan",
    bg="black"
)
title_label.pack(pady=10)

# Clock display
clock_label = tk.Label(
    app,
    font=("Helvetica", 80, "bold"),
    fg="lime",
    bg="black"
)
clock_label.pack(pady=20)

# Date display
date_label = tk.Label(
    app,
    font=("Helvetica", 24),
    fg="white",
    bg="black"
)
date_label.pack(pady=10)

# Footer
footer_label = tk.Label(
    app,
    text="Python Tkinter Live Clock",
    font=("Helvetica", 14),
    fg="gray",
    bg="black"
)
footer_label.pack(side="bottom", pady=10)

# Start updating
update_clock()

# Run app
app.mainloop()