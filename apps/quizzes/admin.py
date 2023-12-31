import nested_admin
from django.contrib import admin

from .models import (
    Answer,
    Question,
    Quiz,
    QuestionResponse,
    QuizAttempt,
    Theme,
)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)
    empty_value_display = "-пусто-"


class AnswerAdmin(nested_admin.NestedTabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(nested_admin.NestedTabularInline):
    inlines = [AnswerAdmin]
    model = Question
    extra = 0


@admin.register(Quiz)
class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionAdmin]
    autocomplete_fields = ("theme",)
    list_display = ("id", "title", "created")
    empty_value_display = "-пусто-"


class QuestionResponseAdmin(admin.TabularInline):
    model = QuestionResponse


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    inlines = [QuestionResponseAdmin]
    list_display = ("id", "quiz", "created", "is_completed")
    empty_value_display = "-пусто-"
