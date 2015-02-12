import flask
from flask import Flask
from flask import render_template
from flask import request
from flask_mail import Mail

from email_gateway import FlaskEmailGateway
from config import FLASK_CONFIGURATION

from request_parsers import safe_int
from evaluator.usecases.answer_evaluation_form import AnswerEvaluationFormUseCase
from evaluator.usecases.answer_evaluation_form import EvaluationForm


app = Flask(__name__)
app.config.update(FLASK_CONFIGURATION)
mail = Mail(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/recruitment", methods=['POST'])
def recruitment():
    form = EvaluationForm(request.form['name'], request.form['email'], skills={
        'html': safe_int(request.form['html']),
        'css': safe_int(request.form['css']),
        'javascript': safe_int(request.form['javascript']),
        'python': safe_int(request.form['python']),
        'django': safe_int(request.form['django']),
        'android': safe_int(request.form['android']),
        'ios': safe_int(request.form['ios']),
    })
    response = AnswerEvaluationFormUseCase(FlaskEmailGateway(mail)).execute(form)
    return flask.jsonify(**response)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404