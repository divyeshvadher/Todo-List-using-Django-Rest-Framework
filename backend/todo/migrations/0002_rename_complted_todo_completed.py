# Generated by Django 4.2.3 on 2024-03-17 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='complted',
            new_name='completed',
        ),
    ]
