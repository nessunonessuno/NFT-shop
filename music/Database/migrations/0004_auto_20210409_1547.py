# Generated by Django 3.1.7 on 2021-04-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0003_auto_20210409_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sold',
            field=models.IntegerField(),
        ),
    ]
