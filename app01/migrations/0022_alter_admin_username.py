# Generated by Django 3.2.11 on 2023-12-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0021_auto_20231218_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='username',
            field=models.CharField(max_length=32, unique=True, verbose_name='用户名'),
        ),
    ]
