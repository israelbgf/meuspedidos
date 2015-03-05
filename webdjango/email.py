from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context
from webdjango import tasks

EMAIL_TEMPLATE_LOOKUP = {
    'FRONTEND': 'email/frontend.html',
    'BACKEND': 'email/backend.html',
    'MOBILE': 'email/mobile.html',
    'NONE': 'email/generic.html',
}


class BaseEmailGateway(object):

    def send(self, email, templates):
        try:
            self.send_email(email, templates)
        except Exception, e:
            self.handle_exception(e)

    def send_email(self, email, templates):
        raise NotImplementedError

    def handle_exception(self, e):
        print 'DjangoEmailGateway Error:', e.__class__, e
        raise e


class DjangoEmailGateway(BaseEmailGateway):

    def send_email(self, email, templates):
        subject, from_email, to = 'Obrigado por se candidatar!', 'recruitment@meuspedidos.com', email

        for template in templates:
            html_content = loader.get_template(EMAIL_TEMPLATE_LOOKUP[template]).render(Context({}))
            msg = EmailMultiAlternatives(subject, '', from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()


class DjangoAsyncEmailGateway(BaseEmailGateway):

    def send_email(self, email, templates):
        subject, from_email, to = 'Obrigado por se candidatar!', 'recruitment@meuspedidos.com', email

        for template in templates:
            html_content = loader.get_template(EMAIL_TEMPLATE_LOOKUP[template]).render(Context({}))
            tasks.send_email.delay(subject, from_email, [email], html_content)