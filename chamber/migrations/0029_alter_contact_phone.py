# Generated by Django 3.2.6 on 2022-04-21 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamber', '0028_auto_20220421_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]