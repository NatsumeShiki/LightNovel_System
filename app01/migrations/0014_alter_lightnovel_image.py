# Generated by Django 3.2.11 on 2023-12-18 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0013_alter_lightnovel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightnovel',
            name='image',
            field=models.ImageField(default='default.png', upload_to='image', verbose_name='封面'),
        ),
    ]
