from rest_framework.serializers import ModelSerializer
 
from web.models import Question,Score,Statistics,Category
from rest_framework import serializers
 
 
class QuestionSerializer(ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        fields =("id","category","question","answer","option_one","option_two","option_three","option_four")
        model = Question

    def get_category(self,instance):
        return instance.category.name


class CategorySerializer(ModelSerializer):
    class Meta:
        fields =("id","name")
        model = Category


class ScoreSerializer(ModelSerializer):
    class Meta:
        fields =("id","number","score")
        model = Score


class StatisticsSerializer(ModelSerializer):
    class Meta:
        model = Statistics
        fields =("id","questions_answered","correct_answers","wrong_answers","correct_percentage","games_played","games_won","win_rate","money_earned")
        