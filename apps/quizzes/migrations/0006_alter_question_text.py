# Generated by Django 4.2.7 on 2023-11-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quizzes", "0005_alter_questionresponse_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="text",
            field=models.CharField(
                max_length=255, verbose_name="Текст вопроса"
            ),
        ),
    ]