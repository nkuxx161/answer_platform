# Generated by Django 3.0.8 on 2020-07-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatting',
            name='personId',
            field=models.TextField(blank=True),
        ),
    ]
