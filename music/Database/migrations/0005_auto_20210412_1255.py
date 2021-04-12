# Generated by Django 3.1.7 on 2021-04-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0004_auto_20210409_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(),
        ),
    ]
