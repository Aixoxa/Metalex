# Generated by Django 3.2.6 on 2021-12-26 12:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0004_rename_categorie_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='categoryLetter',
        ),
    ]
