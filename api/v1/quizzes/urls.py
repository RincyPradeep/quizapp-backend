from django.urls import path
from api.v1.quizzes import views
 
 
urlpatterns = [
    path('categories/',views.categories),
    path('category/<int:pk>/',views.category),
    path('scores/',views.scores),
    path('statistics/<int:pk>/',views.statistics),
    path('change-statistics/<int:pk>/',views.changeStatistics),
]
