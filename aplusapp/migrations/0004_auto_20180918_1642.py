# Generated by Django 2.0.3 on 2018-09-18 16:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplusapp', '0003_freeconsultationrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(blank=True, max_length=17, null=True)),
                ('details', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('number_of_hours', models.IntegerField(validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(0)])),
                ('details', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(blank=True, max_length=17, null=True)),
                ('school', models.CharField(blank=True, max_length=250, null=True)),
                ('grade', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentTutoredByTutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplusapp.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects_tutoring', models.CharField(max_length=1000)),
                ('hours_tutored', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='aplususer',
            name='is_a_tutor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studenttutoredbytutor',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplusapp.Tutor'),
        ),
        migrations.AddField(
            model_name='report',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplusapp.Student'),
        ),
        migrations.AddField(
            model_name='report',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplusapp.Tutor'),
        ),
    ]
