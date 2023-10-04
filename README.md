# qrunch
tkinter for making flash cards out of your quizzes; 
made for crunching from question banks, effectively

## Setup
Ensure to have Python 3.x installed with path variables enabled

After cloning/downloading the repo, run `pip install -r requirements.txt`

## Usage
If your question data file has the answers set already, run `player.pyw` by double clicking it and make option choices from the visible items

Right answer is highlighted green, wrong in red

If your answers are to be set manually, run `setter_random.pyw` or `setter_sequential.pyw` by double clicking; Select an option and click save to save the option value to the bank file (`output.json`)
You may also wish to manually make changes to the `output.json` file's `answer` field by changing it to a value desired (starting from 1).

Note: the "mark" field generated from setter programs are an indicator of whether a question has been visited.

Suggest changes/features in [Issues](https://github.com/Hsad1644/qrunch/issues)

## Meta
Upcoming improvements —
* File refactoring
* Extended features
* Better UI
* Improved data pre-processing
