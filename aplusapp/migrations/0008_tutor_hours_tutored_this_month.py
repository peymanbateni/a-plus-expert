# Generated by Django 2.1.1 on 2018-09-22 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplusapp', '0007_auto_20180921_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='hours_tutored_this_month',
            field=models.FloatField(default=0),
        ),
    ]