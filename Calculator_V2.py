import tkinter as tk
from functools import partial

# Window setup
win = tk.Tk()
win.title("Calcu-latorV2")
win.geometry("500x600+400+100")
win.configure(bg="#1E1E1E")  # Optional: Dark background theme for the window

result_var = tk.StringVar(value="0")  # Display value

# Display label (calculator screen)
tk.Label(
    win, textvariable=result_var, font=("Verdana", 36, "bold"), bd=15,
    bg="#2E8B57", fg="white", anchor="e"
).grid(row=0, column=0, columnspan=4, sticky="nsew")


def sanitize_input(expression):
    """Remove trailing operators to prevent invalid eval."""
    while expression and expression[-1] in "+-x÷/^%":
        expression = expression[:-1]
    return expression


def click_button(char):
    current = result_var.get()

    if char == 'C':  # Clear everything
        result_var.set("0")
    elif char == '=':  # Evaluate the expression
        try:
            sanitized_expr = sanitize_input(current)  # Remove trailing operators
            result = eval(sanitized_expr.replace('x', '*').replace('÷', '/').replace('^', '**'))
            result_var.set(str(result))
        except ZeroDivisionError:
            result_var.set("Cannot divide by 0")
        except:
            result_var.set("Error")
    else:  # Input handling
        if current == "0" or current == "Error" or current == "Cannot divide by 0":
            result_var.set(char)  # Reset display if starting fresh
        else:
            # Prevent duplicate operators
            if current[-1] in "+-x÷/^%" and char in "+-x÷/^%":
                result_var.set(current[:-1] + char)  # Replace last operator
            else:
                result_var.set(current + char)


# Button layout
buttons = [
    ('^', 1, 0), ('//', 1, 1), ('%', 1, 2), ('C', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('x', 4, 3),
    ('.', 5, 0), ('0', 5, 1), ('=', 5, 2), ('÷', 5, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    tk.Button(
        win, text=text, font=("Helvetica", 20), width=5, height=2,
        bg="#1C1C1C", fg="#FFFFFF", command=partial(click_button, text),
        relief="flat", activebackground="#2E8B57", activeforeground="white"
    ).grid(row=row, column=col, sticky="nsew", padx=10, pady=10)

# Configure window grids
for i in range(4):
    win.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    win.grid_rowconfigure(i, weight=1)

win.mainloop()
