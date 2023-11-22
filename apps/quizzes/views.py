from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import (
    HttpResponse,
    HttpRequest,
    HttpResponsePermanentRedirect,
)
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import QuestionResponseForm
from .models import Quiz
from .selectors import (
    get_quizzes_with_user_data,
    get_existing_attempt,
    get_first_unanswered_question,
)
from .services import get_attempt_data, create_quiz_response


class QuizListView(ListView):
    """Представление главной страницы со списком квизов."""

    model = Quiz
    template_name = "quizzes/index.html"
    context_object_name = "quizzes"

    def get_queryset(self) -> QuerySet[Any]:
        return get_quizzes_with_user_data(user=self.request.user)


class QuizDetailView(DetailView):
    """Представление страницы квиза со статистикой."""

    model = Quiz
    template_name = "quizzes/quiz_details.html"

    def get_queryset(self) -> QuerySet[Any]:
        return get_quizzes_with_user_data(user=self.request.user)


class QuizAttemptView(LoginRequiredMixin, View):
    """Представление страницы с ответами на вопросы квиза."""

    template_name = "quizzes/quiz_attempt.html"

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        user = request.user
        quiz = get_object_or_404(Quiz, pk=pk)
        context = get_attempt_data(user=user, quiz=quiz)
        question = context.get("question")
        if question is not None:
            form = QuestionResponseForm(q=question)
            context["form"] = form
        return render(request, "quizzes/quiz_attempt.html", context)

    def post(
        self, request: HttpRequest, pk: int, *args, **kwargs
    ) -> HttpResponsePermanentRedirect:
        user = request.user
        quiz = get_object_or_404(Quiz, pk=pk)
        attempt = get_existing_attempt(user, quiz)
        question = get_first_unanswered_question(attempt)

        answer_form = QuestionResponseForm(q=question, data=request.POST)
        if answer_form.is_valid():
            data = answer_form.cleaned_data
            create_quiz_response(attempt, question, data)
        return redirect("quizzes:quiz_attempt", pk=pk)
