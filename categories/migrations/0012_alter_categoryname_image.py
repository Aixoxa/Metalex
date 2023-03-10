# Generated by Django 3.2.6 on 2022-02-05 06:28

import backend.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0011_auto_20220201_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryname',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/images', validators=[backend.validators.validate_file_size]),
        ),
    ]
