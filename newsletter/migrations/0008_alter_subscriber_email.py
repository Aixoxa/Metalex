# Generated by Django 3.2.6 on 2022-02-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_alter_subscriber_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
