# Generated by Django 4.1.3 on 2023-01-07 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ubukarani', '0002_rename_name_icyangombwa_amazina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ibyasabwe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('umubyeyi', models.ImageField(upload_to='pics')),
                ('umuryangoremezo', models.ImageField(upload_to='pics')),
                ('amazina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ubukarani.icyangombwa')),
            ],
        ),
    ]
