from flask import Flask, render_template, redirect, url_for, session, request, flash
from surverys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

responses = []

@app.route('/')
def start_page():
    return render_template('start.html', survey=satisfaction_survey)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/questions/<int:qid>')
def question_page(qid):
    if qid != len(responses):
        flash("Invalid question ID.")
        return redirect(url_for('question_page', qid=len(responses)))
    
    if qid >= len(satisfaction_survey.questions):
        return redirect(url_for('thank_you'))
    
    question = satisfaction_survey.questions[qid]
    return render_template('question.html', question_num=qid, question=question)

@app.route('/answer', methods=["POST"])
def answer():
    answer = request.form['answer']
    qid = int(request.form['qid'])

    if qid != len(responses):
        flash("Invalid question ID.")
        return redirect(url_for('question_page', qid=len(responses)))
    
    responses.append(answer)

    if len(responses) >= len(satisfaction_survey.questions):
        return redirect(url_for('thank_you'))
    else:
        return redirect(url_for('question_page', qid=len(responses)))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/', methods=["GET", "POST"])
def start_page():
    if request.method == "POST":
        session['responses'] = []
        return redirect(url_for('question_page', qid=0))
    return render_template('start.html', survey=satisfaction_survey)

@app.route('/questions/<int:qid>')
def question_page(qid):
    responses = session.get('responses', [])
    if qid != len(responses):
        flash("Invalid question ID.")
        return redirect(url_for('question_page', qid=len(responses)))
    
    if qid >= len(satisfaction_survey.questions):
        return redirect(url_for('thank_you'))
    
    question = satisfaction_survey.questions[qid]
    return render_template('question.html', question_num=qid, question=question)

@app.route('/answer', methods=["POST"])
def answer():
    responses = session.get('responses', [])
    answer = request.form['answer']
    qid = int(request.form['qid'])

    if qid != len(responses):
        flash("Invalid question ID.")
        return redirect(url_for('question_page', qid=len(responses)))
    
    responses.append(answer)
    session['responses'] = responses

    if len(responses) >= len(satisfaction_survey.questions):
        return redirect(url_for('thank_you'))
    else:
        return redirect(url_for('question_page', qid=len(responses)))