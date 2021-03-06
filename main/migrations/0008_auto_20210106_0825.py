# Generated by Django 3.1.4 on 2021-01-06 08:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210106_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='listproduct',
            name='list_product',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='product_list', to='main.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 8, 24, 49, 659073, tzinfo=utc)),
        ),
    ]
