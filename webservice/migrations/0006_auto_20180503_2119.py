# Generated by Django 2.0.4 on 2018-05-04 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0005_auto_20180503_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='line_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
