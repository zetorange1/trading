# Generated by Django 2.0 on 2018-01-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_realtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtime',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='realtime',
            name='value',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]