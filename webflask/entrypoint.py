import flask
from flask import Flask
from flask import render_template
from flask import request
from flask_mail import Mail

from email import FlaskEmailGateway
from config import FLASK_CONFIGURATION

from parsers import SafeForm
from evaluator.usecases.answer_evaluation_form import AnswerEvaluationFormUseCase
from evaluator.usecases.answer_evaluation_form import EvaluationForm


app = Flask(__name__)
app.config.update(FLASK_CONFIGURATION)
mail = Mail(app)


@app.route("/")
def index():
    return render_template('index.html', delivery_mechanism='Flask')


@app.route("/api/recruitment", methods=['POST'])
def recruitment():
    form = SafeForm(request.form)
    
    evaluation_form = EvaluationForm(form.str('name'), form.str('email'), skills={
        'html': form.int('html'),
        'css': form.int('css'),
        'javascript': form.int('javascript'),
        'python': form.int('python'),
        'django': form.int('django'),
        'android': form.int('android'),
        'ios': form.int('ios'),
    })
    response = AnswerEvaluationFormUseCase(FlaskEmailGateway(mail)).execute(evaluation_form)
    return flask.jsonify(**response)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404