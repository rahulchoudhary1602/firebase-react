# Generated by Django 2.2.4 on 2019-09-03 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_auto_20190903_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 9, 3, 22, 51, 4, 227346)),
        ),
    ]
