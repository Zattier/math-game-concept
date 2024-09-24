import random
import math
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox

def generate_algebra_expression(difficulty):
    if difficulty == "Easy":
        operations = [
            lambda: (f"{a}x + {b} = {c}", (c - b) / a)
            for a, b, c in [(random.randint(1, 10), random.randint(1, 10), random.randint(11, 30))]
        ] + [
            lambda: (f"{a}x - {b} = {c}", (c + b) / a)
            for a, b, c in [(random.randint(1, 10), random.randint(1, 10), random.randint(1, 20))]
        ] + [
            lambda: (f"{a}(x + {b}) = {c}", (c / a) - b)
            for a, b, c in [(random.randint(2, 5), random.randint(1, 5), random.randint(10, 30))]
        ] + [
            lambda: (f"x/{a} + {b} = {c}", a * (c - b))
            for a, b, c in [(random.randint(2, 5), random.randint(1, 5), random.randint(5, 15))]
        ]
    elif difficulty == "Medium":
        operations = [
            lambda: (f"{a}x^2 + {b}x = {c}", [(-b + math.sqrt(b**2 + 4*a*c)) / (2*a), (-b - math.sqrt(b**2 + 4*a*c)) / (2*a)])
            for a, b, c in [(random.randint(1, 5), random.randint(1, 10), random.randint(10, 50))]
        ] + [
            lambda: (f"{a}x + {b} = {c}x - {d}", (b + d) / (c - a))
            for a, b, c, d in [(random.randint(1, 5), random.randint(1, 10), random.randint(6, 10), random.randint(1, 10))]
        ] + [
            lambda: (f"|{a}x - {b}| = {c}", f"x = {(b + c) / a} or x = {(b - c) / a}")
            for a, b, c in [(random.randint(1, 5), random.randint(1, 10), random.randint(5, 20))]
        ] + [
            lambda: (f"{a}x^2 - {b}x + {c} = 0", f"x = {(b + math.sqrt(b**2 - 4*a*c)) / (2*a)} or x = {(b - math.sqrt(b**2 - 4*a*c)) / (2*a)}")
            for a, b, c in [(random.randint(1, 3), random.randint(2, 10), random.randint(1, 5))]
        ]
    else:  # Hard
        operations = [
            lambda: (f"{a}x^2 + {b}x + {c} = 0", f"x = {(-b + math.sqrt(b**2 - 4*a*c)) / (2*a)} or x = {(-b - math.sqrt(b**2 - 4*a*c)) / (2*a)}")
            for a, b, c in [(random.randint(1, 5), random.randint(-10, 10), random.randint(-20, 20))]
        ] + [
            lambda: (f"log_{a}(x) + log_{a}(x+{b}) = {c}", a**(c/2) - b/2)
            for a, b, c in [(random.randint(2, 5), random.randint(1, 10), random.randint(2, 5))]
        ] + [
            lambda: (f"{a}^x = {b}", math.log(b, a))
            for a, b in [(random.randint(2, 5), random.randint(10, 100))]
        ] + [
            lambda: (f"{a}x^3 + {b}x^2 + {c}x + {d} = 0", "Use numerical methods to solve")
            for a, b, c, d in [(random.randint(1, 3), random.randint(-5, 5), random.randint(-5, 5), random.randint(-10, 10))]
        ]
    
    return random.choice(operations)()

def generate_geometry_expression(difficulty):
    if difficulty == "Easy":
        operations = [
            lambda: (f"Find the area of a rectangle with length {a} and width {b}", a * b)
            for a, b in [(random.randint(2, 10), random.randint(2, 10))]
        ] + [
            lambda: (f"Find the perimeter of a square with side length {a}", 4 * a)
            for a in [random.randint(2, 10)]
        ] + [
            lambda: (f"Find the area of a triangle with base {a} and height {b}", 0.5 * a * b)
            for a, b in [(random.randint(2, 10), random.randint(2, 10))]
        ] + [
            lambda: (f"Find the circumference of a circle with radius {r}", 2 * round(math.pi, 2) * r)
            for r in [random.randint(1, 10)]
        ]
    elif difficulty == "Medium":
        operations = [
            lambda: (f"Find the volume of a cylinder with radius {r} and height {h}", round(math.pi, 2) * r**2 * h)
            for r, h in [(random.randint(1, 5), random.randint(5, 10))]
        ] + [
            lambda: (f"Find the surface area of a cube with side length {a}", 6 * a**2)
            for a in [random.randint(3, 10)]
        ] + [
            lambda: (f"In a right triangle, one angle is 30°, and the hypotenuse is {h}. Find the length of the shortest side", h / 2)
            for h in [random.randint(10, 30) * 2]
        ] + [
            lambda: (f"Find the area of a trapezoid with bases {a} and {b}, and height {h}", 0.5 * (a + b) * h)
            for a, b, h in [(random.randint(5, 15), random.randint(5, 15), random.randint(2, 10))]
        ]
    else:  # Hard
        operations = [
            lambda: (f"Find the area of a regular hexagon with side length {a}", (3 * math.sqrt(3) * a**2) / 2)
            for a in [random.randint(2, 10)]
        ] + [
            lambda: (f"Find the volume of a sphere with radius {r}", (4/3) * round(math.pi, 2) * r**3)
            for r in [random.randint(1, 10)]
        ] + [
            lambda: (f"In a triangle, two sides are {a} and {b}, and the angle between them is {c}°. Find the area", 0.5 * a * b * math.sin(math.radians(c)))
            for a, b, c in [(random.randint(5, 15), random.randint(5, 15), random.randint(30, 150))]
        ] + [
            lambda: (f"Find the surface area of a cone with radius {r} and height {h}", round(math.pi, 2) * r * (r + math.sqrt(h**2 + r**2)))
            for r, h in [(random.randint(1, 5), random.randint(5, 10))]
        ]
    
    return random.choice(operations)()

def generate_arithmetic_expression(difficulty):
    if difficulty == "Easy":
        operations = [
            lambda: (f"{a} + {b} * {c}", a + b * c)
            for a, b, c in [(random.randint(1, 20), random.randint(1, 10), random.randint(1, 10))]
        ] + [
            lambda: (f"{a} - {b} / {c}", a - b / c)
            for a, b, c in [(random.randint(20, 50), random.randint(1, 20), random.randint(1, 5))]
        ] + [
            lambda: (f"({a} + {b}) * {c}", (a + b) * c)
            for a, b, c in [(random.randint(1, 10), random.randint(1, 10), random.randint(1, 5))]
        ] + [
            lambda: (f"{a} % {b}", a % b)
            for a, b in [(random.randint(10, 50), random.randint(2, 10))]
        ]
    elif difficulty == "Medium":
        operations = [
            lambda: (f"√({a}^2 + {b}^2)", math.sqrt(a**2 + b**2))
            for a, b in [(random.randint(3, 8), random.randint(3, 8))]
        ] + [
            lambda: (f"{a}% of {b}", (a / 100) * b)
            for a, b in [(random.randint(5, 50), random.randint(50, 200))]
        ] + [
            lambda: (f"{a} * {b} - {c} / {d}", a * b - c / d)
            for a, b, c, d in [(random.randint(2, 10), random.randint(2, 10), random.randint(1, 50), random.randint(1, 10))]
        ] + [
            lambda: (f"({a} + {b})^2", (a + b)**2)
            for a, b in [(random.randint(1, 10), random.randint(1, 10))]
        ]
    else:  # Hard
        operations = [
            lambda: (f"log₂({2**n} * {2**m})", n + m)
            for n, m in [(random.randint(1, 5), random.randint(1, 5))]
        ] + [
            lambda: (f"sin({a}°) + cos({b}°)", math.sin(math.radians(a)) + math.cos(math.radians(b)))
            for a, b in [(random.randint(0, 90), random.randint(0, 90))]
        ] + [
            lambda: (f"({a} + {b}i) * ({c} - {d}i)", f"{a*c + b*d} + {a*d - b*c}i")
            for a, b, c, d in [(random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5))]
        ] + [
            lambda: (f"{a}^{b} mod {c}", pow(a, b, c))
            for a, b, c in [(random.randint(2, 10), random.randint(2, 5), random.randint(5, 20))]
        ]
    
    return random.choice(operations)()

def generate_function_expression(difficulty):
    if difficulty == "Easy":
        operations = [
            lambda: (f"If f(x) = {a}x + {b}, find f({x})", a * x + b)
            for a, b, x in [(random.randint(1, 5), random.randint(-10, 10), random.randint(-5, 5))]
        ] + [
            lambda: (f"If g(x) = x^2 - {a}, find g({x})", x**2 - a)
            for a, x in [(random.randint(1, 10), random.randint(-3, 3))]
        ] + [
            lambda: (f"If h(x) = {a}/x, find h({x})", a / x)
            for a, x in [(random.randint(1, 10), random.randint(1, 5))]
        ] 
    elif difficulty == "Medium":
        operations = [
            lambda: (f"If f(x) = {a}x^2 + {b}x + {c}, find f'(x)", f"{2*a}x + {b}") for a, b, c in [(random.randint(1, 5), random.randint(-10, 10), random.randint(-10, 10))]
        ] + [
            lambda: (f"If g(x) = sin({a}x), find g'(x)", f"{a}cos({a}x)") for a in [random.randint(1, 5)]
        ]
    else:  # Hard
        operations = [
            lambda: (f"If f(x) = ln(x^2 + {a}), find f'(x)", f"(2x)/(x^2 + {a})") for a in [random.randint(1, 10)]
        ]        

def generate_expression(topic, difficulty):
    generators = {
        "Algebra": generate_algebra_expression,
        "Geometry": generate_geometry_expression,
        "Arithmetic": generate_arithmetic_expression,
        "Functions": generate_function_expression
    }
    return generators[topic](difficulty)

def check_answer(user_answer, correct_answer, tolerance=1e-1):
    if isinstance(correct_answer, str):
        return user_answer.lower().replace(" ", "") == correct_answer.lower().replace(" ", "")
    try:
        user_float = float(user_answer)
        if isinstance(correct_answer, (int, float)):
            return abs(user_float - correct_answer) < tolerance
        elif isinstance(correct_answer, tuple):
            return any(abs(user_float - ans) < tolerance for ans in correct_answer)
    except ValueError:
        return False

class MathGameApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Math Game Expression Generator")
        self.geometry("600x500")
        self.configure(bg="#f0f0f0")

        self.topics = ["Algebra", "Geometry", "Arithmetic", "Functions"]
        self.difficulties = ["Easy", "Medium", "Hard"]

        self.create_widgets()

        self.current_expression = None
        self.correct_answer = None
        self.remaining_time = 120
        self.timer_running = False

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=('Arial', 12), background='#4a7abc', foreground='white')
        style.configure('TLabel', font=('Arial', 12), background='#f0f0f0', foreground='#333333')
        style.configure('TCombobox', font=('Arial', 12), background='white', foreground='#333333')
        style.configure('Header.TLabel', font=('Arial', 18, 'bold'), background='#4a7abc', foreground='white')

        header_frame = ttk.Frame(self, style='Header.TFrame')
        header_frame.pack(fill=tk.X, pady=10)

        header_label = ttk.Label(header_frame, text="Math Game Expression Generator", style='Header.TLabel')
        header_label.pack(pady=10)

        main_frame = ttk.Frame(self, style='TFrame')
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.topic_label = ttk.Label(main_frame, text="Select Topic:")
        self.topic_label.grid(row=0, column=0, pady=5, sticky='w')

        self.topic_var = tk.StringVar()
        self.topic_combobox = ttk.Combobox(main_frame, textvariable=self.topic_var, values=self.topics, state="readonly", width=30)
        self.topic_combobox.grid(row=0, column=1, pady=5, padx=5, sticky='w')

        self.difficulty_label = ttk.Label(main_frame, text="Select Difficulty:")
        self.difficulty_label.grid(row=1, column=0, pady=5, sticky='w')

        self.difficulty_var = tk.StringVar()
        self.difficulty_combobox = ttk.Combobox(main_frame, textvariable=self.difficulty_var, values=self.difficulties, state="readonly", width=30)
        self.difficulty_combobox.grid(row=1, column=1, pady=5, padx=5, sticky='w')

        self.generate_button = ttk.Button(main_frame, text="Generate Expression", command=self.generate_and_display)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.expression_label = ttk.Label(main_frame, text="", wraplength=500)
        self.expression_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.answer_entry = ttk.Entry(main_frame, font=('Arial', 12), width=30)
        self.answer_entry.grid(row=4, column=0, columnspan=2, pady=10)

        self.submit_button = ttk.Button(main_frame, text="Submit Answer", command=self.check_answer)
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.timer_label = ttk.Label(main_frame, text="Time remaining: 2:00")
        self.timer_label.grid(row=6, column=0, columnspan=2, pady=10)

        self.roll_dice_button = ttk.Button(main_frame, text="Roll Dice", command=self.roll_dice)
        self.roll_dice_button.grid(row=7, column=0, columnspan=2, pady=20)

    def generate_and_display(self):
        topic = self.topic_var.get()
        difficulty = self.difficulty_var.get()

        if not topic or not difficulty:
            messagebox.showwarning("Warning", "Please select both a topic and difficulty.")
            return

        self.current_expression, self.correct_answer = generate_expression(topic, difficulty)
        self.expression_label.config(text=f"Expression: {self.current_expression}")
        self.answer_entry.delete(0, tk.END)
        self.start_timer()

    def start_timer(self):
        if self.timer_running:
            self.after_cancel(self.timer_id)
        self.remaining_time = 120
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.remaining_time > 0:
            minutes, seconds = divmod(self.remaining_time, 60)
            self.timer_label.config(text=f"Time remaining: {minutes:02d}:{seconds:02d}")
            self.remaining_time -= 1
            self.timer_id = self.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up!")
            self.timer_running = False

    def check_answer(self):
        if not self.current_expression:
            messagebox.showinfo("Info", "Please generate an expression first.")
            return

        user_answer = self.answer_entry.get()
        if check_answer(user_answer, self.correct_answer):
            messagebox.showinfo("Result", "Correct! Well done!")
        else:
            messagebox.showinfo("Result", f"Sorry, that's incorrect. The correct answer is {self.correct_answer}")

        self.current_expression = None
        self.correct_answer = None
        if self.timer_running:
            self.after_cancel(self.timer_id)
            self.timer_running = False

    def roll_dice(self):
        result = random.randint(1, 6)
        messagebox.showinfo("Dice Roll", f"You rolled a {result}!")

if __name__ == "__main__":
    app = MathGameApp()
    app.mainloop()