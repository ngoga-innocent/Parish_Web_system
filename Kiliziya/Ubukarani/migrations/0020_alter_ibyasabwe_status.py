# Generated by Django 4.1.3 on 2023-01-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ubukarani', '0019_alter_ibyasabwe_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ibyasabwe',
            name='status',
            field=models.CharField(choices=[('2', 'approved'), ('1', 'Pending')], default='1', max_length=20),
        ),
    ]
