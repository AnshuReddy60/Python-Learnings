import tkinter as tk

window = tk.Tk()
window.title("Python Calculator")
window.geometry("350x500")
window.resizable(False, False)
window.configure(bg="lightgray")

display_value = tk.StringVar()
display = tk.Entry(
    window,
    textvariable=display_value,
    state="readonly",
    font=("Arial", 24),
    justify="right",
)
display.pack(fill="x", padx=20, pady=20)

button_frame = tk.Frame(window, bg="lightgray")
button_frame.pack()

first_number = None
current_operator = None
start_new_input = False


def add_number(number):
    global start_new_input

    if start_new_input or display_value.get() == "Error":
        display_value.set("")
        start_new_input = False

    display_value.set(display_value.get() + number)


def add_decimal():
    global start_new_input

    if start_new_input or display_value.get() == "Error":
        display_value.set("0.")
        start_new_input = False
        return

    current_text = display_value.get()
    if "." not in current_text:
        display_value.set((current_text or "0") + ".")


def format_number(number):
    if number.is_integer():
        return str(int(number))
    return str(number)


def choose_operator(operator):
    global first_number, current_operator, start_new_input

    current_text = display_value.get()
    if current_text == "" or current_text == "Error":
        return

    first_number = float(current_text)
    current_operator = operator
    display_value.set("")
    start_new_input = False


def calculate():
    global first_number, current_operator, start_new_input

    if first_number is None or current_operator is None:
        return

    current_text = display_value.get()
    if current_text == "" or current_text == "Error":
        return

    second_number = float(current_text)

    try:
        if current_operator == "+":
            result = first_number + second_number
        elif current_operator == "-":
            result = first_number - second_number
        elif current_operator == "*":
            result = first_number * second_number
        elif current_operator == "/":
            result = first_number / second_number
    except ZeroDivisionError:
        display_value.set("Error")
        first_number = None
        current_operator = None
        start_new_input = True
        return

    display_value.set(format_number(result))
    first_number = None
    current_operator = None
    start_new_input = True


def convert_to_percent():
    global start_new_input

    current_text = display_value.get()
    if current_text == "" or current_text == "Error":
        return

    number = float(current_text) / 100
    display_value.set(format_number(number))
    start_new_input = True


def clear_calculator():
    global first_number, current_operator, start_new_input

    display_value.set("")
    first_number = None
    current_operator = None
    start_new_input = False


number_layout = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
    ("0", 3, 1),
]

for number, row, column in number_layout:
    button = tk.Button(
        button_frame,
        text=number,
        font=("Arial", 18),
        width=5,
        height=2,
        command=lambda value=number: add_number(value),
    )
    button.grid(row=row, column=column, padx=5, pady=5)

decimal_button = tk.Button(
    button_frame,
    text=".",
    font=("Arial", 18),
    width=5,
    height=2,
    command=add_decimal,
)
decimal_button.grid(row=3, column=0, padx=5, pady=5)

for operator, row in [("+", 0), ("-", 1), ("*", 2), ("/", 3)]:
    operator_button = tk.Button(
        button_frame,
        text=operator,
        font=("Arial", 18),
        width=5,
        height=2,
        command=lambda value=operator: choose_operator(value),
    )
    operator_button.grid(row=row, column=3, padx=5, pady=5)

percent_button = tk.Button(
    button_frame,
    text="%",
    font=("Arial", 18),
    width=5,
    height=2,
    command=convert_to_percent,
)
percent_button.grid(row=4, column=3, padx=5, pady=5)

clear_button = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 18),
    width=5,
    height=2,
    command=clear_calculator,
)
clear_button.grid(row=4, column=0, padx=5, pady=5)

equals_button = tk.Button(
    button_frame,
    text="=",
    font=("Arial", 18),
    width=12,
    height=2,
    command=calculate,
)
equals_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

window.mainloop()