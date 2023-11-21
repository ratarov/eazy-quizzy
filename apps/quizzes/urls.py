from django.urls import path

from .views import QuizListView

app_name = "quizzes"

urlpatterns = [
    path("", QuizListView.as_view(), name="index"),
]
