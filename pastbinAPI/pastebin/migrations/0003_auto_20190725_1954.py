# Generated by Django 2.2.3 on 2019-07-25 16:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0002_auto_20190725_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 25, 16, 54, 35, 202328, tzinfo=utc)),
        ),
    ]