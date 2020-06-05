# Generated by Django 3.0.6 on 2020-05-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_magmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registerpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=40, null=True)),
                ('bemail', models.CharField(max_length=40, null=True)),
                ('password', models.CharField(max_length=40, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('certificate', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]