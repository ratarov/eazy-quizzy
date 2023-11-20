from django.db import models

from apps.users.models import CustomUser


class BaseModel(models.Model):
    """Базовая модель для отслеживания изменений и обновлений."""

    created = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        abstract = True


class Theme(models.Model):
    """Модель Темы для тестов."""

    title = models.CharField(verbose_name="Название темы", max_length=50)

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self):
        return self.title


class Quiz(BaseModel):
    """Модель Теста-Квиза."""

    title = models.CharField(verbose_name="Название теста", max_length=50)
    theme = models.ManyToManyField(Theme, verbose_name="Темы квиза")

    class Meta:
        verbose_name = "Квиз"
        verbose_name_plural = "Квизы"
        default_related_name = "quizzes"

    def __str__(self):
        return self.title


class Question(BaseModel):
    """Модель Вопросов."""

    class QuestionType(models.TextChoices):
        SINGLE = "s", "один верный ответ"
        MULTI = "m", "несколько вреных ответов"

    text = models.TextField(verbose_name="Текст вопроса", max_length=500)
    q_type = models.CharField(
        verbose_name="Кол-во верных ответов",
        max_length=1,
        choices=QuestionType.choices,
        default=QuestionType.SINGLE,
    )
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, verbose_name="Тест"
    )
    is_active = models.BooleanField(verbose_name="Активен", default=True)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        default_related_name = "questions"

    def __str__(self):
        return f"Тест {self.quiz}, вопрос: {self.text[:10]}"


class Answer(BaseModel):
    """Модель Вариантов Ответов на вопросы."""

    text = models.CharField(verbose_name="Ответ", max_length=50)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="Вопрос"
    )
    is_correct = models.BooleanField(verbose_name="Верный", default=False)

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответов"
        default_related_name = "answers"

    def __str__(self):
        return self.text


class QuizAttempt(BaseModel):
    """Модель Попытки прохождения Квиза пользователем."""

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, verbose_name="Квиз"
    )
    is_completed = models.BooleanField(
        verbose_name="Квиз завершен", default=False
    )

    class Meta:
        verbose_name = "Прохождение теста"
        verbose_name_plural = "Прохождения тестов"
        default_related_name = "attempts"
        constraints = []  # только 1 активное прохождение

    def __str__(self):
        return f"{self.created}: Попытка {self.user} пройти {self.quiz}"


class QuestionResponse(BaseModel):
    """Модель отправленного Ответа на вопрос в рамках Квиза."""

    attempt = models.ForeignKey(
        QuizAttempt,
        on_delete=models.CASCADE,
        verbose_name="Попытка прохождения",
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="Вопрос"
    )
    answer = models.ManyToManyField(Answer, verbose_name="Выбранные ответы")
    is_correct = models.BooleanField(verbose_name="Ответ дан верно")

    class Meta:
        verbose_name = "Прохождение теста"
        verbose_name_plural = "Прохождения тестов"
        default_related_name = "sent_answers"

    def __str__(self):
        return f"{self.created}: Попытка {self.user} пройти {self.quiz}"
