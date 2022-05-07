from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
import random
 
from api.v1.quizzes.serializers import QuestionSerializer,ScoreSerializer,StatisticsSerializer
from web.models import Question,Score,Statistics

from django.contrib.auth.models import User
 
 
@api_view(["GET"])
@permission_classes([AllowAny])
def quizzes(request):
     instances = Question.objects.filter(is_deleted = False)
     context = {"request" : request}
     serializer = QuestionSerializer(instances,many =True,context=context)
     return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def scores(request):
     instances = Score.objects.all()
     context = {"request" : request}
     serializer = ScoreSerializer(instances,many =True,context=context)
     return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def statistics(request,pk):
     if not(User.objects.filter(id = pk)).exists():
          response_data = {
               'status_code' : 6001,
               'message' : 'No such user found!'
          }
          return Response(response_data)
     else:
          if Statistics.objects.filter(user_id = pk).exists():
               instances = Statistics.objects.filter(user_id = pk)    
               context = {"request" : request}
               serializer = StatisticsSerializer(instances,many=True,context=context)
               response_data = {
                    'status_code' : 6000,
                    'data' : serializer.data
               }
               return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def changeStatistics(request,pk):
    try: 
        user = pk
        questions_answered = request.data["questions_answered"]
        correct_answers = request.data["correct_answers"]
        wrong_answers = request.data["wrong_answers"] 
        games_played = request.data["games_played"]
        games_won = request.data["games_won"]
        money_earned = request.data["money_earned"] 
    except:
        response_data = {
            'status_code' : 6001,
            'message' : "There was something wrong while updating your statistics."
        }
        return Response(response_data)

    if not(User.objects.filter(id = user)).exists():
        response_data = {
            'status_code' : 6001,
            'message' : 'No such user found!'
        }        
    else:       
        statistics = Statistics.objects.filter(user = user)
        if statistics.exists():
            old_questions_answered = statistics.values("questions_answered")
            old_correct_answers = statistics.values("correct_answers")
            old_wrong_answers = statistics.values("wrong_answers")
            old_games_played = statistics.values("games_played")
            old_games_won = statistics.values("games_won")           
            old_money_earned = statistics.values("money_earned")
            
            correct_percentage = ((correct_answers + old_correct_answers[0].get("correct_answers")) / (questions_answered + old_questions_answered[0].get("questions_answered")) ) * 100
            win_rate = ((games_won + old_games_won[0].get("games_won")) / (games_played + old_games_played[0].get("games_played"))) * 100

            statistics.update(questions_answered = questions_answered + old_questions_answered[0].get("questions_answered"),
                              correct_answers = correct_answers + old_correct_answers[0].get("correct_answers"),
                              wrong_answers = wrong_answers + old_wrong_answers[0].get("wrong_answers"),
                              correct_percentage = correct_percentage,
                              games_played = games_played + old_games_played[0].get("games_played"),
                              games_won = games_won + old_games_won[0].get("games_won"),
                              win_rate = win_rate,
                              money_earned = money_earned + old_money_earned[0].get("money_earned"))
            response_data = {
                'status_code' : 6000,
                'message' : "Statistics Updated"
            }
        
    return Response(response_data)
