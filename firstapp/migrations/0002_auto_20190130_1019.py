# Generated by Django 2.1.5 on 2019-01-30 04:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='ap_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.Signup'),
        ),
        migrations.AlterField(
            model_name='business',
            name='b_applied_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 30, 10, 19, 19, 896990)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='ap_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 30, 10, 19, 19, 896990)),
        ),
    ]
