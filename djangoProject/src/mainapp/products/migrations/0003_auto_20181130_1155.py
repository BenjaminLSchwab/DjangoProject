# Generated by Django 2.0.7 on 2018-11-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181129_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('appetizers', 'appetisers'), ('entrees', 'entrees'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
