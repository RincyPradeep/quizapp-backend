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
    questions_answered = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    wrong_answers = models.IntegerField(default=0)
    correct_percentage = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    games_won = models.IntegerField(default=0)
    win_rate = models.IntegerField(default=0)
    money_earned = models.DecimalField(default=0, max_digits=15 ,decimal_places=2)

    class Meta:
        db_table = "web_statistics"
        verbose_name_plural = "statistics"
 
    def __str__(self):
        return str(self.id)


class Score(models.Model):
    number = models.IntegerField()
    score = models.BigIntegerField()

    def __str__(self):
        return str(self.number)
