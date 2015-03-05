from webdjango.models import Evaluation


class EvaluationFormGateway(object):

    def save(self, form):
        evaluation = Evaluation(name=form.name,
                                email=form.email,
                                html_skill=form.skills['html'],
                                css_skill=form.skills['css'],
                                javascript_skill=form.skills['javascript'],
                                python_skill=form.skills['python'],
                                django_skill=form.skills['django'],
                                ios_skill=form.skills['ios'],
                                android_skill=form.skills['android'],
        )
        evaluation.save()