# Generated by Django 5.1 on 2024-11-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_question_is_multiple'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
