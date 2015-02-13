from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context

EMAIL_TEMPLATE_LOOKUP = {
    'FRONTEND': 'email/frontend.html',
    'BACKEND': 'email/backend.html',
    'MOBILE': 'email/mobile.html',
    'NONE': 'email/generic.html',
}


class DjangoEmailGateway(object):


    def send(self, email, templates):
        try:
            self._send_email(email, templates)
        except Exception, e:
            self.handle_exception(e)

    def _send_email(self, email, templates):
        for template in templates:
            subject, from_email, to = 'Obrigado por se candidatar!', 'recruitment@meuspedidos.com', email
            html_content = loader.get_template(EMAIL_TEMPLATE_LOOKUP[template]).render(Context({}))
            msg = EmailMultiAlternatives(subject, '', from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

    def handle_exception(self, e):
        print 'DjangoEmailGateway Error:', e.__class__, e
        raise e
