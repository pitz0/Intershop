# Generated by Django 2.1.5 on 2019-01-18 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meddata', '0007_auto_20190117_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='genric_med',
            new_name='generic_med',
        ),
    ]
