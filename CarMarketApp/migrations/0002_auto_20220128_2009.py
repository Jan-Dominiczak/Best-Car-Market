# Generated by Django 3.2.11 on 2022-01-28 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarMarketApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dealer',
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(default='', max_length=4000),
        ),
    ]
