# Generated by Django 2.1.1 on 2018-09-06 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplusapp', '0002_newslettersubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeConsultationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(blank=True, max_length=17, null=True)),
                ('school', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.CharField(blank=True, max_length=350, null=True)),
                ('subjects', models.CharField(blank=True, max_length=350, null=True)),
                ('grade', models.CharField(blank=True, max_length=50, null=True)),
                ('details', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]