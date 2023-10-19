from django.urls import path, re_path, include
from my_app.views import questions_views


urlpatterns = [
    path('get-questions/', questions_views.GetQuestionAPIView.as_view())

]
