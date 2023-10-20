import random
from django.db.models import Prefetch
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from my_app.pagination import QuestionPagination
from my_app.models import Question, Answer
from my_app.serializer.question_serializers import QuestionSerializer



class GetQuestionAPIView(APIView):
    
    def get(self, request):
        all_question_ids = Question.objects.values_list('id', flat=True) #save this data on chace for optimize
        random_question_ids = random.sample(list(all_question_ids), 5)
        random_questions = Question.objects.filter(id__in=random_question_ids)
        # results = self.paginate_queryset(random_questions, request, view=self)
        serializer = QuestionSerializer(random_questions, many=True)
        # return self.get_paginated_response(serializer.data)
        return Response(serializer.data)
    

class CheckQuestion(APIView):
    def get(self, request, question_id, answer_id):
        question_check = Question.objects.filter(id=question_id).prefetch_related(
            Prefetch("answers", queryset=Answer.objects.filter(is_correct=True))
        )
        if question_check.exists():
            question = question_check.first()
            question_description = question.correct_answer_description
            correct_answer_check = False
            for correct in question.answers.all():
                if correct.id == answer_id:
                    correct_answer_check = True
            if correct_answer_check:
                return Response(correct_answer_check, status=status.HTTP_200_OK)
            return Response({"description": question_description, "check": correct_answer_check}, status=status.HTTP_200_OK)
        return Response("Question not found", status=status.HTTP_404_NOT_FOUND)
    


        