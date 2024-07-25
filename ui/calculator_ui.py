# calculator_ui.py

import tkinter as tk
from logic.calculator_logic import add, subtract
from logic.calculator_plus import multiply, divide

def calculate_add():
    result.set(add(entry1.get(), entry2.get()))

def calculate_subtract():
    result.set(subtract(entry1.get(), entry2.get()))

def calculate_multiply():
    result.set(multiply(entry1.get(), entry2.get()))

def calculate_divide():
    result.set(divide(entry1.get(), entry2.get()))

def on_digit_button_click(digit):
    current = entry1.get()
    entry1.delete(0, tk.END)
    entry1.insert(0, current + str(digit))

def run():
    global entry1, entry2, result  # 声明为全局变量
    app = tk.Tk()
    app.title("Calculator v1.0.2")

    entry1 = tk.Entry(app)
    entry1.grid(row=0, column=0, columnspan=4)

    entry2 = tk.Entry(app)
    entry2.grid(row=1, column=0, columnspan=4)

    result = tk.StringVar()
    result_label = tk.Label(app, textvariable=result)
    result_label.grid(row=2, column=0, columnspan=4)

    add_button = tk.Button(app, text="+", command=calculate_add)
    add_button.grid(row=3, column=0)

    subtract_button = tk.Button(app, text="-", command=calculate_subtract)
    subtract_button.grid(row=3, column=1)

    multiply_button = tk.Button(app, text="*", command=calculate_multiply)
    multiply_button.grid(row=3, column=2)

    divide_button = tk.Button(app, text="/", command=calculate_divide)
    divide_button.grid(row=3, column=3)

    digits = [
        ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
        ('4', 5, 0), ('5', 5, 1), ('6', 5, 2),
        ('1', 6, 0), ('2', 6, 1), ('3', 6, 2),
        ('0', 7, 1)
    ]

    for (digit, row, col) in digits:
        button = tk.Button(app, text=digit, command=lambda d=digit: on_digit_button_click(d))
        button.grid(row=row, column=col)

    app.mainloop()