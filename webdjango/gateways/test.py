from django.test import TestCase

from django.core import mail
from django.test.utils import override_settings

from evaluator.usecases.answer_evaluation_form import DataStructure

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
        form = DataStructure(
            name='James',
            email='bond@uk.co',
            html_skill=1,
            css_skill=2,
            javascript_skill=3,
            python_skill=4,
            django_skill=5,
            ios_skill=6,
            android_skill=7
        )
        
        gateway = EvaluationFormGateway()
        gateway.save(form)
        evaluation = Evaluation.objects.get(email='bond@uk.co')
        
        self.assertEqual(evaluation.name, 'James')
        self.assertEqual(evaluation.email, 'bond@uk.co')
        self.assertEqual(evaluation.html_skill, 1)
        self.assertEqual(evaluation.css_skill, 2)
        self.assertEqual(evaluation.javascript_skill, 3)
        self.assertEqual(evaluation.python_skill, 4)
        self.assertEqual(evaluation.django_skill, 5)
        self.assertEqual(evaluation.ios_skill, 6)
        self.assertEqual(evaluation.android_skill, 7)