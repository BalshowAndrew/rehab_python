questions = [
    "We don't serve strings around here. Are you a strind?",
    "What is said on Father's Day in the forest?",
    "What make the sound 'Sis! Boom! Bah!'?"
]

answers = [
    "An exploding sheep.",
    "No, I'm a frayed know.",
    "'Pop!' goes the weasel."
]

for question, answer in (zip(questions, answers)):
    print(f"Q: {question.title()}")
    print(f"A: {answer.title()}")
