# Generated by Django 2.2.3 on 2019-08-20 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtest', '0005_auto_20190820_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
