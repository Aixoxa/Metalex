# Generated by Django 3.2.6 on 2022-01-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamber', '0014_alter_chamber_memberrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamber',
            name='experience',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
