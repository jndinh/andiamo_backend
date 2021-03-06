# Generated by Django 2.0.4 on 2018-04-30 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0003_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservice.Store')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservice.User')),
            ],
        ),
    ]
