# Generated by Django 3.2.6 on 2021-12-24 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionandanswer', '0007_downvote_upvote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='downvote',
            old_name='votes',
            new_name='downvotes',
        ),
        migrations.RenameField(
            model_name='upvote',
            old_name='votes',
            new_name='upvotes',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='downVotes',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='upVotes',
        ),
    ]