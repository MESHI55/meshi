
import tkinter as tk
from tkinter import ttk

# Conversion functions and data
conversion_map = {
    "Miles": {"Kilometers": lambda x: x * 1.60934},
    "Kilometers": {"Miles": lambda x: x / 1.60934},
    "Pounds": {"Kilograms": lambda x: x * 0.453592},
    "Kilograms": {"Pounds": lambda x: x / 0.453592},
    "Inches": {"Centimeters": lambda x: x * 2.54},
    "Centimeters": {"Inches": lambda x: x / 2.54},
    "Fahrenheit": {"Celsius": lambda x: (x - 32) * 5/9},
    "Celsius": {"Fahrenheit": lambda x: (x * 9/5) + 32},
}


def update_to_units(event):
    """Update the 'to' unit dropdown based on the selected 'from' unit."""
    selected_unit = unit_from_var.get()
    if selected_unit in conversion_map:
        combo_to["values"] = list(conversion_map[selected_unit].keys())
        combo_to.set("")
    else:
        combo_to["values"] = []
        combo_to.set("")


def convert():
    unit_from = unit_from_var.get()
    unit_to = unit_to_var.get()
    try:
        value = float(entry_value.get())
    except ValueError:
        label_result.config(text="Invalid input. Please enter a number.")
        return

    if unit_from in conversion_map and unit_to in conversion_map[unit_from]:
        result = conversion_map[unit_from][unit_to](value)
        label_result.config(
            text=f"{value} {unit_from} = {result:.2f} {unit_to}")
    else:
        label_result.config(text="Invalid conversion")


# Create the main window
root = tk.Tk()
root.title("Converter")
root.geometry("400x400")
root.configure(bg="#FF0000")

# Input value
label_value = ttk.Label(root, text="Value:",foreground="blue",background="#FF0000")
label_value.pack(pady=5)
entry_value = ttk.Entry(root, font=("Arial", 14))
entry_value.pack(pady=5)

# Dropdown for "from" unit
label_from = ttk.Label(root, text="Convert from:",foreground="blue",background="#FF0000")
label_from.pack(pady=5)
unit_from_var = tk.StringVar()
combo_from = ttk.Combobox(root, textvariable=unit_from_var, font=("Arial", 14))
combo_from["values"] = list(conversion_map.keys())
combo_from.bind("<<ComboboxSelected>>", update_to_units)
combo_from.pack(pady=5)

# Dropdown for "to" unit
label_to = ttk.Label(root, text="Convert to:",foreground="blue",background="#FF0000")
label_to.pack(pady=5)
unit_to_var = tk.StringVar()
combo_to = ttk.Combobox(root, textvariable=unit_to_var, font=("Arial", 14))
combo_to.pack(pady=5)

# Convert button
button_convert = ttk.Button(
    root, text="Convert", command=convert, style="TButton")
button_convert.pack(pady=10)

# Result label
label_result = ttk.Label(root, text="", font=(
    "Arial", 14), background="#FF0000", foreground="#333")
label_result.pack(pady=20)

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.map("TButton",
          background=[("active", "#0056b3"), ("!active", "#007bff")],
          foreground=[("active", "blue"), ("!active", "blue")])

# Start the Tkinter event loop
root.mainloop()