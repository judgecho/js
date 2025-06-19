import sqlite3
import hashlib
import json

DB_PATH = "instance/database.db"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 사용자 테이블 초기화 및 생성
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )""")

    # 시험 테이블 초기화 및 생성
    cur.execute("DROP TABLE IF EXISTS exams")
    cur.execute("""
    CREATE TABLE exams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        questions TEXT NOT NULL,
        total_score INTEGER NOT NULL
    )""")

    # 관리자 계정 생성
    users = [
        ('master', hash_password('1234'), 'admin'),
        ('vice', hash_password('1234'), 'manager'),
        ('teacher', hash_password('1234'), 'teacher'),
    ]
    cur.executemany("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", users)

    # 예시 시험 데이터 생성
    sample_questions = [
        {"number": 1, "question": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Rome"], "answer": 3},
        {"number": 2, "question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": 2},
        {"number": 3, "question": "Which is a fruit?", "options": ["Car", "Banana", "Stone", "Chair"], "answer": 2},
        {"number": 4, "question": "Select the verb.", "options": ["run", "apple", "blue", "table"], "answer": 1}
    ]
    exam_data = (
        "중2 영어 중간고사 예시",
        json.dumps(sample_questions),
        100
    )
    cur.execute("INSERT INTO exams (title, questions, total_score) VALUES (?, ?, ?)", exam_data)

    conn.commit()
    conn.close()
    print("✅ 테스트 데이터 삽입 완료!")

if __name__ == "__main__":
    main()