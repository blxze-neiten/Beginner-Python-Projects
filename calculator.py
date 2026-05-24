import tkinter as tk
import math

# Function to calculate operations
def calculate(operation):
    try:
        num1 = float(entry1.get())

        # Operations needing two numbers
        if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
            num2 = float(entry2.get())

        if operation == "Add":
            result = num1 + num2

        elif operation == "Subtract":
            result = num1 - num2

        elif operation == "Multiply":
            result = num1 * num2

        elif operation == "Divide":
            if num2 == 0:
                result = "Cannot divide by zero!"
            else:
                result = num1 / num2

        elif operation == "Square Root":
            if num1 < 0:
                result = "Invalid input for square root!"
            else:
                result = math.sqrt(num1)

        elif operation == "Power":
            result = num1 ** num2

        elif operation == "Logarithm":
            if num1 <= 0:
                result = "Log undefined!"
            else:
                result = math.log(num1)

        else:
            result = "Invalid operation!"

        result_label.config(text="Result: " + str(result))

    except ValueError:
        result_label.config(text="Invalid input!")

# Main window
root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("350x400")
root.config(bg="lightblue")

# Labels
label1 = tk.Label(root, text="Enter First Number:", bg="lightblue")
label1.grid(row=0, column=0, padx=5, pady=5)

label2 = tk.Label(root, text="Enter Second Number:", bg="lightblue")
label2.grid(row=1, column=0, padx=5, pady=5)

# Entry boxes
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Operations list
operations = [
    "Add",
    "Subtract",
    "Multiply",
    "Divide",
    "Square Root",
    "Power",
    "Logarithm"
]

# Buttons
row_val = 2

for operation in operations:
    operation_button = tk.Button(
        root,
        text=operation,
        width=20,
        bg="white",
        command=lambda op=operation: calculate(op)
    )

    operation_button.grid(row=row_val, column=0, columnspan=2, padx=5, pady=5)
    row_val += 1

# Result label
result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 12, "bold"),
    bg="lightblue"
)

result_label.grid(row=row_val, column=0, columnspan=2, pady=10)

# Run app
root.mainloop()