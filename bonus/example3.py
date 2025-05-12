import tkinter as tk
from tkinter import ttk

def convert_to_meters():
    try:
        feet = float(feet_entry.get())
        inches = float(inches_entry.get())
        total_inches = feet * 12 + inches
        meters = total_inches * 0.0254
        result_label.config(text=f"{meters:.3f} m")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Feet and Inches to Meters Converter")
root.geometry("300x200")

# Create and place widgets
tk.Label(root, text="Enter feet:").pack(pady=5)
feet_entry = ttk.Entry(root)
feet_entry.pack(pady=5)

tk.Label(root, text="Enter inches:").pack(pady=5)
inches_entry = ttk.Entry(root)
inches_entry.pack(pady=5)

convert_button = ttk.Button(root, text="Convert", command=convert_to_meters)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()