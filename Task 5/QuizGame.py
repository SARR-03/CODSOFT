import tkinter as tk
from tkinter import messagebox

class QuizGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"}, {"question": "How many Alphabets are there in ABCD?", "options": ["21", "22", "23"], "answer": "23"}
            # Add more questions...
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(3):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(pady=5)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)

        self.result_button = tk.Button(root, text="Show Result", command=self.show_result)
        self.result_button.pack(pady=5)

        self.update_question()

    def update_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)
                self.option_buttons[i].config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
        else:
            self.question_label.config(text="Quiz Completed!")
            for button in self.option_buttons:
                button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)

    def check_answer(self, selected_index):
        selected_option = self.questions[self.current_question]["options"][selected_index]
        correct_answer = self.questions[self.current_question]["answer"]
        if selected_option == correct_answer:
            self.score += 1
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        self.update_question()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"Your Score: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameGUI(root)
    root.mainloop()
