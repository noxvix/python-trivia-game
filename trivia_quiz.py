import requests

def fetch_trivia_questions(amount=10, category=None, difficulty=None, type=None):
    url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "category": category,
        "difficulty": difficulty,
        "type": type
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print(f"Failed to fetch questions with status code: {response.status_code}")
        return None

def display_questions(questions):
    for index, question in enumerate(questions, start=1):
        print(f"Question {index}: {question['question']}")
        print(f"Correct Answer: {question['correct_answer']}")
        print(f"Additional Choices: {', '.join(question['incorrect_answers'])}")
        print("\n")

if __name__ == "__main__":
    trivia_questions = fetch_trivia_questions(amount=10, difficulty="medium", type="multiple")
    if trivia_questions:
        display_questions(trivia_questions)
    else:
        print("No questions fetched.")
