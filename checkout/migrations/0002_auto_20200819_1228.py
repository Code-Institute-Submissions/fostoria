# Generated by Django 3.0.8 on 2020-08-19 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlinedetail',
            name='product_size',
        ),
        migrations.AddField(
            model_name='orderlinedetail',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderlinedetail',
            name='date_ordered',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
