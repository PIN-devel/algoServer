from django.db import models

from users.models import User


class Problem(models.Model):
    problem_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProblemSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    submission_result = models.TextField(max_length=100)
