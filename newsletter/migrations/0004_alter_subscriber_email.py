# Generated by Django 3.2.6 on 2022-02-08 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_alter_subscriber_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]