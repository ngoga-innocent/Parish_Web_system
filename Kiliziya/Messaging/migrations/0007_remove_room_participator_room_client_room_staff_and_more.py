# Generated by Django 4.1.3 on 2023-01-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messaging', '0006_room_participator_alter_messaging_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='participator',
        ),
        migrations.AddField(
            model_name='room',
            name='client',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='staff',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='messaging',
            name='sender',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
