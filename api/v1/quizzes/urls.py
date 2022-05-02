from django.urls import path
from api.v1.quizzes import views
 
 
urlpatterns = [
    path('',views.quizzes),
    # path('single_question/',views.single_question),
]
