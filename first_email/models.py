from django.db import models
 

 
# Create your models here.
class UserEmail(models.Model):
  Title_choices =( 
    ("1", "Mrs"), 
    ("2", "Mr"), 
    ("3", "Ms"), 
    ("4", "Miss"), 
    ("5", "Dr"), 
) 
  title = models.CharField(max_length=1, choices=Title_choices, default="Mr")
  author = models.CharField(max_length=100)
  body = models.CharField(max_length=1000)
  date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return str(self.title) + " " + str(self.author)