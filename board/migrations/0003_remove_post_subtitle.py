# Generated by Django 2.2.7 on 2019-11-14 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20191114_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='subtitle',
        ),
    ]
