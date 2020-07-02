# Generated by Django 2.2.5 on 2020-06-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductID', models.CharField(max_length=20)),
                ('ProductName', models.CharField(max_length=20)),
                ('Price', models.FloatField()),
                ('ProductImage', models.ImageField(upload_to='')),
            ],
        ),
    ]
