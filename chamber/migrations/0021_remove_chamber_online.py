# Generated by Django 3.2.6 on 2022-02-18 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamber', '0020_chamber_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chamber',
            name='online',
        ),
    ]
