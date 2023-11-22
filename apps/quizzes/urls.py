from django.urls import path

from .views import QuizListView, QuizAttemptView, QuizDetailView

app_name = "quizzes"

urlpatterns = [
    path("", QuizListView.as_view(), name="index"),
    path(
        "quizzes/<int:pk>/attempt/",
        QuizAttemptView.as_view(),
        name="quiz_attempt",
    ),
    path("quizzes/<int:pk>/", QuizDetailView.as_view(), name="quiz_details"),
]
