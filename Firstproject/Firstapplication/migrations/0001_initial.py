# Generated by Django 2.0.5 on 2020-07-03 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentID', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('ContactNum', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=50)),
            ],
        ),
    ]