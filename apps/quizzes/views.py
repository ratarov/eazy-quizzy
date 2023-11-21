from django.views.generic import ListView

from .models import Quiz


class QuizListView(ListView):
    model = Quiz
    template_name = "quizzes/index.html"
