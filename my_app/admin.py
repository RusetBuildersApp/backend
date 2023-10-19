from django.contrib import admin
from my_app.models import User, Answer, Question, Exam, Statistic

# Register your models here.


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['user_id']


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'question_id']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer']
