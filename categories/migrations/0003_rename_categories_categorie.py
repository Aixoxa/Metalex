# Generated by Django 3.2.6 on 2021-12-26 12:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0002_auto_20211226_1350'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Categorie',
        ),
    ]