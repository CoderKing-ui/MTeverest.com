# Generated by Django 3.1 on 2020-09-01 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='zip',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='itemJSon',
            field=models.CharField(default='', max_length=50000),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]