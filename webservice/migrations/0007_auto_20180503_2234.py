# Generated by Django 2.0.4 on 2018-05-04 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0006_auto_20180503_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='postal_code',
            new_name='zip_code',
        ),
    ]
