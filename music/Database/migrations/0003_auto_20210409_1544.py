# Generated by Django 3.1.7 on 2021-04-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0002_auto_20210409_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sold',
            field=models.CharField(default=0, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(),
        ),
    ]