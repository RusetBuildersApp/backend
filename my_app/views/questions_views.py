from rest_framework.views import APIView
from rest_framework.response import Response
from my_app.pagination import QuestionPagination
from my_app.models import Question
from my_app.serializer.question_serializers import QuestionSerializer

class GetQuestionAPIView(APIView, QuestionPagination):
    
    def get(self, request):
        questions = Question.objects.all()
        results = self.paginate_queryset(questions, request, view=self)
        serializer = QuestionSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)