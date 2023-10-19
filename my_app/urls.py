from django.urls import path, re_path, include
from my_app.views import questions_views


urlpatterns = [
    path('get-questions/', questions_views.GetQuestionAPIView.as_view()),
    path('check-question/<int:question_id>/<int:answer_id>', questions_views.CheckQuestion.as_view())

]
