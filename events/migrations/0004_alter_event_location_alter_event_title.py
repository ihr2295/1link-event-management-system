# Generated by Django 5.0.6 on 2024-06-08 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_profile_avatar_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]