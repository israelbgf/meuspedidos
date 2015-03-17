from django.db import models


class Evaluation(models.Model):
    email = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    
    html_skill = models.IntegerField(blank=True, null=True)
    css_skill = models.IntegerField(blank=True, null=True)
    javascript_skill = models.IntegerField(blank=True, null=True)
    python_skill = models.IntegerField(blank=True, null=True)
    django_skill = models.IntegerField(blank=True, null=True)
    ios_skill = models.IntegerField(blank=True, null=True)
    android_skill = models.IntegerField(blank=True, null=True)


