# Generated by Django 3.2.11 on 2023-12-18 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20231217_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightnovel',
            name='image',
            field=models.ImageField(default='default.png', upload_to='image'),
        ),
    ]
