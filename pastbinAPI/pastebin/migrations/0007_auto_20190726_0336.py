# Generated by Django 2.2.3 on 2019-07-26 00:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0006_auto_20190726_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='share_to',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]