# Generated by Django 2.1.5 on 2019-01-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meddata', '0002_auto_20190117_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='EntryDt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='PISDATE',
            field=models.DateTimeField(null=True),
        ),
    ]
