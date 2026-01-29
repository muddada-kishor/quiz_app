import tkinter as tk

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Online Quiz App")
root.geometry("500x450")
root.resizable(False, False)

# ---------------- QUESTIONS DATA ----------------
questions = [
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "JavaScript", "C++", "Java"],
        "answer": "JavaScript"
    },
    {
        "question": "Who developed Python?",
        "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Elon Musk"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["List", "Set", "Dictionary", "Tuple"],
        "answer": "Tuple"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "<!--"],
        "answer": "#"
    }
]

current_question = 0
score = 0

# ---------------- FUNCTIONS ----------------
def start_quiz():
    title_label.pack_forget()
    info_label.pack_forget()
    start_button.pack_forget()
    show_question()

def show_question():
    question_label.config(text=questions[current_question]["question"])
    
    options = questions[current_question]["options"]
    for i in range(4):
        option_buttons[i].config(
            text=options[i],
            command=lambda opt=options[i]: check_answer(opt)
        )

def check_answer(selected_option):
    global current_question, score

    correct_answer = questions[current_question]["answer"]

    if selected_option == correct_answer:
        score += 1

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        show_result()

def show_result():
    question_label.config(
        text=f"Quiz Completed! 🎉\nYour Score: {score}/{len(questions)}",
        font=("Arial", 16, "bold")
    )

    for btn in option_buttons:
        btn.pack_forget()

    restart_button.pack(pady=20)

def restart_quiz():
    global current_question, score
    current_question = 0
    score = 0

    restart_button.pack_forget()

    for btn in option_buttons:
        btn.pack(pady=5)

    show_question()

# ---------------- UI ELEMENTS ----------------
title_label = tk.Label(root, text="Welcome to Quiz App", font=("Arial", 22, "bold"))
title_label.pack(pady=30)

info_label = tk.Label(root, text="Click Start to begin the quiz", font=("Arial", 12))
info_label.pack(pady=10)

start_button = tk.Button(root, text="Start Quiz", font=("Arial", 12), width=15, command=start_quiz)
start_button.pack(pady=20)

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=450)
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=30)
    btn.pack(pady=5)
    option_buttons.append(btn)

restart_button = tk.Button(root, text="Restart Quiz", font=("Arial", 12), command=restart_quiz)

# ---------------- RUN ----------------
root.mainloop()