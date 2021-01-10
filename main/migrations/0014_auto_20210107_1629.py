# Generated by Django 3.1.4 on 2021-01-07 16:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210107_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headlisttitle',
            name='title_del',
        ),
        migrations.AddField(
            model_name='listtitle',
            name='title_del',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='head_list', to='main.headlisttitle'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 7, 16, 29, 53, 7016, tzinfo=utc)),
        ),
    ]