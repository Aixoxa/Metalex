# Generated by Django 3.2.6 on 2022-05-02 06:26

import backend.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexquirynotifications', '0007_auto_20220421_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentplannotification',
            name='notificationImage',
            field=models.ImageField(blank=True, null=True, upload_to='notification/images', validators=[backend.validators.validate_file_size]),
        ),
        migrations.AddField(
            model_name='recentquestionnotification',
            name='notificationImage',
            field=models.ImageField(blank=True, null=True, upload_to='notification/images', validators=[backend.validators.validate_file_size]),
        ),
    ]
