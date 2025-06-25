#과목: 오픈소스SW와 파이썬 프로그래밍
#과제: Assignment4
#작성자: 소프트웨어학부 20201148 이수민
#작성일시: 2025년 6월 25일
#프로그램명: 토익 영단어 퀴즈

import json
import random

# 시작 문구
print("📖 단어 안 외우면 못 나감.zip")
print("졸업을 위해 토익 750점은 필수! 중앙대 소프트학부생이라면 피해갈 수 없다.")
print("이 문을 나가고 싶다면… 단어를 맞춰라! 🧠\n")

# 📚 레벨 선택 안내
print("📚 레벨 안내")
print("1. 초급 (기초/일상 단어: ~600점)")
print("2. 중급 (실전 핵심 단어: 600~800점)")
print("3. 고급 (고난이도 RC 단어: 800점 이상)\n")

level_map = {
    "1": "초급",
    "2": "중급",
    "3": "고급"
}

level_choice = ""

while level_choice not in level_map:
    level_choice = input("레벨을 입력하세요 (1/2/3): ").strip()

level = level_map[level_choice]
print(f"\n🎮 게임 시작! 선택한 레벨: {level}")
print("정답을 입력하세요! (종료: 'q')\n")

# 📂 단어장 로딩
try:
    with open("words.json", "r", encoding="utf-8") as f:
        word_data = json.load(f)[level]
except FileNotFoundError:
    print("❌ 'words.json' 파일이 없습니다. 같은 폴더에 단어장을 넣어주세요.")
    exit()

# 점수와 오답노트 초기화
score = 0
total = 0
wrong_answers = []

# 게임 시작
while True:
    word = random.choice(word_data)
    eng = word["word"]
    kor = word["meaning"]

    answer = input(f"🔤 영어 단어의 뜻은? 👉 {eng}: ").strip()

    if answer.lower() == "q":
        break

    total += 1

    if answer == kor:
        print("✅ 정답입니다!\n")
        score += 1
    else:
        print(f"❌ 오답입니다. 정답: {kor}\n")
        wrong_answers.append({
            "word": eng,
            "your_answer": answer,
            "correct": kor
        })

# 🧾 결과 출력
print("\n🎯 게임 종료!")
print(f"총 점수: {score} / {total}")

if wrong_answers:
    print("\n📝 오답노트:")
    for w in wrong_answers:
        print(f" - {w['word']} : 당신의 답변 → {w['your_answer']} / 정답 → {w['correct']}")
