from main import calculate_score, QUESTIONS_DB

def test_all_correct():
    answers = [1, 2, 1, 2, 3]  
    assert calculate_score(answers, QUESTIONS_DB) == 5

def test_no_correct():
    answers = [0, 0, 0, 0, 0]
    score = calculate_score(answers, QUESTIONS_DB)
    assert score < 5 

def test_mixed_answers():
    answers = [1, 0, 1, 0, 3]
    score = calculate_score(answers, QUESTIONS_DB)
    assert score == 3

def test_empty_db():
    answers = []
    db = []
    assert calculate_score(answers, db) == 0
