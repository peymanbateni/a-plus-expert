# Generated by Django 2.0.3 on 2018-09-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplusapp', '0016_auto_20180924_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='hours_of_tutoring_used_this_month',
            field=models.FloatField(default=0),
        ),
    ]