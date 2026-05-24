from tkinter import *
import datetime
import threading
import time
import winsound


# Alarm function
def alarm(set_alarm_timer):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        if current_time == set_alarm_timer:
            result_label.config(text="⏰ Time to Wake Up!")

            # Beep sound
            for i in range(5):
                winsound.Beep(1000, 1000)

            break

        time.sleep(1)


# Function called by button
def actual_time():
    set_alarm_timer = f"{hour.get()}:{minute.get()}:{second.get()}"

    result_label.config(
        text=f"Alarm set for {set_alarm_timer}"
    )

    # Run alarm in separate thread
    alarm_thread = threading.Thread(
        target=alarm,
        args=(set_alarm_timer,)
    )

    alarm_thread.daemon = True
    alarm_thread.start()


# Main window
clock = Tk()
clock.title("PYANDREI Alarm Clock")
clock.geometry("400x250")
clock.resizable(False, False)

# Title
title_label = Label(
    clock,
    text="Alarm Clock",
    font=("Arial", 18, "bold"),
    fg="blue"
)
title_label.pack(pady=10)

# Instructions
time_format = Label(
    clock,
    text="Enter time in 24-hour format (HH:MM:SS)",
    fg="red"
)
time_format.pack()

# Frame for inputs
frame = Frame(clock)
frame.pack(pady=10)

# Variables
hour = StringVar()
minute = StringVar()
second = StringVar()

# Hour input
hour_entry = Entry(
    frame,
    textvariable=hour,
    width=5,
    font=("Arial", 14),
    justify="center"
)
hour_entry.grid(row=0, column=0, padx=5)

# Minute input
minute_entry = Entry(
    frame,
    textvariable=minute,
    width=5,
    font=("Arial", 14),
    justify="center"
)
minute_entry.grid(row=0, column=1, padx=5)

# Second input
second_entry = Entry(
    frame,
    textvariable=second,
    width=5,
    font=("Arial", 14),
    justify="center"
)
second_entry.grid(row=0, column=2, padx=5)

# Labels
Label(frame, text="Hour").grid(row=1, column=0)
Label(frame, text="Min").grid(row=1, column=1)
Label(frame, text="Sec").grid(row=1, column=2)

# Button
submit = Button(
    clock,
    text="Set Alarm",
    fg="white",
    bg="green",
    width=15,
    command=actual_time
)
submit.pack(pady=15)

# Result label
result_label = Label(
    clock,
    text="",
    font=("Arial", 12)
)
result_label.pack()

# Run app
clock.mainloop()