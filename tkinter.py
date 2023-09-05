import tkinter as tk
from tkinter import messagebox

# Function to perform Fahrenheit to Celsius conversion
def convert_temperature():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid temperature in Fahrenheit.")

# Create the main application window
app = tk.Tk()
app.title("Temperature Converter")

# Create and arrange widgets
label = tk.Label(app, text="Enter temperature in Fahrenheit:")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack()

convert_button = tk.Button(app, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack()

# Start the Tkinter event loop
app.mainloop()
