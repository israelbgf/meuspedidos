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


