# Generated by Django 5.1.2 on 2025-03-30 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_alter_license_image_alter_review_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license',
            name='slug',
        ),
    ]
