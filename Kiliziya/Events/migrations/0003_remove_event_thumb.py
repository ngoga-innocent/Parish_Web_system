# Generated by Django 4.1.3 on 2023-01-04 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_alter_event_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='thumb',
        ),
    ]