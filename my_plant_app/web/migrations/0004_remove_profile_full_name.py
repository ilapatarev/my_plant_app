# Generated by Django 4.2.2 on 2023-06-23 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_profile_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
    ]
