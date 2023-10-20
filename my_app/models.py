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
    image = models.FileField(upload_to='images', blank=True, null=True)
    correct_answer_description = models.TextField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=1000)
    question_id = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    is_correct = models.BooleanField()

    def __str__(self):
        return self.answer


class Statistic(models.Model):
    class CategoryChoices(models.TextChoices):
        EDEMIREM = 'EDEMMIREM'
        BILMIREM = 'BILMIREM'
        SEHVLEREDIREM = 'SEHVLEREDIREM'
        TAMBILIREM = 'TAMBILIREM'
        
        
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='statistics')
    category = models.CharField(max_length=50,choices=CategoryChoices.choices, default=CategoryChoices.EDEMIREM)
    correct_answers = models.PositiveIntegerField()
    incorrect_answers = models.PositiveIntegerField()

    def __str__(self):
        return self.user_id.username