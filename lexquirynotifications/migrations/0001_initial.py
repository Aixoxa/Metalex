# Generated by Django 3.2.6 on 2022-02-12 12:43

import backend.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0004_alter_post_caption'),
        ('questionandanswer', '0023_remove_tag_user'),
        ('chamber', '0019_alter_chamber_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionNotification',
            fields=[
                ('text', models.TextField(blank=True, null=True)),
                ('notificationImage', models.ImageField(blank=True, default='profile-pic.jpg', null=True, upload_to='notification/images', validators=[backend.validators.validate_file_size])),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questionandanswer.question')),
            ],
        ),
        migrations.CreateModel(
            name='LawyerNotification',
            fields=[
                ('text', models.TextField(blank=True, null=True)),
                ('notificationImage', models.ImageField(blank=True, default='profile-pic.jpg', null=True, upload_to='notification/images', validators=[backend.validators.validate_file_size])),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chamber.chamber')),
            ],
        ),
        migrations.CreateModel(
            name='BlogNotification',
            fields=[
                ('text', models.TextField(blank=True, null=True)),
                ('notificationImage', models.ImageField(blank=True, default='profile-pic.jpg', null=True, upload_to='notification/images', validators=[backend.validators.validate_file_size])),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerNotification',
            fields=[
                ('text', models.TextField(blank=True, null=True)),
                ('notificationImage', models.ImageField(blank=True, default='profile-pic.jpg', null=True, upload_to='notification/images', validators=[backend.validators.validate_file_size])),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questionandanswer.answer')),
            ],
        ),
    ]
