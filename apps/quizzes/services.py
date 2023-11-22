from apps.users.models import CustomUser

from .models import Quiz, QuizAttempt, Question, QuestionResponse
from .selectors import (
    check_existing_attempt,
    create_new_attempt,
    get_existing_attempt_with_data,
    get_first_unanswered_question,
)


def get_attempt_data(user: CustomUser, quiz: Quiz) -> dict:
    """Формирование данных для отправки вопроса или результатов квиза."""
    user_started_quiz = check_existing_attempt(user, quiz)
    if user_started_quiz:
        attempt = get_existing_attempt_with_data(user, quiz)
        number = attempt.total_answered + 1
        total = attempt.total
    else:
        attempt = create_new_attempt(user, quiz)
        number = 1
        total = attempt.quiz.questions.count()

    question = get_first_unanswered_question(attempt)

    if question is None:
        attempt.is_completed = True
        attempt.save()

    return {
        "attempt": attempt,
        "question": question,
        "number": number,
        "total": total,
    }


def create_quiz_response(
    attempt: QuizAttempt, question: Question, data: dict
) -> QuestionResponse:
    """Создание ответа пользователя на вопрос квиза."""
    try:
        answers = list(data.get("answers"))
    except TypeError:
        answers = [data.get("answers")]

    correct_answers = list(question.answers.filter(is_correct=True))
    is_correct = answers == correct_answers

    response = QuestionResponse.objects.create(
        question=question, attempt=attempt, is_correct=is_correct
    )
    response.answers.set(answers)
    return response
