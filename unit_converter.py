import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)
from PyQt5.QtCore import Qt


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_input.text())
        fahrenheit = (celsius * 9 / 5) + 32

        result_label.setText(
            f"{celsius}°C is equivalent to {fahrenheit:.2f}°F."
        )

    except ValueError:
        result_label.setText("Please enter a valid number.")


# Create application
app = QApplication(sys.argv)

# Create main window
window = QWidget()
window.setWindowTitle("Celsius to Fahrenheit Converter")

# Create layout
layout = QVBoxLayout()

# Title label
title_label = QLabel("Temperature Converter")
title_label.setStyleSheet(
    "font-size: 18px; font-weight: bold;"
)
title_label.setAlignment(Qt.AlignCenter)
layout.addWidget(title_label)

# Input field
celsius_input = QLineEdit()
celsius_input.setPlaceholderText(
    "Enter temperature in Celsius"
)
layout.addWidget(celsius_input)

# Convert button
convert_button = QPushButton("Convert")
convert_button.clicked.connect(celsius_to_fahrenheit)
layout.addWidget(convert_button)

# Result label
result_label = QLabel("")
result_label.setAlignment(Qt.AlignCenter)
layout.addWidget(result_label)

# Align layout
layout.setAlignment(Qt.AlignCenter)

# Set layout to window
window.setLayout(layout)

# Window size and position
window.setGeometry(100, 100, 400, 200)

# Show window
window.show()

# Run application
sys.exit(app.exec_())