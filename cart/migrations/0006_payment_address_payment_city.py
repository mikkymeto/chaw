# Generated by Django 4.0.6 on 2022-09-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_payment_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='address',
            field=models.CharField(default='a', max_length=20),
        ),
        migrations.AddField(
            model_name='payment',
            name='city',
            field=models.CharField(default='a', max_length=20),
        ),
    ]
