# Generated by Django 3.2.6 on 2022-03-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexquirynotifications', '0005_rename_paymentplannotifications_paymentplannotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentplannotification',
            name='plan',
            field=models.TextField(blank=True, null=True),
        ),
    ]
