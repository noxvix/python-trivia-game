Trivia Quiz CLI
An interactive trivia quiz game in Python utilizing the Open Trivia API. This command-line application fetches trivia questions based on various parameters and displays them to users along with the correct answers and additional choices.

Table of Contents
Prerequisites
Installation
Usage
Customization
Contributing
License
Prerequisites
Python 3.6+
pip (Python package manager)
Installation
Clone this repository:
bash
Copy code
git clone https://github.com/noxvix/trivia-quiz-cli.git
Navigate to the project directory:
bash
Copy code
cd trivia-quiz-cli
Install the required libraries:
bash
Copy code
pip install -r requirements.txt
Usage
To start the trivia quiz game, run the following command:

bash
Copy code
python trivia_quiz.py
By default, the application fetches 10 medium-difficulty multiple-choice questions. The questions and their respective answers are displayed in the terminal.

Customization
You can customize the number of questions, difficulty level, and question type by modifying the fetch_trivia_questions() function call in trivia_quiz.py. For example:

python
Copy code
trivia_questions = fetch_trivia_questions(amount=20, difficulty="easy", type="boolean")
Valid difficulty levels: easy, medium, hard

Valid question types: multiple, boolean

For more customization options, please refer to the Open Trivia API documentation.

Contributing
Contributions are welcome! Please feel free to submit pull requests, report issues, or suggest new features.

Fork the repository.
Create a new branch with a descriptive name: git checkout -b your-feature-branch
Make your changes.
Commit your changes with a clear commit message: git commit -m "Add a new feature"
Push your changes to your fork: git push origin your-feature-branch
Create a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more information.
