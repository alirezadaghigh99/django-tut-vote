# Generated by Django 3.2.4 on 2021-06-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_alter_question_q_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
