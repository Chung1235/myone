import os
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

questions = [
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": ["m"]},
    {"question": "The more you take, the more you leave behind. What am I?", "answer": ["footsteps","footstep"]},
    {"question": "What has keys but can't open locks?", "answer": ["piano", "keyboard"]},
    {"question": "What word is spelled incorrectly in every dictionary?", "answer": ["incorrectly"]},
    {"question": "What is always coming, but never arrives?", "answer": ["tomorrow"]},
    {"question": "What is it that if you have, you want to share me, and if you share, you do not have?", "answer": ["secret","secrets"]},
    {"question": "What is it that goes up, but never comes down?", "answer": ["age","ages"]},
    {"question": "What has hands but doesn't clap?", "answer": ["clock", "watch"]},
    {"question": "What begins with an E but only has one letter?", "answer": ["envelope","email"]},
    {"question": "What can you catch but not throw?", "answer": ["cold"]}
]
random.shuffle(questions)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_question', methods=['GET'])
def get_question():
    return jsonify(questions)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
