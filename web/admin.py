from django.contrib import admin
from web.models import Question,Statistics
 
 
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id","question","answer"]
 
admin.site.register(Question,QuestionAdmin)


class StatisticsAdmin(admin.ModelAdmin):
    list_display = ["id","user","money_earned"]
 
admin.site.register(Statistics,StatisticsAdmin)
