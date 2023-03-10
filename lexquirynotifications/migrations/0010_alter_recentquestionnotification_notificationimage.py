# Generated by Django 3.2.6 on 2022-05-02 15:14

import backend.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexquirynotifications', '0009_auto_20220502_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentquestionnotification',
            name='notificationImage',
            field=models.ImageField(blank=True, default=',https://res.cloudinary.com/dthlim6ef/image/upload/v1651605071/media/simone-secci-49uySSA678U-unsplash_1_swrsb6.jpg', null=True, upload_to='notification/images', validators=[backend.validators.validate_file_size]),
        ),
    ]
