# Generated by Django 2.0.7 on 2018-12-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20181130_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('treats', 'treats'), ('appetizers', 'appetisers'), ('entrees', 'entrees')], max_length=60),
        ),
    ]
