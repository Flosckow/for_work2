# Generated by Django 3.1.4 on 2021-01-06 07:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210106_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 7, 38, 52, 788137, tzinfo=utc)),
        ),
    ]
