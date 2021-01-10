# Generated by Django 3.1.4 on 2021-01-10 05:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210110_0502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headlisttitle',
            name='title_del',
        ),
        migrations.AddField(
            model_name='listtitle',
            name='title_del',
            field=models.ManyToManyField(to='main.HeadListTitle'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 10, 5, 5, 33, 422912, tzinfo=utc)),
        ),
    ]
