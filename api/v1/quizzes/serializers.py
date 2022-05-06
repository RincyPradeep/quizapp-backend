from rest_framework.serializers import ModelSerializer
 
from web.models import Question,Statistics
from rest_framework import serializers
 
 
class QuestionSerializer(ModelSerializer):
    class Meta:
        fields =("id","question","answer","option_one","option_two","option_three","option_four")
        model = Question


class StatisticsSerializer(ModelSerializer):
    class Meta:
        model = Statistics
        fields =("id","questions_answered","correct_answers","wrong_answers","correct_percentage","games_played","games_won","win_rate","money_earned")
        