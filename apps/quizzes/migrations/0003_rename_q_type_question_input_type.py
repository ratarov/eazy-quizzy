# Generated by Django 4.2.7 on 2023-11-21 11:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "quizzes",
            "0002_alter_answer_options_alter_question_options_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="q_type",
            new_name="input_type",
        ),
    ]