import tkinter as tk

root = tk.Tk()
root.title("ماشین حساب پلاس")
root.geometry("320x440")
root.resizable(False, False)
root.configure(bg="#20242b")

expression = ""

display = tk.Entry(
    root, font=("Arial", 25),
    justify="right", bd=0,
    bg="#303640", fg="white"
)
display.pack(fill="x", padx=16, pady=20, ipady=15)

def press(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def calculate():
    global expression
    try:
        allowed = "0123456789.+-*/() "
        if not expression or any(c not in allowed for c in expression):
            raise ValueError
        result = eval(expression, {"__builtins__": {}}, {})
        expression = str(result)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)
    except ZeroDivisionError:
        expression = ""
        display.delete(0, tk.END)
        display.insert(tk.END, "تقسیم بر صفر ممکن نیست")
    except Exception:
        expression = ""
        display.delete(0, tk.END)
        display.insert(tk.END, "عبارت نامعتبر است")

buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "−"],
    ["C", "0", "=", "+"]
]

def handle_button(value):
    if value == "C":
        clear()
    elif value == "=":
        calculate()
    else:
        symbols = {"÷": "/", "×": "*", "−": "-"}
        press(symbols.get(value, value))

frame = tk.Frame(root, bg="#20242b")
frame.pack(expand=True, fill="both", padx=12, pady=8)

for r, row in enumerate(buttons):
    for c, value in enumerate(row):
        color = "#f0a83a" if value in ["+", "−", "×", "÷", "="] else "#3a424e"
        if value == "C":
            color = "#b94b4b"

        button = tk.Button(
            frame, text=value,
            font=("Arial", 20, "bold"),
            bg=color, fg="white",
            bd=0,
            command=lambda v=value: handle_button(v)
        )
        button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
    frame.grid_rowconfigure(i, weight=1)

root.mainloop()
