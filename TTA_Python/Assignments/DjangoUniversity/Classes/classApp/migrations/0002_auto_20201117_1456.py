# Generated by Django 3.1.3 on 2020-11-17 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
