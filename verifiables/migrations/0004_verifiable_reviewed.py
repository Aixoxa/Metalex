# Generated by Django 3.2.6 on 2022-02-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verifiables', '0003_rename_uploadedat_verifiable_uploadedat'),
    ]

    operations = [
        migrations.AddField(
            model_name='verifiable',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
