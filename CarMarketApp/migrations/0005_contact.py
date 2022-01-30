# Generated by Django 3.2.11 on 2022-01-30 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CarMarketApp', '0004_auto_20220130_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(help_text='Tell buyers, where can they buy your car', max_length=30)),
                ('phone_number', models.IntegerField(help_text='Your phone number will help buyers contact with you')),
                ('seller_status', models.CharField(choices=[('private', 'Private'), ('dealer', 'Dealer')], help_text='Private seller/Company', max_length=30)),
                ('company_name', models.CharField(help_text='Optional', max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]