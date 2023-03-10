# Generated by Django 3.2.6 on 2022-03-29 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chamber', '0024_auto_20220303_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentPlan',
            fields=[
                ('plan', models.CharField(blank=True, max_length=200, null=True)),
                ('paidAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chamber.chamber')),
            ],
        ),
    ]
