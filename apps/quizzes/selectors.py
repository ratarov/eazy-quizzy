from django.db.models import Count, Prefetch, Q, QuerySet

from apps.users.models import CustomUser

from .models import Quiz, QuizAttempt, Question, QuestionResponse


def add_quizzes_user_stats(
    qs: QuerySet[Quiz], user: CustomUser
) -> QuerySet[Quiz]:
    """Добавление статистики пользователя по прохождению квизов."""

    return qs.prefetch_related(
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
    ).annotate(
        attempts_number=Count(
            "attempts", filter=Q(attempts__user=user), distinct=True
        ),
    )


def get_all_quizzes(
    user: CustomUser, theme_id: int | None = None
) -> QuerySet[Quiz]:
    """Получение квизов со статистикой для аутентифицированных юзеров."""
    qs = Quiz.objects.select_related("theme").annotate(
        questions_number=Count(
            "questions", filter=Q(questions__is_active=True), distinct=True
        )
    )
    if theme_id is not None:
        qs = qs.filter(theme_id=theme_id)
    if user.is_authenticated:
        return add_quizzes_user_stats(qs, user)
    return qs


def check_existing_attempt(user: CustomUser, quiz: Quiz) -> bool:
    """Проверка на наличие начатого пользователем прохождения квиза."""
    return QuizAttempt.objects.filter(
        user=user, quiz=quiz, is_completed=False
    ).exists()


def get_existing_attempt_with_data(
    user: CustomUser, quiz: Quiz
) -> QuizAttempt:
    """Получение текущей попытки с аннотацией статистикой."""
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
    """Получение текущей попытки прохождения квиза."""
    return (
        QuizAttempt.objects.filter(user=user, quiz=quiz, is_completed=False)
    ).get()


def create_new_attempt(user: CustomUser, quiz: Quiz) -> QuizAttempt:
    """Создание новой попытки прохождения квиза."""
    return QuizAttempt.objects.create(user=user, quiz=quiz, is_completed=False)


def get_first_unanswered_question(attempt: QuizAttempt) -> Question | None:
    """Получение первого неотвеченного вопроса в текущей попытке."""
    return (
        attempt.quiz.questions.filter(is_active=True)
        .exclude(sent_answers__attempt=attempt)
        .first()
    )


def create_response(
    question: Question, attempt: QuizAttempt, is_correct: bool
) -> QuestionResponse:
    """Создание ответа пользователя на вопрос квиза."""
    return QuestionResponse.objects.create(
        question=question, attempt=attempt, is_correct=is_correct
    )
