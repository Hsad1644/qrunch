import tkinter as tk
from tkinter import ttk
import json
import random

def set_custom_styles():
    style = ttk.Style()
    
    # Configure styles here
    style.configure("TLabel", font=("Sans", 14))
    style.configure("TButton", font=("Sans", 14))
    style.configure("TRadiobutton", font=("Sans", 14))
    
# Initialize variables
current_question = None
total_questions = 0
correct_answers = 0
wrong_answers = 0

# Function to update the scoreboard
def update_scoreboard():
    global total_questions, correct_answers, wrong_answers
    total_label.config(text=f"Total Questions: {total_questions}")
    correct_label.config(text=f"Correct Answers: {correct_answers}")
    wrong_label.config(text=f"Wrong Answers: {wrong_answers}")
    
    if total_questions > 0:
        accuracy = (correct_answers / total_questions) * 100
        accuracy_label.config(text=f"Accuracy: {accuracy:.2f}%")

answered_question = 0  # Initialize

# Function to select and display a random question
def select_random_question():
    global current_question, total_questions, answered_question
    current_question = random.choice(questions_data)
    question_label.config(text=current_question['question_text'])
    
    # Clear previous selections
    selected_answer.set("")
    for widget in options_frame.winfo_children():
        widget.destroy()
    
    # Display answer options as radio buttons
    for i, option in enumerate(current_question['options']):
        if len(current_question['options']) >= 1: 
            radio = ttk.Radiobutton(options_frame, text=option, variable=selected_answer, value=str(i + 1),
                                    command=lambda option=option: highlight_option(option))
            radio.grid(row=i, column=0, sticky='w')
        else:
            select_random_question()
        
    # if not answered_question:  # Only increment total_questions if the question hasn't been answered
    total_questions += 1
    
    update_scoreboard()
    # answered_question = current_question['question_number']  # set this question number

# Function to highlight the selected and correct option
def highlight_option(selected_option):
    next_button.config(state=tk.NORMAL)
    global correct_answers, wrong_answers, answered_question
    correct_option = current_question.get('answer', '1')  # Get the correct answer (default to 1)
    
    for radio in options_frame.winfo_children():
        option_text = radio['text']
        if option_text == selected_option and total_questions >= correct_answers + wrong_answers:
            if option_text == current_question['options'][int(correct_option) - 1]:
                radio.configure(style='Correct.TLabel')  # Correct and selected option in green
                correct_answers += 1
            else:
                radio.configure(style='Clicked.TLabel')  # Selected option in red
                wrong_answers += 1
        elif option_text == current_question['options'][int(correct_option) - 1]:
            radio.configure(style='Correct.TLabel')  # Correct option in green
        elif answered_question:  # Keep the selected option highlighted
            radio.configure(style='Clicked.TLabel')  # Selected option in red
        else:
            radio.configure(style='TLabel')  # Default style
    
    update_scoreboard()

# Create the main window
root = tk.Tk()
root.title("Quiz App")
set_custom_styles()
# Load your JSON data from "output.json"
with open('output.json', 'r', encoding='utf-8') as json_file:
    questions_data = json.load(json_file)

# Create a StringVar
selected_answer = tk.StringVar()

# Create styles for highlighting correct, selected, and default options
style = ttk.Style()
style.configure('Correct.TLabel', foreground='green')  # Correct option in green
style.configure('Clicked.TLabel', foreground='red')  # Selected option in red
style.configure('TButton', foreground='black')  # Default style

# Create widgets
question_label = ttk.Label(root, text="", wraplength=400)
options_frame = ttk.Frame(root)
next_button = ttk.Button(root, text="Next Question", command=select_random_question, state=tk.DISABLED)

# Create scoreboard labels
total_label = ttk.Label(root, text="Total Questions: 0")
correct_label = ttk.Label(root, text="Correct Answers: 0")
wrong_label = ttk.Label(root, text="Wrong Answers: 0")
accuracy_label = ttk.Label(root, text="Accuracy: N/A")

# Grid layout for widgets
question_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
options_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
next_button.grid(row=2, column=0, padx=10, pady=10)
total_label.grid(row=0, column=2, padx=10, pady=10, sticky='w')
correct_label.grid(row=1, column=2, padx=10, pady=10, sticky='w')
wrong_label.grid(row=2, column=2, padx=10, pady=10, sticky='w')
accuracy_label.grid(row=3, column=2, padx=10, pady=10, sticky='w')

# Initial question
select_random_question()

# Start the GUI main loop
root.mainloop()
