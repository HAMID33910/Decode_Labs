# General Knowledge Quiz

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["A. Karachi", "B. Lahore", "C. Islamabad", "D. Peshawar"],
        "answer": "C"
    },
    {
        "question": "Who invented Python?",
        "options": ["A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Elon Musk"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "How many continents are there?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Which language is primarily used for AI and Machine Learning?",
        "options": ["A. Java", "B. Python", "C. PHP", "D. C"],
        "answer": "B"
    }
]

score = 0

print("=" * 40)
print("      GENERAL KNOWLEDGE QUIZ")
print("=" * 40)

name = input("Enter your name: ")

for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}")
    print(q["question"])

    for option in q["options"]:
        print(option)

    while True:
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input! Please enter A, B, C or D.")

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}")

print("\n" + "=" * 40)
print(f"Quiz Completed, {name}!")
print(f"Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")