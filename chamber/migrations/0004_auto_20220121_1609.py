# Generated by Django 3.2.6 on 2022-01-21 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamber', '0003_auto_20220121_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='practicearea',
            name='name',
        ),
        migrations.RemoveField(
            model_name='qualification',
            name='name',
        ),
    ]