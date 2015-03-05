from django.db import models


class Evaluation(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    
    html_skill = models.IntegerField()
    css_skill = models.IntegerField()
    javascript_skill = models.IntegerField()
    android_skill = models.IntegerField()
    ios_skill = models.IntegerField()
    django_skill = models.IntegerField()
    python_skill = models.IntegerField()


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