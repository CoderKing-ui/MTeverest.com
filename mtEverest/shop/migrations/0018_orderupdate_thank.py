# Generated by Django 3.1 on 2020-09-04 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20200904_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='thank',
            field=models.CharField(default='', max_length=10),
        ),
    ]
