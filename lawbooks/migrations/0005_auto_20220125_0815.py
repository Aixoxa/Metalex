# Generated by Django 3.2.6 on 2022-01-25 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawbooks', '0004_alter_lawbook_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawbook',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='lawbook',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]