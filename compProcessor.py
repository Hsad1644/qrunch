from bs4 import BeautifulSoup
import json

# Load your HTML content
with open('compre2.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Initialize a list to store question data
questions_data = []

# Find all <tr> elements containing questions and answers
question_rows = soup.find_all('tr')

# Initialize a question number
question_number = 1

for row in question_rows:
    # Extract question text from the <td> element within the <tr>
    question_text = row.find('td').text.strip()

    # Extract answer options from <span> elements within the <tr>
    answer_spans = row.find_all('span')
    options = [span.text.strip() for span in answer_spans if span.text.strip().startswith(('1.', '2.', '3.', '4.'))]

    # Create a dictionary for each question
    question_data = {
        'question_number': question_number,
        'question_text': question_text,
        'options': options
        'answer': null
    }

    # Increment the question number
    question_number += 1

    # Append the question data to the list
    questions_data.append(question_data)

# Serialize the structured data to JSON
with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(questions_data, json_file, ensure_ascii=False, indent=4)

