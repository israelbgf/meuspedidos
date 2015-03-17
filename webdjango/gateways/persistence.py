from webdjango.models import Evaluation


class EvaluationFormGateway(object):
    def save(self, form):
        evaluation = Evaluation(name=form.name,
                                email=form.email,
                                html_skill=form.html_skill,
                                css_skill=form.css_skill,
                                javascript_skill=form.javascript_skill,
                                python_skill=form.python_skill,
                                django_skill=form.django_skill,
                                ios_skill=form.ios_skill,
                                android_skill=form.android_skill)
        
        evaluation.save()