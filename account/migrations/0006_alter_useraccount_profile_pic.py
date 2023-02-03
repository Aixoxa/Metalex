# Generated by Django 3.2.6 on 2022-04-21 16:42

import backend.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_useraccount_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='account/images', validators=[backend.validators.validate_file_size]),
        ),
    ]
