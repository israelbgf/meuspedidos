from webdjango.models import Evaluation


class EvaluationFormGateway(object):

    def save(self, form):
        evaluation = Evaluation(name=form.name,
                                email=form.email,
                                html_skill=form.skills.get('html'),
                                css_skill=form.skills.get('css'),
                                javascript_skill=form.skills.get('javascript'),
                                python_skill=form.skills.get('python'),
                                django_skill=form.skills.get('django'),
                                ios_skill=form.skills.get('ios'),
                                android_skill=form.skills.get('android')
        )
        evaluation.save()