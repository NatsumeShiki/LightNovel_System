# Generated by Django 3.2.11 on 2023-12-18 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_auto_20231218_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightnovel',
            name='image',
            field=models.ImageField(default='default.png', upload_to='image', verbose_name='封面'),
        ),
    ]
