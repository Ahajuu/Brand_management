# Generated by Django 3.0.6 on 2020-05-31 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_magmt', '0005_auto_20200530_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=40, null=True),
        ),
    ]