from django.urls import path
from api.v1.quizzes import views
 
 
urlpatterns = [
    path('',views.quizzes),
    path('statistics/<int:pk>/',views.statistics),
    path('change-statistics/<int:pk>/',views.changeStatistics),
]
