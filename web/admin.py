from django.contrib import admin
from web.models import Question,Statistics,Score,Category
 
 
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id","category","question","answer"]
 
admin.site.register(Question,QuestionAdmin)


class StatisticsAdmin(admin.ModelAdmin):
    list_display = ["id","user","money_earned"]
 
admin.site.register(Statistics,StatisticsAdmin)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ["id","number","score"]
 
admin.site.register(Score,ScoreAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
 
admin.site.register(Category,CategoryAdmin)