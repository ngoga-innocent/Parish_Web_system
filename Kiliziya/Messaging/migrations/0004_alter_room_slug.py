# Generated by Django 4.1.3 on 2023-01-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messaging', '0003_alter_messaging_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.CharField(max_length=1000),
        ),
    ]