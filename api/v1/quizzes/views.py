from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
import random
 
from api.v1.quizzes.serializers import QuestionSerializer
from web.models import Question
 
 
@api_view(["GET"])
def quizzes(request):
     instances = Question.objects.filter(is_deleted = False)
     context = {"request" : request}
     serializer = QuestionSerializer(instances,many =True,context=context)
     return Response(serializer.data)


# @api_view(["GET"])
# def single_question(request):
#      instances = Question.objects.filter(is_deleted = False)
#      print("!!!!!!!",instances)
#      random_index = random.randint(0,len(instances)-1)
#      print("INDEX:",random_index)
#      instance = Question.objects.filter(Q(id = random_index),Q(is_deleted = False))
#      print("@@@@@@@",instance)
#      context = {"request" : request}
#      serializer = QuestionSerializer(instance,context=context)
#      return Response(serializer.data)