import random
import tkinter as tk
from tkinter import ttk, messagebox


MAX_NUMBER = 100
QUESTIONS_PER_ROUND = 10


class MathGameApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("🌟 Math Adventure for Kids 🌟")
        self.root.geometry("700x520")
        self.root.configure(bg="#FFF7D6")

        self.level = tk.IntVar(value=1)
        self.topic = tk.StringVar(value="Mixed")

        self.score = 0
        self.question_count = 0
        self.current_answer: str | int = ""

        self._build_ui()
        self.new_question()

    def _build_ui(self) -> None:
        header = tk.Label(
            self.root,
            text="Welcome to Math Adventure!",
            font=("Comic Sans MS", 24, "bold"),
            bg="#FFF7D6",
            fg="#5A3D9A",
        )
        header.pack(pady=(15, 8))

        controls_frame = tk.Frame(self.root, bg="#FFF7D6")
        controls_frame.pack(pady=8)

        tk.Label(
            controls_frame,
            text="Choose Level:",
            font=("Arial", 12, "bold"),
            bg="#FFF7D6",
        ).grid(row=0, column=0, padx=6)

        level_combo = ttk.Combobox(
            controls_frame,
            values=[1, 2, 3, 4, 5],
            textvariable=self.level,
            width=5,
            state="readonly",
        )
        level_combo.grid(row=0, column=1, padx=6)
        level_combo.bind("<<ComboboxSelected>>", lambda _event: self.new_question())

        tk.Label(
            controls_frame,
            text="Choose Topic:",
            font=("Arial", 12, "bold"),
            bg="#FFF7D6",
        ).grid(row=0, column=2, padx=6)

        topic_combo = ttk.Combobox(
            controls_frame,
            values=[
                "Mixed",
                "Addition",
                "Subtraction",
                "Number Pattern",
                "Odd or Even",
                "Higher or Lower",
            ],
            textvariable=self.topic,
            width=16,
            state="readonly",
        )
        topic_combo.grid(row=0, column=3, padx=6)
        topic_combo.bind("<<ComboboxSelected>>", lambda _event: self.new_question())

        self.progress_label = tk.Label(
            self.root,
            text="Question 1 of 10   |   Score: 0",
            font=("Arial", 13, "bold"),
            bg="#FFF7D6",
            fg="#1F6E8C",
        )
        self.progress_label.pack(pady=(8, 10))

        question_card = tk.Frame(self.root, bg="#E0F7FA", bd=3, relief="ridge")
        question_card.pack(fill="x", padx=30, pady=10)

        self.question_label = tk.Label(
            question_card,
            text="",
            font=("Arial", 20, "bold"),
            bg="#E0F7FA",
            fg="#003049",
            wraplength=620,
            justify="center",
            pady=28,
        )
        self.question_label.pack()

        answer_frame = tk.Frame(self.root, bg="#FFF7D6")
        answer_frame.pack(pady=15)

        tk.Label(
            answer_frame,
            text="Your Answer:",
            font=("Arial", 14, "bold"),
            bg="#FFF7D6",
        ).grid(row=0, column=0, padx=8)

        self.answer_entry = tk.Entry(answer_frame, font=("Arial", 14), width=18)
        self.answer_entry.grid(row=0, column=1, padx=8)
        self.answer_entry.bind("<Return>", lambda _event: self.check_answer())

        submit_button = tk.Button(
            answer_frame,
            text="Check ✅",
            command=self.check_answer,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=14,
        )
        submit_button.grid(row=0, column=2, padx=10)

        button_frame = tk.Frame(self.root, bg="#FFF7D6")
        button_frame.pack(pady=8)

        tk.Button(
            button_frame,
            text="Next Question ➡️",
            command=self.new_question,
            font=("Arial", 11, "bold"),
            bg="#2196F3",
            fg="white",
            padx=12,
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            button_frame,
            text="Start New Round 🔄",
            command=self.reset_round,
            font=("Arial", 11, "bold"),
            bg="#FF9800",
            fg="white",
            padx=12,
        ).grid(row=0, column=1, padx=10)

        self.feedback_label = tk.Label(
            self.root,
            text="Let's learn and have fun! 🎉",
            font=("Arial", 14, "bold"),
            bg="#FFF7D6",
            fg="#5A3D9A",
        )
        self.feedback_label.pack(pady=(12, 0))

    def get_level_limit(self) -> int:
        limits = {1: 10, 2: 25, 3: 50, 4: 75, 5: MAX_NUMBER}
        return limits.get(self.level.get(), 10)

    def random_topic(self) -> str:
        topic = self.topic.get()
        if topic == "Mixed":
            return random.choice(
                [
                    "Addition",
                    "Subtraction",
                    "Number Pattern",
                    "Odd or Even",
                    "Higher or Lower",
                ]
            )
        return topic

    def new_question(self) -> None:
        if self.question_count >= QUESTIONS_PER_ROUND:
            messagebox.showinfo(
                "Round Complete!",
                f"Amazing work! You scored {self.score}/{QUESTIONS_PER_ROUND}.\n"
                "Click 'Start New Round' to play again.",
            )
            return

        limit = self.get_level_limit()
        chosen_topic = self.random_topic()

        if chosen_topic == "Addition":
            a = random.randint(0, limit)
            b = random.randint(0, limit)
            self.current_answer = a + b
            question = f"What is {a} + {b}?"
        elif chosen_topic == "Subtraction":
            a = random.randint(0, limit)
            b = random.randint(0, a)
            self.current_answer = a - b
            question = f"What is {a} - {b}?"
        elif chosen_topic == "Number Pattern":
            step = random.randint(1, min(10, max(2, limit // 8)))
            start = random.randint(0, max(0, limit - (step * 4)))
            pattern = [start + step * i for i in range(5)]
            self.current_answer = pattern[4]
            question = (
                "Find the missing number:\n"
                f"{pattern[0]}, {pattern[1]}, {pattern[2]}, {pattern[3]}, ?"
            )
        elif chosen_topic == "Odd or Even":
            number = random.randint(0, limit)
            self.current_answer = "even" if number % 2 == 0 else "odd"
            question = f"Is {number} odd or even?"
        else:  # Higher or Lower
            left = random.randint(0, limit)
            right = random.randint(0, limit)
            while right == left:
                right = random.randint(0, limit)
            self.current_answer = max(left, right)
            question = f"Which number is higher: {left} or {right}?"

        self.question_label.config(text=question)
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="Type your answer and press Check ✅", fg="#5A3D9A")
        self.progress_label.config(
            text=(
                f"Question {self.question_count + 1} of {QUESTIONS_PER_ROUND}"
                f"   |   Score: {self.score}"
            )
        )

    def check_answer(self) -> None:
        user_answer = self.answer_entry.get().strip().lower()
        if not user_answer:
            self.feedback_label.config(text="Please type an answer first 🙂", fg="#C62828")
            return

        if isinstance(self.current_answer, int):
            try:
                is_correct = int(user_answer) == self.current_answer
            except ValueError:
                is_correct = False
        else:
            is_correct = user_answer == self.current_answer

        if is_correct:
            self.score += 1
            self.feedback_label.config(text="Great job! That's correct! 🌟", fg="#2E7D32")
        else:
            self.feedback_label.config(
                text=f"Nice try! Correct answer: {self.current_answer}",
                fg="#AD1457",
            )

        self.question_count += 1

        if self.question_count >= QUESTIONS_PER_ROUND:
            self.progress_label.config(
                text=f"Question {QUESTIONS_PER_ROUND} of {QUESTIONS_PER_ROUND}   |   Score: {self.score}"
            )
            messagebox.showinfo(
                "Round Complete!",
                f"You finished this round with {self.score}/{QUESTIONS_PER_ROUND}!\n"
                "Try a harder level now! 🚀",
            )
        else:
            self.new_question()

    def reset_round(self) -> None:
        self.score = 0
        self.question_count = 0
        self.feedback_label.config(text="New round started! You can do it! 💪", fg="#5A3D9A")
        self.new_question()


def main() -> None:
    root = tk.Tk()
    app = MathGameApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
