# Generated by Django 2.2.4 on 2019-09-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20190901_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('English', 'ENGLISH'), ('Hindi', 'HINDI')], max_length=10),
        ),
    ]
