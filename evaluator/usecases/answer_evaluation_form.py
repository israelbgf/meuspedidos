from re import match

VALID_EMAIL_PATTERN = '[^@]+@[^@]+\.[^@]+'


class DataStructure(object):
    def __init__(self, **values):
        for field_name, field_value in values.iteritems():
            setattr(self, field_name, field_value)
            
    def __getattr__(self, name):
        return None


class AnswerEvaluationFormUseCase:
    def __init__(self, email_gateway, persistence_gateway):
        self.errors = []
        self.email = email_gateway
        self.persistence = persistence_gateway

    def execute(self, request_model):
        evaluation_form = self.build_valid_model(request_model)

        if not self.errors:
            self.send_email(evaluation_form)
            self.persistence.save(evaluation_form)

        return self.create_response()

    def build_valid_model(self, request):
        return DataStructure(
            name=self.parse_name(request.name),
            email=self.parse_email(request.email),
            html_skill=self.parse_skill(request.html_skill, 'HTML'),
            css_skill=self.parse_skill(request.css_skill, 'CSS'),
            javascript_skill=self.parse_skill(request.javascript_skill, 'JAVASCRIPT'),
            python_skill=self.parse_skill(request.python_skill, 'PYTHON'),
            django_skill=self.parse_skill(request.django_skill, 'DJANGO'),
            ios_skill=self.parse_skill(request.ios_skill, 'IOS'),
            android_skill=self.parse_skill(request.android_skill, 'ANDROID')
        )

    def parse_name(self, value):
        if not value:
            self.errors.append('REQUIRED_NAME')
        return value

    def parse_email(self, value):
        if not value:
            self.errors.append('REQUIRED_EMAIL')
        elif not match(VALID_EMAIL_PATTERN, value if value else ''):
            self.errors.append('INVALID_EMAIL')
        return value
        
    def parse_skill(self, value, skill_name):
        try:
            skill = int(value if value else 0)
        except ValueError:
            self.errors.append('INVALID_{0}_SKILL'.format(skill_name))
            return
        
        if skill < 0 or skill > 10:
            self.errors.append('INVALID_{0}_SKILL'.format(skill_name))
        return skill

    def send_email(self, form):
        try:
            self.email.send(form.email, self.figures_aptitude(form))
        except Exception:
            self.errors.append('EMAIL_SENDING_UNAVAIBLE')

    def figures_aptitude(self, form):
        aptitudes = []
        if form.html_skill >= 7 and form.css_skill >= 7 and form.javascript_skill >= 7:
            aptitudes.append('FRONTEND')
        if form.python_skill >= 7 and form.django_skill >= 7:
            aptitudes.append('BACKEND')
        if form.android_skill >= 7 or form.ios_skill >= 7:
            aptitudes.append('MOBILE')
        return ['NONE'] if not aptitudes else aptitudes

    def create_response(self):
        return {'success': not self.errors, 'errors': self.errors}