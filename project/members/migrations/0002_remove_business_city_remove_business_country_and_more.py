# Generated by Django 4.2 on 2023-05-12 09:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='city',
        ),
        migrations.RemoveField(
            model_name='business',
            name='country',
        ),
        migrations.RemoveField(
            model_name='business',
            name='pricerange',
        ),
        migrations.AddField(
            model_name='business',
            name='rating',
            field=models.CharField(default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business',
            name='business_type',
            field=models.CharField(default='Tourist Attraction', max_length=12),
        ),
    ]
