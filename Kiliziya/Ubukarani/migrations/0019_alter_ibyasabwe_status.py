# Generated by Django 4.1.3 on 2023-01-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ubukarani', '0018_ibyasabwe_owner_id_alter_ibyasabwe_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ibyasabwe',
            name='status',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'approved')], default='1', max_length=20),
        ),
    ]
