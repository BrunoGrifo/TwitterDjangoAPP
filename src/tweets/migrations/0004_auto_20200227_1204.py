# Generated by Django 3.0.2 on 2020-02-27 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20200217_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-timestamp']},
        ),
    ]