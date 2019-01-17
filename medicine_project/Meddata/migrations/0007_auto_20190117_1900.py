# Generated by Django 2.1.5 on 2019-01-17 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Meddata', '0006_auto_20190117_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='genric_med',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Meddata.GENERIC'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='mfg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Meddata.MFG'),
        ),
    ]
