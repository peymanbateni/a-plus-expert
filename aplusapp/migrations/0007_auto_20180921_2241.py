# Generated by Django 2.1.1 on 2018-09-21 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplusapp', '0006_auto_20180919_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='title',
        ),
        migrations.AddField(
            model_name='student',
            name='aplus_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='hours_tutored',
            field=models.FloatField(default=0),
        ),
    ]
