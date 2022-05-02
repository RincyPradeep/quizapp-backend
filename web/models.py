from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=128)
    option_one = models.CharField(max_length=128)
    option_two = models.CharField(max_length=128)
    option_three = models.CharField(max_length=128)
    option_four = models.CharField(max_length=128)
    is_deleted = models.BooleanField(default = False)
 
    def __str__(self):
        return self.question


class Statistics(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    questions_answered = models.IntegerField()
    correct_answeres = models.IntegerField()
    wrong_answeres = models.IntegerField()
    correct_percentage = models.IntegerField()
    games_played = models.IntegerField()
    games_won = models.IntegerField()
    win_rate = models.IntegerField()
    money_earned = models.DecimalField(max_digits=15 ,decimal_places=2)

    class Meta:
        db_table = "web_statistics"
        verbose_name_plural = "statistics"
 
    def __str__(self):
        return self.user
