# Generated by Django 3.2.6 on 2022-01-22 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chamber', '0005_auto_20220121_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('memberName', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.CharField(blank=True, max_length=200, null=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chamber.chamber')),
            ],
        ),
    ]