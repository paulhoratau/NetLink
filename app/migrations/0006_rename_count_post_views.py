# Generated by Django 5.1.5 on 2025-02-05 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_post_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='count',
            new_name='views',
        ),
    ]
