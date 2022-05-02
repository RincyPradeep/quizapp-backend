from rest_framework.serializers import ModelSerializer
 
from web.models import Question
from rest_framework import serializers
 
 
class QuestionSerializer(ModelSerializer):
    class Meta:
        fields =("id","question","answer","option_one","option_two","option_three","option_four")
        model = Question