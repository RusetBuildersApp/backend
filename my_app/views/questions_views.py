import random
from rest_framework.views import APIView
from rest_framework.response import Response
from my_app.pagination import QuestionPagination
from my_app.models import Question
from my_app.serializer.question_serializers import QuestionSerializer

class GetQuestionAPIView(APIView, QuestionPagination):
    
    def get(self, request):
        all_question_ids = Question.objects.values_list('id', flat=True)
        random_question_ids = random.sample(list(all_question_ids), 5)
        random_questions = Question.objects.filter(id__in=random_question_ids)
        results = self.paginate_queryset(random_questions, request, view=self)
        serializer = QuestionSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)