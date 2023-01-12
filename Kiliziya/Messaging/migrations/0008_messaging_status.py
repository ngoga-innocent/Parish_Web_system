# Generated by Django 4.1.3 on 2023-01-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messaging', '0007_remove_room_participator_room_client_room_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='messaging',
            name='status',
            field=models.CharField(choices=[('1', 'not read'), ('2', 'read')], default='1', max_length=20),
        ),
    ]
