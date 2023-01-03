# Generated by Django 4.1.3 on 2022-12-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mass', '0006_mass_delete_holymass'),
    ]

    operations = [
        migrations.AddField(
            model_name='mass',
            name='ivanjiri_verse',
            field=models.CharField(default='luke', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mass',
            name='verse_1',
            field=models.CharField(default='intangiriro', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mass',
            name='verse_2',
            field=models.CharField(default='amateka', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mass',
            name='padiri',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mass',
            name='place',
            field=models.CharField(max_length=50),
        ),
    ]
