from django.test import TestCase

from django.core import mail
from django.test.utils import override_settings

from evaluator.usecases.answer_evaluation_form import EvaluationForm

from webdjango.gateways.email import *
from webdjango.models import Evaluation
from webdjango.gateways.persistence import EvaluationFormGateway


class EmailGateway(TestCase):
    def setUp(self):
        self.to_email = 'juca@dev.com'
        self.templates = ['FRONTEND', 'BACKEND', 'MOBILE', 'NONE']

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True)
    def test_async_gateway(self):
        gateway = DjangoAsyncEmailGateway()
        gateway.send(self.to_email, self.templates)
        self.assertEqual(len(mail.outbox), 4)

    def test_sync_gateway(self):
        gateway = DjangoSyncEmailGateway()
        gateway.send(self.to_email, self.templates)
        self.assertEqual(len(mail.outbox), 4)


class PersistenceGateway(TestCase):
    def test_persistence(self):
        form = EvaluationForm('User', 'user@provider.com')
        gateway = EvaluationFormGateway()
        gateway.save(form)
        self.assertIsNotNone(Evaluation.objects.get(email='user@provider.com'))

    def test_persistence_with_null_values(self):
        form = EvaluationForm('User', 'user@provider.com', skills={'android': 10})
        gateway = EvaluationFormGateway()
        gateway.save(form)
        self.assertIsNotNone(Evaluation.objects.get(email='user@provider.com'))