# Generated by Django 5.1 on 2024-11-06 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_alter_option_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='text',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
