# Generated by Django 3.0.8 on 2020-09-05 12:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_remove_ordershippingdetails_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlinedetail',
            name='size',
            field=models.CharField(max_length=3),
            preserve_default=False,
        ),
    ]
