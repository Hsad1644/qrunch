import tkinter as tk
from tkinter import ttk
import json


def set_custom_styles():
    style = ttk.Style()

    # Configure styles here
    style.configure("TLabel", font=("Sans", 14))
    style.configure("TButton", font=("Sans", 14))
    style.configure("TRadiobutton", font=("Sans", 14))


# Function to load questions from JSON file
def load_questions():
    with open("output.json", "r", encoding="utf-8") as json_file:
        return json.load(json_file)


# Initialize variables
questions_data = []
current_question_index = 0
starting_question_number = 1  # Default starting question number


# Function to display the current question and options
def display_question():
    global current_question_index
    if 0 <= current_question_index < len(questions_data):
        question = questions_data[current_question_index]
        question_label.config(
            text=f"Question {current_question_index + 1}: {question['question_text']}"
        )

        # Clear previous selections
        selected_answer.set("")
        for widget in options_frame.winfo_children():
            widget.destroy()

        # Display answer options as radio buttons
        for i, option in enumerate(question["options"]):
            radio = ttk.Radiobutton(
                options_frame, text=option, variable=selected_answer, value=str(i + 1)
            )
            radio.grid(row=i, column=0, sticky="w")
    else:
        question_label.config(text="No more questions")


# Function to display the next question
def display_next_question():
    # save_answer()  # Save the answer before moving to the next question
    global current_question_index
    current_question_index += 1
    display_question()


# Function to save the marked answer
def save_answer():
    marked_option = selected_answer.get()
    if marked_option:
        questions_data[current_question_index]["mark"] = True
        questions_data[current_question_index]["answer"] = int(marked_option)
        with open("output.json", "w", encoding="utf-8") as json_file:
            json.dump(questions_data, json_file, ensure_ascii=False, indent=4)
        display_next_question()


# Function to update the starting question number
def update_starting_question_number():
    global current_question_index
    try:
        starting_question_number = int(starting_question_entry.get())
        current_question_index = (
            starting_question_number - 1
        )  # Adjust the current index based on the starting question number
    except ValueError:
        current_question_index = 0  # Default to 1 if an invalid value is entered
    display_question()


# Create the main window
root = tk.Tk()
root.title("Answer Setting App")

set_custom_styles()

# Load questions data from JSON file
questions_data = load_questions()

# Create a StringVar
selected_answer = tk.StringVar()

# Create widgets
question_label = ttk.Label(root, text="", wraplength=400)
options_frame = ttk.Frame(root)
save_button = ttk.Button(root, text="Save & Next", command=save_answer)
next_button = ttk.Button(root, text="Next Question", command=display_next_question)

# Entry widget for starting question number
starting_question_label = ttk.Label(root, text="Starting Question Number:")
starting_question_entry = ttk.Entry(root)
starting_question_button = ttk.Button(
    root, text="Update", command=update_starting_question_number
)

# Grid layout
question_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
options_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
save_button.grid(row=2, column=0, padx=10, pady=10)
next_button.grid(row=2, column=1, padx=10, pady=10)

starting_question_label.grid(row=3, column=0, padx=10, pady=10)
starting_question_entry.grid(row=3, column=1, padx=10, pady=10)
starting_question_button.grid(row=3, column=2, padx=10, pady=10)

# Display the first question
display_question()

# Start the GUI main loop
root.mainloop()
