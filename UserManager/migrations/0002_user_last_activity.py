# Generated by Django 3.2.7 on 2022-03-12 01:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_activity',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='last activity'),
        ),
    ]
