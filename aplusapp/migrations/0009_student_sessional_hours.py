# Generated by Django 2.1.1 on 2018-09-23 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplusapp', '0008_tutor_hours_tutored_this_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sessional_hours',
            field=models.FloatField(default=0),
        ),
    ]