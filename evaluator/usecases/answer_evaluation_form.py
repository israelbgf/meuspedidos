from re import match

VALID_EMAIL_PATTERN = '[^@]+@[^@]+\.[^@]+'


class EvaluationForm:
    def __init__(self, email="", name="", skills=None):
        self.email = email
        self.name = name
        self.skills = skills if skills else {
            'html': 0,
            'css': 0,
            'python': 0,
            'django': 0,
            'ios': 0,
            'android': 0
        }


class AnswerEvaluationFormUseCase:
    def __init__(self, email_gateway):
        self.errors = []
        self.email_gateway = email_gateway

    def execute(self, form):
        self.validate_contact(form)
        self.validate_skills(form)
        self.email_gateway.send(form.email, self.figures_aptitude(form))

        if self.errors:
            return {'success': False, 'errors': self.errors}
        else:
            return {'success': True, 'errors': self.errors}

    def validate_contact(self, form):
        if not form.name:
            self.errors.append('REQUIRED_NAME')
        if not form.email:
            self.errors.append('REQUIRED_EMAIL')
        if not match(VALID_EMAIL_PATTERN, form.email):
            self.errors.append('INVALID_EMAIL')

    def validate_skills(self, form):
        for skill, level in form.skills.iteritems():
            if level < 0 or level > 10:
                self.errors.append('INVALID_{0}_SKILL'.format(skill.upper()))

    def figures_aptitude(self, form):
        skills = form.skills
        aptitudes = []
        if skills.get('html', 0) >= 7 and skills.get('css', 0) >= 7:
            aptitudes.append('FRONTEND')
        if skills.get('python', 0) >= 7 and skills.get('django', 0) >= 7:
            aptitudes.append('BACKEND')
        if skills.get('android', 0) >= 7 and skills.get('ios', 0) >= 7:
            aptitudes.append('MOBILE')
        return 'NONE' if not aptitudes else aptitudes
