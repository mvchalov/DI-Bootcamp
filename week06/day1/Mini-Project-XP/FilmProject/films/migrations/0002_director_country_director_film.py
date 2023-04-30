# Generated by Django 4.2 on 2023-04-30 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='country',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='films.country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='director',
            name='film',
            field=models.ManyToManyField(blank=True, related_name='films', to='films.film'),
        ),
    ]
