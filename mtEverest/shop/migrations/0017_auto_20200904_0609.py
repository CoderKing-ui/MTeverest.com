# Generated by Django 3.1 on 2020-09-04 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_orderupdate_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]