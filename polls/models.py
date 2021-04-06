import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

# question has question and publication date
# a choice has two fields : the text of the choice and a vote tally. Each choice is associated with a question 
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# this small bit of model code gives Django the means to do several things
    # create a db schema - "Create table" statements 
    # create a python database-access API for accessing Question and Choice objects

#django apps are pluggable - you can use an app in multiple projects. Modular.
