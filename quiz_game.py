import random

questions = [
    {
        "question": "What is capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["A) Python", "B) JavaScript", "C) C++", "D) Jave"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
        "answer": "B"
    }
]

def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ")
    return answer.upper() == question["answer"]

def run_quiz(questions):
    score = 0
    random.shuffle(questions)
    for question in questions:
        if ask_question(question):
            print('Correct!\n')
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}")
    print(f"You got {score} out of {len(questions)}")


print('Welcome to my Quiz to my quiz game')
print('Do you want to play')
reply = input("Enter Yes to play and No to quit: ")
if reply.lower() == 'yes':
    run_quiz(questions)
else:
    quit()
