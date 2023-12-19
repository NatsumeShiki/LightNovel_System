# Generated by Django 3.2.11 on 2023-12-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_rename_book_lightnovel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='address',
        ),
        migrations.AddField(
            model_name='publisher',
            name='date',
            field=models.DateField(blank=True, max_length=64, null=True, verbose_name='创立日期'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=64, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='illustrator',
            name='email',
            field=models.EmailField(blank=True, max_length=64, null=True, verbose_name='邮箱'),
        ),
    ]
