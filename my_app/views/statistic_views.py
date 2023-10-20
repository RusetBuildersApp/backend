from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F, Case, When, Value, CharField, FloatField, ExpressionWrapper, Count
from django.db.models.functions import Cast
from my_app.models import Statistic, Question


class GetUserStatistic(APIView):
    def get(self, request):
        questions_count = Question.objects.aggregate(questions_count=Count('id'))
        print(questions_count)
        statistic = Statistic.objects.values('category').annotate(count=Count('category')/questions_count['questions_count'])
        return Response(statistic)
    
