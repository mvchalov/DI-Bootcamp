# Generated by Django 4.2 on 2023-04-25 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='gif',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
