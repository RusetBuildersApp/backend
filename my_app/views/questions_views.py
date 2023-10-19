import random
from django.db.models import Prefetch
from rest_framework.views import APIView
from rest_framework.response import Response
from my_app.pagination import QuestionPagination
from my_app.models import Question, Answer
from my_app.serializer.question_serializers import QuestionSerializer

class GetQuestionAPIView(APIView):
    
    def get(self, request):
        all_question_ids = Question.objects.values_list('id', flat=True)
        random_question_ids = random.sample(list(all_question_ids), 5)
        random_questions = Question.objects.filter(id__in=random_question_ids)
        # results = self.paginate_queryset(random_questions, request, view=self)
        serializer = QuestionSerializer(random_questions, many=True)
        # return self.get_paginated_response(serializer.data)
        return Response(serializer.data)
    

class CheckQuestion(APIView):
    def get(self, request, question_id, answer_id):
        question = Question.objects.filter(id=1).prefetch_related(
            Prefetch("answers", queryset=Answer.objects.filter(is_correct=True))
        ).first()
        correct_answer_id = None
        for correct in question.answers.all():
            correct_answer_id = correct.id
        return Response(correct_answer_id == answer_id)