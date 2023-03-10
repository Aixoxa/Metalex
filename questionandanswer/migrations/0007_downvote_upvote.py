# Generated by Django 3.2.6 on 2021-12-24 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionandanswer', '0006_auto_20211224_0137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('votes', models.IntegerField(blank=True, default=0, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='questionandanswer.answer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Downvote',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('votes', models.IntegerField(blank=True, default=0, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='questionandanswer.answer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
