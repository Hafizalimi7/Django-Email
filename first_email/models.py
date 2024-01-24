from django.db import models

# Create your models here.
class UserEmail(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  body = models.CharField(max_length=1000)
  
  def __str__(self):
    return str(self.title) + " " + str(self.author)