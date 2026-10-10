import random

QUESTIONS_DB = [
    {
        "text": "Чему равно 1010 в двоичной системе?",
        "options": ["8", "10", "12", "15"],
        "correct_index": 1,
        "reason": "1010₂ = 8 + 2 = 10"
    },
    {
        "text": "Что делает оператор % в Python?",
        "options": ["Деление", "Целочисленное деление", "Остаток от деления", "Степень"],
        "correct_index": 2,
        "reason": "% — это остаток от деления"
    },
    {
        "text": "sin(30°) равен?",
        "options": ["0", "0.5", "1", "√2/2"],
        "correct_index": 1,
        "reason": "sin(30°) = 1/2"
    },
    {
        "text": "Сколько корней у x² = 4?",
        "options": ["0", "1", "2", "∞"],
        "correct_index": 2,
        "reason": "x = ±2 → два корня"
    },
    {
        "text": "Где пишется НН?",
        "options": [
            "жаре_ый картофель",
            "краше_ая дверь",
            "тушё_ая капуста",
            "жаре_ая на масле картошка"
        ],
        "correct_index": 3,
        "reason": "Есть зависимое слово «на масле» → НН"
    }
]


def ask_single_question(q):
    print(q["text"])
    for i, option in enumerate(q["options"]):
        print(f"{i + 1}. {option}")

    while True:
        user_input = input("Твой ответ (номер): ")
        try:
            choice = int(user_input) - 1
            if 0 <= choice < len(q["options"]):
                return choice
            print(f"Введи число от 1 до {len(q['options'])}")
        except ValueError:
            print("Нужно ввести цифру.")


def calculate_score(answers, db):
    score = 0
    for i, q in enumerate(db):
        if answers[i] == q["correct_index"]:
            score += 1
    return score


def run_quiz_session(db):
    shuffled = db.copy()
    random.shuffle(shuffled)

    score = 0
    total = len(shuffled)
    print("=== ЕГЭ-тренажёр: викторина ===\n")

    for q in shuffled:
        chosen = ask_single_question(q)
        if chosen == q["correct_index"]:
            print("✅ Верно!")
            score += 1
        else:
            print("❌ Ошибка.")
            correct_answer = q["options"][q["correct_index"]]
            print(f"Правильный вариант: {correct_answer}")
            print(f"Почему: {q['reason']}")
        print()

    print("=== Итоги ===")
    print(f"Результат: {score} из {total}")
    if score == total:
        print("🎉 Идеально!")
    elif score > total // 2:
        print("👍 Хорошо, продолжай.")
    else:
        print("📚 Есть над чем поработать.")


if __name__ == "__main__":
    run_quiz_session(QUESTIONS_DB)
