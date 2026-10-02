import tkinter as tk
from tkinter import ttk
import math

# ---------- YOUR CALCULATOR CODE ----------

def calculate():
    # Read an input with:
    # entries["a"].get()
    #
    # This returns text. To turn it into a number:
    # float(entries["a"].get())
    #
    # Remember: some boxes will be empty!
    #
    # Show your answer with:
    # result_text.set("Your answer here")
    
    try:
        A = float(entries["A"].get())
        B = float(entries["B"].get())
        a = float(entries["a"].get())

        if not all(math.isfinite(value) for value in (A, B, a)):
            result_text.set("Please enter finite numbers.")
            return

        if a <= 0:
            result_text.set("Side a must be greater than zero.")
            return

        if A <= 0 or B <= 0:
            result_text.set("Angles A and B must be greater than zero.")
            return

        if A + B >= 180:
            result_text.set("Angles A and B must add up to less than 180°.")
            return

        A_rad = math.radians(A)
        B_rad = math.radians(B)
        sin_a = math.sin(A_rad)
        sin_b = math.sin(B_rad)
        b = (a * sin_b) / sin_a

        result_text.set(f"The length of side b is: {b:.2f}")

    except ValueError:
        result_text.set("Please enter valid numbers for A, B, and a.")
        return







# ---------- INTERFACE CODE ----------

window = tk.Tk()
window.title("Triangle Calculator")
window.geometry("620x720")
window.minsize(520, 650)
window.configure(bg="#172033")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TButton",
    font=("Segoe UI", 11),
    padding=10,
)

main = tk.Frame(window, bg="#172033")
main.pack(fill="both", expand=True, padx=25, pady=20)

tk.Label(
    main,
    text="Triangle Calculator",
    font=("Segoe UI", 24, "bold"),
    fg="#f1f5f9",
    bg="#172033",
).pack()

tk.Label(
    main,
    text="Enter the sides and angles you know. Leave the rest blank.",
    font=("Segoe UI", 10),
    fg="#b8c5d9",
    bg="#172033",
    wraplength=460,
).pack(pady=(8, 12))

# Triangle diagram — a guide, not drawn to match the inputs.
canvas = tk.Canvas(
    main,
    width=460,
    height=220,
    bg="#172033",
    highlightthickness=0,
)
canvas.pack()

canvas.create_polygon(
    65, 180,
    405, 180,
    270, 35,
    fill="#243954",
    outline="#53d8ce",
    width=3,
)

# Each angle is opposite its matching lowercase side.
labels = [
    (45, 185, "A"),
    (425, 185, "B"),
    (270, 18, "C"),
    (350, 100, "a"),
    (150, 100, "b"),
    (235, 200, "c"),
]

for x, y, label in labels:
    canvas.create_text(
        x, y,
        text=label,
        fill="#f1f5f9",
        font=("Segoe UI", 15, "bold"),
    )

inputs = tk.Frame(main, bg="#172033")
inputs.pack(fill="x", pady=12)

inputs.columnconfigure(0, weight=1)
inputs.columnconfigure(1, weight=1)

entries = {}

for column, (heading, names) in enumerate([
    ("Side lengths", ("a", "b", "c")),
    ("Angles (degrees)", ("A", "B", "C")),
]):
    tk.Label(
        inputs,
        text=heading,
        font=("Segoe UI", 12, "bold"),
        fg="#53d8ce",
        bg="#172033",
    ).grid(row=0, column=column, pady=8)

    for row, name in enumerate(names, start=1):
        field = tk.Frame(inputs, bg="#172033")
        field.grid(row=row, column=column, padx=12, pady=6)

        tk.Label(
            field,
            text=f"{name}:",
            width=3,
            font=("Segoe UI", 12),
            fg="#f1f5f9",
            bg="#172033",
        ).pack(side="left")

        entry = ttk.Entry(field, width=13, font=("Segoe UI", 12))
        entry.pack(side="left")
        entries[name] = entry

result_text = tk.StringVar(value="Your results will appear here.")


def clear():
    for entry in entries.values():
        entry.delete(0, tk.END)
    result_text.set("Your results will appear here.")
    entries["a"].focus_set()


buttons = tk.Frame(main, bg="#172033")
buttons.pack(pady=12)

ttk.Button(
    buttons, text="Calculate", command=calculate
).pack(side="left", padx=6)

ttk.Button(
    buttons, text="Clear", command=clear
).pack(side="left", padx=6)

tk.Label(
    main,
    textvariable=result_text,
    font=("Segoe UI", 12),
    fg="#f1f5f9",
    bg="#243954",
    padx=15,
    pady=15,
    wraplength=450,
    justify="left",
).pack(fill="both", expand=True, pady=(5, 0))

window.mainloop()