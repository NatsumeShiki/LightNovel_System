# Generated by Django 3.2.11 on 2023-12-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0020_rename_account_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='username',
            field=models.CharField(default='root', max_length=32, verbose_name='用户名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=64, verbose_name='密码'),
        ),
    ]
