# Generated by Django 3.2.11 on 2023-12-18 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0019_rename_user_account'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='account',
            new_name='Admin',
        ),
    ]
