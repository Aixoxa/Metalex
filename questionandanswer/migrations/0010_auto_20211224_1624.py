# Generated by Django 3.2.6 on 2021-12-24 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionandanswer', '0009_auto_20211224_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='downvote',
            old_name='votes',
            new_name='dvotes',
        ),
        migrations.RenameField(
            model_name='upvote',
            old_name='votes',
            new_name='uvotes',
        ),
    ]