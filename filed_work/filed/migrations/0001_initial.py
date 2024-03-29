# Generated by Django 3.1.7 on 2021-05-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audiobook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audiofile', models.CharField(default='Audiobook', max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('author_of_title', models.CharField(max_length=100)),
                ('narrator', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Postcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audiofile', models.CharField(default='Postcard', max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
                ('host', models.CharField(max_length=20)),
                ('participants', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audiofile', models.CharField(default='Song', max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
