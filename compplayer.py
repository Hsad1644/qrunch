import tkinter as tk
from tkinter import ttk
import json
import random

# Initialize variables
current_question = None

# Function to select and display a random question
def select_random_question():
    global current_question
    current_question = random.choice(questions_data)
    question_label.config(text=current_question['question_text'])
    
    # Clear previous selections
    selected_answer.set("")
    for widget in options_frame.winfo_children():
        widget.destroy()
    
    # Display answer options as radio buttons
    for i, option in enumerate(current_question['options']):
        radio = ttk.Radiobutton(options_frame, text=option, variable=selected_answer, value=str(i + 1),
                                command=lambda option=option: highlight_option(option))
        radio.grid(row=i, column=0, sticky='w')

# Function to highlight the selected and correct option
def highlight_option(selected_option):
    correct_option = current_question.get('answer', '1')  # Get the correct answer (default to 1)
    
    for radio in options_frame.winfo_children():
        option_text = radio['text']
        if option_text == selected_option:
            if option_text == current_question['options'][int(correct_option) - 1]:
                radio.configure(style='Correct.TButton')  # Correct and selected option in green
            else:
                radio.configure(style='Clicked.TButton')  # Selected option in red
        elif option_text == current_question['options'][int(correct_option) - 1]:
            radio.configure(style='Correct.TButton')  # Correct option in green
        else:
            radio.configure(style='TButton')  # Default style

# Create the main window
root = tk.Tk()
root.title("Quiz App")

# Load your JSON data from "output.json"
with open('output.json', 'r', encoding='utf-8') as json_file:
    questions_data = json.load(json_file)

# Create a StringVar
selected_answer = tk.StringVar()

# Create styles for highlighting correct, selected, and default options
style = ttk.Style()
style.configure('Correct.TButton', foreground='green')  # Correct option in green
style.configure('Clicked.TButton', foreground='red')  # Selected option in red
style.configure('TButton', foreground='black')  # Default style

# Create widgets
question_label = ttk.Label(root, text="", wraplength=400)
options_frame = ttk.Frame(root)
next_button = ttk.Button(root, text="Next Question", command=select_random_question)

# Grid layout
question_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
options_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
next_button.grid(row=2, column=0, padx=10, pady=10)

# Initial question
select_random_question()

# Start the GUI main loop
root.mainloop()
