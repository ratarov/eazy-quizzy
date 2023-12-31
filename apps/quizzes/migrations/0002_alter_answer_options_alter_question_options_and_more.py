# Generated by Django 4.2.7 on 2023-11-20 18:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quizzes", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="answer",
            options={
                "default_related_name": "answers",
                "verbose_name": "Вариант ответа",
                "verbose_name_plural": "Варианты ответов",
            },
        ),
        migrations.AlterModelOptions(
            name="question",
            options={
                "default_related_name": "questions",
                "verbose_name": "Вопрос",
                "verbose_name_plural": "Вопросы",
            },
        ),
        migrations.AlterModelOptions(
            name="quiz",
            options={
                "default_related_name": "quizzes",
                "verbose_name": "Квиз",
                "verbose_name_plural": "Квизы",
            },
        ),
    ]
