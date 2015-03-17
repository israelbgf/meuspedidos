import unittest
from evaluator.usecases.answer_evaluation_form import AnswerEvaluationFormUseCase, DataStructure


class PersistenceGatewaySpy(object):
    
    def __init__(self):
        self.form = None
        self.called = False
    
    def save(self, form):
        self.form = form
        self.called = True


class EmailGatewaySpy(object):

    def __init__(self):
        self.email = None
        self.templates = None
        self.called = False

    def send(self, email, templates):
        self.email = email
        self.templates = templates
        self.called = True


class AlwaysFailingEmailGateway(object):
    
    def execute(self, *parameters):
        raise Exception('Some nasty problem')


class TestEvaluationFormValidation(unittest.TestCase):
    def setUp(self):
        self.email_gateway = EmailGatewaySpy()
        self.persistence_gateway = PersistenceGatewaySpy()
        self.use_case = AnswerEvaluationFormUseCase(self.email_gateway, self.persistence_gateway)

    def test_answer_form_with_blank_name(self):
        response = self.use_case.execute(DataStructure())
        self.assertValidationFailed(response)
        self.assertIn("REQUIRED_NAME", response['errors'])

    def test_answer_form_with_blank_email(self):
        response = self.use_case.execute(DataStructure())
        self.assertValidationFailed(response)
        self.assertNotIn("INVALID_EMAIL", response['errors'])
        self.assertIn("REQUIRED_EMAIL", response['errors'])

    def test_answer_form_with_invalid_email(self):
        response = self.use_case.execute(DataStructure(email='bla@'))
        self.assertValidationFailed(response)
        self.assertIn("INVALID_EMAIL", response['errors'])

    def test_answer_form_with_none_email(self):
        response = self.use_case.execute(DataStructure(email=None))
        self.assertValidationFailed(response)
        self.assertIn("REQUIRED_EMAIL", response['errors'])

    def test_answer_form_with_html_skill_undefined(self):
        response = self.use_case.execute(DataStructure(name='Israel', email='israel@email.com', html_skill=None))
        self.assertTrue(response['success'])
        self.assertNotIn("INVALID_HTML_SKILL", response['errors'])

    def test_answer_form_with_html_skill_invalid(self):
        response = self.use_case.execute(DataStructure(name='Israel', email='israel@email.com', html_skill='A'))
        self.assertFalse(response['success'])
        self.assertIn("INVALID_HTML_SKILL", response['errors'])

    def test_answer_form_with_html_skill_negative(self):
        response = self.use_case.execute(DataStructure(html_skill=-1))
        self.assertValidationFailed(response)
        self.assertIn("INVALID_HTML_SKILL", response['errors'])

    def test_answer_form_with_android_skill_over_10(self):
        response = self.use_case.execute(DataStructure(android_skill=11))
        self.assertValidationFailed(response)
        self.assertIn("INVALID_ANDROID_SKILL", response['errors'])

    def test_answer_form_with_valid_ios_skill(self):
        response = self.use_case.execute(DataStructure(ios_skill=5))
        self.assertValidationFailed(response)
        self.assertNotIn("INVALID_IOS_SKILL", response['errors'])
        
    def test_valid_answer_form(self):
        response = self.use_case.execute(DataStructure(name='Israel', email='israel@email.com'))
        self.assertEqual(len(response['errors']), 0)
        self.assertTrue(response['success'])

    def assertValidationFailed(self, response):
        self.assertFalse(response['success'])
        self.assertFalse(self.email_gateway.called)
        self.assertFalse(self.persistence_gateway.called)


class TestEmailSending(unittest.TestCase):
    def setUp(self):
        self.email_gateway = EmailGatewaySpy()
        self.use_case = AnswerEvaluationFormUseCase(self.email_gateway, PersistenceGatewaySpy())
        self.form = DataStructure()
        self.form.name = "Solid Snake"
        self.form.email = "snake@outerheaven.com"

    def test_gracefully_email_error_handling(self):
        email_gateway = AlwaysFailingEmailGateway()
        use_case = AnswerEvaluationFormUseCase(email_gateway, PersistenceGatewaySpy())
        response = use_case.execute(self.form)

        self.assertIn('EMAIL_SENDING_UNAVAIBLE', response['errors'])
        self.assertFalse(response['success'])

    def test_sent_email_for_frontend_aptitude(self):
        self.form.html_skill = 10
        self.form.css_skill = 10
        self.form.javascript_skill = 10

        response = self.use_case.execute(self.form)

        self.assertEqual(['FRONTEND'], self.email_gateway.templates)
        self.assertEmailSending(response)

    def test_sent_email_for_backend_aptitude(self):
        self.form.python_skill = 10
        self.form.django_skill = 10

        response = self.use_case.execute(self.form)

        self.assertEqual(['BACKEND'], self.email_gateway.templates)
        self.assertEmailSending(response)

    def test_sent_email_for_mobile_aptitude(self):
        self.form.ios_skill = 10
        self.form.android_skill = 10

        response = self.use_case.execute(self.form)

        self.assertEqual(['MOBILE'], self.email_gateway.templates)
        self.assertEmailSending(response)

    def test_sent_email_for_all_aptitude(self):
        self.form.html_skill = 10
        self.form.css_skill = 10
        self.form.javascript_skill = 10
        self.form.python_skill = 10
        self.form.django_skill = 10
        self.form.ios_skill = 10
        self.form.android_skill = 10

        response = self.use_case.execute(self.form)

        self.assertEqual(3, len(self.email_gateway.templates))
        self.assertIn('FRONTEND', self.email_gateway.templates)
        self.assertIn('BACKEND', self.email_gateway.templates)
        self.assertIn('MOBILE', self.email_gateway.templates)
        self.assertEmailSending(response)

    def test_sent_email_for_none_aptitude(self):
        response = self.use_case.execute(self.form)

        self.assertEqual(1, len(self.email_gateway.templates))
        self.assertEqual(['NONE'], self.email_gateway.templates)
        self.assertEmailSending(response)

    def assertEmailSending(self, response):
        self.assertEqual(self.email_gateway.email, "snake@outerheaven.com")
        self.assertTrue(response['success'])


class TestPersistence(unittest.TestCase):
    def setUp(self):
        self.persistence_gateway = PersistenceGatewaySpy()
        self.use_case = AnswerEvaluationFormUseCase(EmailGatewaySpy(), self.persistence_gateway)
        self.form = DataStructure()
        self.form.name = "Solid Snake"
        self.form.email = "snake@outerheaven.com"

    def test_persistence(self):
        self.use_case.execute(self.form)
        self.assertIsNotNone(self.persistence_gateway.form)