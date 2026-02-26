import random

import ui


MAX_NUMBER = 100
QUESTIONS_PER_ROUND = 10
TOPICS = [
    "Addition",
    "Subtraction",
    "Number Pattern",
    "Odd or Even",
    "Higher or Lower",
]
LEVEL_LIMITS = {1: 10, 2: 25, 3: 50, 4: 75, 5: MAX_NUMBER}


class MathAdventureView(ui.View):
    def __init__(self):
        super().__init__()
        self.name = "🌟 Math Adventure 🌟"
        self.background_color = "#FFF7D6"
        self.level = 1
        self.topic = "Mixed"
        self.score = 0
        self.question_count = 0
        self.current_answer = None

        self._build_ui()
        self.new_question()

    def _build_ui(self):
        title = ui.Label(frame=(20, 20, self.width - 40, 36), flex="W")
        title.text = "Welcome to Math Adventure!"
        title.alignment = ui.ALIGN_CENTER
        title.font = ("<System-Bold>", 28)
        title.text_color = "#5A3D9A"
        self.add_subview(title)

        self.progress_label = ui.Label(frame=(20, 60, self.width - 40, 28), flex="W")
        self.progress_label.alignment = ui.ALIGN_CENTER
        self.progress_label.font = ("<System-Bold>", 17)
        self.progress_label.text_color = "#1F6E8C"
        self.add_subview(self.progress_label)

        level_label = ui.Label(frame=(20, 100, 90, 28), flex="R")
        level_label.text = "Level:"
        level_label.font = ("<System-Bold>", 16)
        self.add_subview(level_label)

        self.level_control = ui.SegmentedControl(frame=(110, 100, 280, 32), flex="R")
        self.level_control.segments = ["1", "2", "3", "4", "5"]
        self.level_control.selected_index = 0
        self.level_control.action = self.on_level_changed
        self.add_subview(self.level_control)

        topic_label = ui.Label(frame=(20, 138, 90, 28), flex="R")
        topic_label.text = "Topic:"
        topic_label.font = ("<System-Bold>", 16)
        self.add_subview(topic_label)

        self.topic_control = ui.SegmentedControl(frame=(110, 138, self.width - 130, 32), flex="W")
        self.topic_control.segments = ["Mixed", "Add", "Sub", "Pattern", "Odd/Even", "High/Low"]
        self.topic_control.selected_index = 0
        self.topic_control.action = self.on_topic_changed
        self.add_subview(self.topic_control)

        self.question_box = ui.Label(frame=(20, 182, self.width - 40, 130), flex="W")
        self.question_box.background_color = "#E0F7FA"
        self.question_box.border_width = 2
        self.question_box.corner_radius = 10
        self.question_box.alignment = ui.ALIGN_CENTER
        self.question_box.number_of_lines = 0
        self.question_box.font = ("<System-Bold>", 28)
        self.question_box.text_color = "#003049"
        self.add_subview(self.question_box)

        answer_label = ui.Label(frame=(20, 328, 120, 28), flex="R")
        answer_label.text = "Your Answer:"
        answer_label.font = ("<System-Bold>", 16)
        self.add_subview(answer_label)

        self.answer_field = ui.TextField(frame=(145, 326, self.width - 165, 34), flex="W")
        self.answer_field.border_style = ui.TEXT_FIELD_ROUNDED_RECT
        self.answer_field.font = ("<System>", 18)
        self.answer_field.autocorrection_type = False
        self.answer_field.autocapitalization_type = ui.AUTOCAPITALIZE_NONE
        self.answer_field.clear_button_mode = "while_editing"
        self.answer_field.keyboard_type = ui.KEYBOARD_NUMBERS
        self.add_subview(self.answer_field)

        self.check_button = ui.Button(frame=(20, 374, 140, 42), flex="R")
        self.check_button.title = "Check ✅"
        self.check_button.background_color = "#4CAF50"
        self.check_button.tint_color = "white"
        self.check_button.corner_radius = 8
        self.check_button.action = self.check_answer
        self.add_subview(self.check_button)

        self.next_button = ui.Button(frame=(175, 374, 170, 42), flex="R")
        self.next_button.title = "Next Question ➡️"
        self.next_button.background_color = "#2196F3"
        self.next_button.tint_color = "white"
        self.next_button.corner_radius = 8
        self.next_button.action = self.new_question
        self.add_subview(self.next_button)

        self.reset_button = ui.Button(frame=(360, 374, self.width - 380, 42), flex="W")
        self.reset_button.title = "Start New Round 🔄"
        self.reset_button.background_color = "#FF9800"
        self.reset_button.tint_color = "white"
        self.reset_button.corner_radius = 8
        self.reset_button.action = self.reset_round
        self.add_subview(self.reset_button)

        self.feedback_label = ui.Label(frame=(20, 430, self.width - 40, 70), flex="WT")
        self.feedback_label.alignment = ui.ALIGN_CENTER
        self.feedback_label.number_of_lines = 0
        self.feedback_label.font = ("<System-Bold>", 18)
        self.feedback_label.text_color = "#5A3D9A"
        self.feedback_label.text = "Let's learn and have fun! 🎉"
        self.add_subview(self.feedback_label)

    def layout(self):
        self._relayout_controls()

    def _relayout_controls(self):
        w = self.width
        self.progress_label.frame = (20, 60, w - 40, 28)
        self.topic_control.frame = (110, 138, w - 130, 32)
        self.question_box.frame = (20, 182, w - 40, 130)
        self.answer_field.frame = (145, 326, w - 165, 34)
        self.reset_button.frame = (360, 374, w - 380, 42)
        self.feedback_label.frame = (20, 430, w - 40, 70)

    def on_level_changed(self, sender):
        self.level = sender.selected_index + 1
        self.new_question()

    def on_topic_changed(self, sender):
        mapping = {
            0: "Mixed",
            1: "Addition",
            2: "Subtraction",
            3: "Number Pattern",
            4: "Odd or Even",
            5: "Higher or Lower",
        }
        self.topic = mapping.get(sender.selected_index, "Mixed")
        if self.topic == "Odd or Even":
            self.answer_field.keyboard_type = ui.KEYBOARD_DEFAULT
            self.answer_field.placeholder = "Type odd or even"
        else:
            self.answer_field.keyboard_type = ui.KEYBOARD_NUMBERS
            self.answer_field.placeholder = "Type a number"
        self.new_question()

    def get_level_limit(self):
        return LEVEL_LIMITS.get(self.level, 10)

    def select_topic(self):
        if self.topic == "Mixed":
            return random.choice(TOPICS)
        return self.topic

    def update_progress(self):
        shown_question = min(self.question_count + 1, QUESTIONS_PER_ROUND)
        self.progress_label.text = "Question {} of {}   |   Score: {}".format(
            shown_question, QUESTIONS_PER_ROUND, self.score
        )

    def new_question(self, sender=None):
        if self.question_count >= QUESTIONS_PER_ROUND:
            ui.alert(
                "Round Complete!",
                "Amazing work! You scored {}/{}.\nTap Start New Round to play again.".format(
                    self.score, QUESTIONS_PER_ROUND
                ),
                "OK",
                hide_cancel_button=True,
            )
            return

        limit = self.get_level_limit()
        chosen_topic = self.select_topic()

        if chosen_topic == "Addition":
            a = random.randint(0, limit)
            b = random.randint(0, limit)
            self.current_answer = a + b
            question = "What is {} + {}?".format(a, b)
        elif chosen_topic == "Subtraction":
            a = random.randint(0, limit)
            b = random.randint(0, a)
            self.current_answer = a - b
            question = "What is {} - {}?".format(a, b)
        elif chosen_topic == "Number Pattern":
            step = random.randint(1, min(10, max(2, limit // 8)))
            start = random.randint(0, max(0, limit - (step * 4)))
            pattern = [start + step * i for i in range(5)]
            self.current_answer = pattern[4]
            question = "Find the missing number:\n{}, {}, {}, {}, ?".format(*pattern[:4])
        elif chosen_topic == "Odd or Even":
            number = random.randint(0, limit)
            self.current_answer = "even" if number % 2 == 0 else "odd"
            question = "Is {} odd or even?".format(number)
        else:
            left = random.randint(0, limit)
            right = random.randint(0, limit)
            while right == left:
                right = random.randint(0, limit)
            self.current_answer = max(left, right)
            question = "Which number is higher: {} or {}?".format(left, right)

        self.question_box.text = question
        self.answer_field.text = ""
        self.feedback_label.text = "Type your answer and tap Check ✅"
        self.feedback_label.text_color = "#5A3D9A"
        self.update_progress()

    def check_answer(self, sender):
        user_answer = self.answer_field.text.strip().lower()
        if not user_answer:
            self.feedback_label.text = "Please type an answer first 🙂"
            self.feedback_label.text_color = "#C62828"
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
            self.feedback_label.text = "Great job! That's correct! 🌟"
            self.feedback_label.text_color = "#2E7D32"
        else:
            self.feedback_label.text = "Nice try! Correct answer: {}".format(self.current_answer)
            self.feedback_label.text_color = "#AD1457"

        self.question_count += 1

        if self.question_count >= QUESTIONS_PER_ROUND:
            self.update_progress()
            ui.alert(
                "Round Complete!",
                "You finished with {}/{}!\nTry a harder level now! 🚀".format(
                    self.score, QUESTIONS_PER_ROUND
                ),
                "OK",
                hide_cancel_button=True,
            )
            return

        self.new_question()

    def reset_round(self, sender):
        self.score = 0
        self.question_count = 0
        self.feedback_label.text = "New round started! You can do it! 💪"
        self.feedback_label.text_color = "#5A3D9A"
        self.new_question()


def main():
    view = MathAdventureView()
    view.frame = (0, 0, 700, 520)
    view.present("sheet")


if __name__ == "__main__":
    main()
