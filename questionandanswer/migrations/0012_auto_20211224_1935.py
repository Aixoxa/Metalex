# Generated by Django 3.2.6 on 2021-12-24 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionandanswer', '0011_auto_20211224_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='downVotes',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='upVotes',
        ),
    ]
