# Generated by Django 5.0.7 on 2024-09-16 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='type',
            new_name='media_type',
        ),
    ]
