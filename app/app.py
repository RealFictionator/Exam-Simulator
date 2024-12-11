import os
import random
#import webbrowser
#from threading import Timer
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

# Liste der Frage-IDs (z.B. von 1 bis zur Anzahl der verfügbaren Fragen)
questions = list(range(1, 101))  # Beispiel mit 100 Fragen
random.shuffle(questions)

@app.route('/')
def index():
    return redirect(url_for('show_question', question_idx=0))

@app.route('/question/<int:question_idx>')
def show_question(question_idx):
    if question_idx >= len(questions):
        return redirect(url_for('index'))  # Zurück zur ersten Frage, wenn alle durch sind
    
    question_num = questions[question_idx]
    question_image_path = f'static/Exam-Topics/questions/question_{question_num}.png'
    answer_image_path = f'static/Exam-Topics/answers/answer_{question_num}.png'

    if not os.path.exists(question_image_path):
        # Wenn das Bild nicht existiert, zur nächsten Frage weiterleiten
        return redirect(url_for('show_question', question_idx=question_idx + 1))

    question_image = url_for('static', filename=f'Exam-Topics/questions/question_{question_num}.png')
    answer_image = url_for('static', filename=f'Exam-Topics/answers/answer_{question_num}.png')
    return render_template('index.html', question_num=question_num, question_image=question_image, answer_image=answer_image, question_idx=question_idx)

@app.route('/delete_question/<int:question_idx>')
def delete_question(question_idx):
    if question_idx >= len(questions):
        return redirect(url_for('index'))  # Zurück zur ersten Frage, wenn alle durch sind
    
    question_num = questions[question_idx]
    question_image_path = f'static/Exam-Topics/questions/question_{question_num}.png'
    answer_image_path = f'static/Exam-Topics/answers/answer_{question_num}.png'

    if os.path.exists(question_image_path):
        os.remove(question_image_path)
    if os.path.exists(answer_image_path):
        os.remove(answer_image_path)

    return redirect(url_for('show_question', question_idx=question_idx + 1))

#def open_browser():
    #webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    #Timer(1, open_browser).start()
    app.run(host='0.0.0.0', port=8000,debug=True)
