# Generated by Django 4.0.6 on 2022-09-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_shopcart_c_date_shopcart_c_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='c_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='c_item',
            field=models.IntegerField(default=1),
        ),
    ]
