# Generated by Django 5.1.5 on 2025-02-01 12:29

import app.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('creation_date', models.DateField(auto_now=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to=app.models.upload_to)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
