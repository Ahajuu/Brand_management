# Generated by Django 3.0.6 on 2020-06-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_magmt', '0007_designer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designer',
            name='pics',
            field=models.ImageField(upload_to=''),
        ),
    ]