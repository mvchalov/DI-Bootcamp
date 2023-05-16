# Generated by Django 4.2.1 on 2023-05-08 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='', max_length=100)),
                ('temperature', models.FloatField(default=-273)),
                ('created_at', models.DateField(auto_now=True)),
                ('type', models.CharField(choices=[('su', 'Sunny'), ('cl', 'Cloudy'), ('wi', 'Windy'), ('ra', 'Rainy'), ('st', 'Stormy')], default='su', max_length=2)),
            ],
        ),
    ]
