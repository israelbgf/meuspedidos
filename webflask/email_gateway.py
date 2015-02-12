from flask import render_template
from flask_mail import Message, Mail

EMAIL_TEMPLATE_LOOKUP = {
    'FRONTEND': 'email/frontend.html',
    'BACKEND': 'email/backend.html',
    'MOBILE': 'email/mobile.html',
    'NONE': 'email/generic.html',
    }


class FlaskEmailGateway(object):


    def __init__(self, mail):
        self.mail = mail

    def send(self, email, templates):

        for template in templates:
            message = Message("Obrigado por se candidatar!",
                              sender="recruitment@meuspedidos.com",
                              recipients=[email])
            message.html = render_template(EMAIL_TEMPLATE_LOOKUP[template])
            self.mail.send(message)
