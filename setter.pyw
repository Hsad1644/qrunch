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

# Function to load questions from JSON file
def load_questions():
    with open('output.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

# Function to display the current question and options
def display_question():
    global current_question
    current_question = random.choice(questions_data)
    question_label.config(text=current_question['question_text'])

    # Clear previous selections
    selected_answer.set("")
    for widget in options_frame.winfo_children():
        widget.destroy()

    # Display answer options as radio buttons
    for i, option in enumerate(current_question['options']):
        radio = ttk.Radiobutton(options_frame, text=option, variable=selected_answer, value=str(i + 1))
        radio.grid(row=i, column=0, sticky='w')

# Function to save the marked answer and mark the question
def save_and_mark():
    marked_option = selected_answer.get()
    if marked_option:
        current_question['answer'] = marked_option
        current_question['mark'] = True
        with open('output.json', 'w', encoding='utf-8') as json_file:
            json.dump(questions_data, json_file, ensure_ascii=False, indent=4)
    display_question()

# Create the main window
root = tk.Tk()
root.title("Question Editor")

set_custom_styles() 

# Load questions data from JSON file
questions_data = load_questions()

# Create a StringVar
selected_answer = tk.StringVar()

# Create widgets
question_label = ttk.Label(root, text="", wraplength=400)
options_frame = ttk.Frame(root)
save_button = ttk.Button(root, text="Save", command=save_and_mark)
next_button = ttk.Button(root, text="Next", command=display_question)

# Grid layout
question_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
options_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
save_button.grid(row=2, column=0, padx=10, pady=10)
next_button.grid(row=2, column=1, padx=10, pady=10)

# Display the first question
display_question()

# Start the GUI main loop
root.mainloop()
