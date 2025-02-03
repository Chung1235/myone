from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

questions = [
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "m"},
    {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"},
    {"question": "What has keys but can't open locks?", "answer": "piano"},
    {"question": "What word is spelled incorrectly in every dictionary?", "answer": "incorrectly"},
    {"question": "What is always coming, but never arrives?", "answer": "tomorrow"},
    {"question": "What is it that if you have, you want to share me, and if you share, you do not have?", "answer": "secret"},
    {"question": "What is it that goes up, but never comes down?", "answer": "age"},
    {"question": "What has hands but doesn't clap?", "answer": "clock"},
    {"question": "What begins with an E but only has one letter?", "answer": "envelope"},
    {"question": "What can you catch but not throw?", "answer": "cold"}
]
random.shuffle(questions)

@app.route('/')
def index():
    return render_template('game.html')  # game.html로 수정 (템플릿 이름)

@app.route('/get_question', methods=['GET'])
def get_question():
    return jsonify(questions)

# Vercel 환경에서는 app.run()을 사용하지 않음
if __name__ == '__main__':
    app.run(debug=True)  # 이 줄은 Vercel에서는 불필요함
