# Generated by Django 3.2.6 on 2022-02-05 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_useraccount_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile-pic.jpg', null=True, upload_to='account/images'),
        ),
    ]
