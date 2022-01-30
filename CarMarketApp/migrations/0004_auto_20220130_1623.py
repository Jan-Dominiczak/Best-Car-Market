# Generated by Django 3.2.11 on 2022-01-30 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CarMarketApp', '0003_car_seller_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='id',
        ),
        migrations.AddField(
            model_name='car',
            name='col1',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Seller'),
        ),
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('used', 'Used'), ('damaged', 'Damaged')], max_length=32),
        ),
    ]
