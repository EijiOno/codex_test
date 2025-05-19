"""Simple GUI calculator using tkinter."""
from tkinter import Tk, Entry, Button, END
from calculator import eval_expr


def on_click(key, entry):
    """Handle button click."""
    if key == "C":
        entry.delete(0, END)
    elif key == "=":
        try:
            result = eval_expr(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except Exception as exc:
            entry.delete(0, END)
            entry.insert(END, f"Error: {exc}")
    else:
        entry.insert(END, key)



def create_gui():
    root = Tk()
    root.title("Calculator")

    entry = Entry(root, width=25, borderwidth=2, relief="groove")
    entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "=", "+",
        "C"
    ]

    row = 1
    col = 0
    for btn_text in buttons:
        action = lambda x=btn_text: on_click(x, entry)
        b = Button(root, text=btn_text, width=5, command=action)
        b.grid(row=row, column=col, padx=2, pady=2)
        col += 1
        if col > 3:
            col = 0
            row += 1

    root.mainloop()


if __name__ == "__main__":
    create_gui()
