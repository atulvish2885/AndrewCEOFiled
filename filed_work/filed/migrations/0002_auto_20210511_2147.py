# Generated by Django 3.1.7 on 2021-05-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcast',
            name='participants',
            field=models.PositiveIntegerField(max_length=100),
        ),
    ]
