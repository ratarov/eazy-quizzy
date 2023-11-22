from django.db.models import Count, Prefetch, Q, QuerySet

from apps.users.models import CustomUser

from .models import Quiz, QuizAttempt, Question, QuestionResponse


def get_quizzes_with_user_data(user: CustomUser) -> QuerySet[Quiz]:
    return (
        Quiz.objects.select_related("theme")
        .prefetch_related(
            Prefetch(
                lookup="attempts",
                queryset=QuizAttempt.objects.filter(user=user).annotate(
                    right=Count(
                        "sent_answers",
                        filter=Q(sent_answers__is_correct=True),
                    ),
                    total_answered=Count("sent_answers", distinct=True),
                ),
            ),
        )
        .annotate(
            questions_number=Count(
                "questions", filter=Q(questions__is_active=True), distinct=True
            )
        )
    )


def check_existing_attempt(user: CustomUser, quiz: Quiz) -> bool:
    return QuizAttempt.objects.filter(
        user=user, quiz=quiz, is_completed=False
    ).exists()


def get_existing_attempt_with_data(
    user: CustomUser, quiz: Quiz
) -> QuizAttempt:
    return (
        QuizAttempt.objects.filter(user=user, quiz=quiz, is_completed=False)
        .annotate(
            right=Count(
                "sent_answers",
                filter=Q(sent_answers__is_correct=True),
                distinct=True,
            ),
            total_answered=Count("sent_answers", distinct=True),
        )
        .annotate(
            total=Count(
                "quiz__questions",
                filter=Q(quiz__questions__is_active=True),
                distinct=True,
            )
        )
    ).get()


def get_existing_attempt(user: CustomUser, quiz: Quiz) -> QuizAttempt:
    return (
        QuizAttempt.objects.filter(user=user, quiz=quiz, is_completed=False)
    ).get()


def create_new_attempt(user: CustomUser, quiz: Quiz) -> QuizAttempt:
    return QuizAttempt.objects.create(user=user, quiz=quiz, is_completed=False)


def get_first_unanswered_question(attempt: QuizAttempt) -> Question | None:
    return (
        attempt.quiz.questions.filter(is_active=True)
        .exclude(sent_answers__attempt=attempt)
        .first()
    )


def create_response(
    question: Question, attempt: QuizAttempt, is_correct: bool
) -> QuestionResponse:
    return QuestionResponse.objects.create(
        question=question, attempt=attempt, is_correct=is_correct
    )
