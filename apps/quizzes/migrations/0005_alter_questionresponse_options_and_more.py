# Generated by Django 4.2.7 on 2023-11-22 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("quizzes", "0004_rename_answer_questionresponse_answers"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="questionresponse",
            options={
                "default_related_name": "sent_answers",
                "verbose_name": "Отправленный ответ",
                "verbose_name_plural": "Отправленные ответы",
            },
        ),
        migrations.AlterField(
            model_name="question",
            name="input_type",
            field=models.CharField(
                choices=[
                    ("s", "один верный ответ"),
                    ("m", "несколько верных ответов"),
                ],
                default="s",
                max_length=1,
                verbose_name="Кол-во верных ответов",
            ),
        ),
        migrations.RemoveField(
            model_name="quiz",
            name="theme",
        ),
        migrations.AddField(
            model_name="quiz",
            name="theme",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="quizzes.theme",
                verbose_name="Темы квиза",
            ),
            preserve_default=False,
        ),
    ]