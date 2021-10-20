from django.db import models

class TestApp(models.Model):
    desc = models.CharField(max_length=100)
    title = models.CharField(max_length=10)


