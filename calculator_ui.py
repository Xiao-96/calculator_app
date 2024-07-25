# calculator_ui.py

import tkinter as tk
from calculator_logic import add, subtract

def calculate_add():
    result.set(add(entry1.get(), entry2.get()))

def calculate_subtract():
    result.set(subtract(entry1.get(), entry2.get()))

app = tk.Tk()
app.title("Calculator v1.0.0")

entry1 = tk.Entry(app)
entry1.grid(row=0, column=0, columnspan=2)

entry2 = tk.Entry(app)
entry2.grid(row=1, column=0, columnspan=2)

result = tk.StringVar()
result_label = tk.Label(app, textvariable=result)
result_label.grid(row=2, column=0, columnspan=2)

add_button = tk.Button(app, text="+", command=calculate_add)
add_button.grid(row=3, column=0)

subtract_button = tk.Button(app, text="-", command=calculate_subtract)
subtract_button.grid(row=3, column=1)

app.mainloop()