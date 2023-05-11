from django.db import models

# Create your models here.
class Comment_duruduru(models.Model):
  content = models.TextField()
  create_date = models.DateTimeField()

class Comment_mochamilk(models.Model):
  content = models.TextField()
  create_date = models.DateTimeField()