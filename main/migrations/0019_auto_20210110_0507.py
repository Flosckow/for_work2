# Generated by Django 3.1.4 on 2021-01-10 05:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210110_0505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listtitle',
            name='title_del',
        ),
        migrations.AddField(
            model_name='listtitle',
            name='title_del',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='headers', to='main.headlisttitle'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 10, 5, 7, 44, 290186, tzinfo=utc)),
        ),
    ]