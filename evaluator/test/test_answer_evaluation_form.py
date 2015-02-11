import unittest
from usecases.answer_evaluation_form import AnswerEvaluationFormUseCase, EvaluationForm


class EmailGatewaySpy(object):
    def send(self, email, templates):
        self.email = email
        self.templates = templates


class TestEvaluationFormValidation(unittest.TestCase):
    def setUp(self):
        self.use_case = AnswerEvaluationFormUseCase(EmailGatewaySpy())

    def test_answer_form_with_blank_name(self):
        response = self.use_case.execute(EvaluationForm())
        self.assertFalse(response['success'])
        self.assertIn("REQUIRED_NAME", response['errors'])

    def test_answer_form_with_blank_email(self):
        response = self.use_case.execute(EvaluationForm())
        self.assertFalse(response['success'])
        self.assertIn("REQUIRED_EMAIL", response['errors'])

    def test_answer_form_with_invalid_email(self):
        response = self.use_case.execute(EvaluationForm(email='bla@'))
        self.assertFalse(response['success'])
        self.assertIn("INVALID_EMAIL", response['errors'])

    def test_valid_answer_form(self):
        response = self.use_case.execute(EvaluationForm(name='Israel', email='israel@email.com'))
        self.assertTrue(response['success'])
        self.assertFalse(response['errors'])

    def test_answer_form_with_html_skill_negative(self):
        response = self.use_case.execute(EvaluationForm(skills={'html': -1}))
        self.assertFalse(response['success'])
        self.assertIn("INVALID_HTML_SKILL", response['errors'])

    def test_answer_form_with_android_skill_over_10(self):
        response = self.use_case.execute(EvaluationForm(skills={'android': 11}))
        self.assertFalse(response['success'])
        self.assertIn("INVALID_ANDROID_SKILL", response['errors'])

    def test_answer_form_with_valid_ios_skill(self):
        response = self.use_case.execute(EvaluationForm(skills={'ios': 5}))
        self.assertFalse(response['success'])
        self.assertNotIn("INVALID_IOS_SKILL", response['errors'])
        

class TestEmailSendingWithCorrespondingAptitude(unittest.TestCase):
    def setUp(self):
        self.email_gateway = EmailGatewaySpy()
        self.use_case = AnswerEvaluationFormUseCase(self.email_gateway)
        self.form = EvaluationForm()
        self.form.name = "Solid Snake"
        self.form.email = "snake@outerheaven.com"

    def test_sent_email_for_frontend_aptitude(self):
        self.form.skills['html'] = 10
        self.form.skills['css'] = 10
        self.form.skills['javascript'] = 10
        
        response = self.use_case.execute(self.form)

        self.assertIn('FRONTEND', self.email_gateway.templates)
        self.assertEqual(self.email_gateway.email, "snake@outerheaven.com")
        self.assertTrue(response['success'])

    def test_sent_email_for_backend_aptitude(self):
        self.form.skills['python'] = 10
        self.form.skills['django'] = 10

        response = self.use_case.execute(self.form)

        self.assertIn('BACKEND', self.email_gateway.templates)
        self.assertEqual(self.email_gateway.email, "snake@outerheaven.com")
        self.assertTrue(response['success'])

    def test_sent_email_for_mobile_aptitude(self):
        self.form.skills['ios'] = 10
        self.form.skills['android'] = 10

        response = self.use_case.execute(self.form)

        self.assertIn('MOBILE', self.email_gateway.templates)
        self.assertEqual(self.email_gateway.email, "snake@outerheaven.com")
        self.assertTrue(response['success'])

    def test_sent_email_for_all_aptitude(self):
        self.form.skills['html'] = 10
        self.form.skills['css'] = 10
        self.form.skills['javascript'] = 10
        self.form.skills['python'] = 10
        self.form.skills['django'] = 10
        self.form.skills['ios'] = 10
        self.form.skills['android'] = 10

        response = self.use_case.execute(self.form)

        self.assertIn('FRONTEND', self.email_gateway.templates)
        self.assertIn('BACKEND', self.email_gateway.templates)
        self.assertIn('MOBILE', self.email_gateway.templates)
        self.assertEqual(self.email_gateway.email, "snake@outerheaven.com")
        self.assertTrue(response['success'])

    def test_sent_email_for_none_aptitude(self):
        response = self.use_case.execute(self.form)

        self.assertIn('NONE', self.email_gateway.templates)
        self.assertEqual(self.email_gateway.email, "snake@outerheaven.com")
        self.assertTrue(response['success'])