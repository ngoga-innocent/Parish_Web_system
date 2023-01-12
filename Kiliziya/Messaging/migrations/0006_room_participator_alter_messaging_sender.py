# Generated by Django 4.1.3 on 2023-01-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messaging', '0005_rename_reciever_messaging_room_messaging_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participator',
            field=models.CharField(default='NGOGA', max_length=10000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messaging',
            name='sender',
            field=models.CharField(default='Ngoga', max_length=10000, null=True),
        ),
    ]
