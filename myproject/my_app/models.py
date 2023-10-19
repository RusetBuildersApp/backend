from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Exam(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    correct_answers = models.PositiveIntegerField()
    incorrect_answers = models.PositiveIntegerField()

    def __str__(self):
        return self.user_id


class Question(models.Model):

    question = models.CharField(max_length=1000)
    image = models.FileField(upload_to='images', blank=True)

    def __str__(self):
        return self.question


class Answer(models.Model):

    answer = models.CharField(max_length=1000)
    question_id = models.ForeignKey(
        Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.answer


class Statistic(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.IntegerField()
    category = models.CharField(max_length=50)
    correct_answers = models.PositiveIntegerField()
    incorrect_answers = models.PositiveIntegerField()

    def __str__(self):
        return self.user_id, self.question_id
