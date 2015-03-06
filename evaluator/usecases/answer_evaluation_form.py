from re import match

VALID_EMAIL_PATTERN = '[^@]+@[^@]+\.[^@]+'


class EvaluationForm:
    def __init__(self, name="", email="", skills={}):
        self.name = name
        self.email = email
        self.skills = {
            'html': 0,
            'css': 0,
            'javascript': 0,
            'python': 0,
            'django': 0,
            'ios': 0,
            'android': 0
        }
        self.skills.update(skills)


class AnswerEvaluationFormUseCase:
    def __init__(self, email_gateway, persistence_gateway):
        self.errors = []
        self.email = email_gateway
        self.persistence = persistence_gateway

    def execute(self, form):
        form = self.normalize_input(form)
        self.validate_contact(form)
        self.validate_skills(form)

        if not self.errors:
            self.send_email(form)

        self.persistence.save(form)

        return {'success': not self.errors, 'errors': self.errors}

    def normalize_input(self, form):
        normalized_skills = form.skills.copy()
        for skill, level in form.skills.iteritems():
            normalized_skills[skill] = 0 if level is None else level
        return EvaluationForm(form.name, form.email, normalized_skills)

    def validate_contact(self, form):
        if not form.name:
            self.errors.append('REQUIRED_NAME')
        if not form.email:
            self.errors.append('REQUIRED_EMAIL')
        if not match(VALID_EMAIL_PATTERN, form.email if form.email else ''):
            self.errors.append('INVALID_EMAIL')

    def validate_skills(self, form):
        for skill, level in form.skills.iteritems():
            if level < 0 or level > 10:
                self.errors.append('INVALID_{0}_SKILL'.format(skill.upper()))

    def send_email(self, form):
        try:
            self.email.send(form.email, self.figures_aptitude(form))
        except Exception:
            self.errors.append('EMAIL_SENDING_UNAVAIBLE')

    def figures_aptitude(self, form):
        skills = form.skills
        aptitudes = []
        if skills.get('html', 0) >= 7 and skills.get('css', 0) >= 7:
            aptitudes.append('FRONTEND')
        if skills.get('python', 0) >= 7 and skills.get('django', 0) >= 7:
            aptitudes.append('BACKEND')
        if skills.get('android', 0) >= 7 and skills.get('ios', 0) >= 7:
            aptitudes.append('MOBILE')
        return ['NONE'] if not aptitudes else aptitudes
