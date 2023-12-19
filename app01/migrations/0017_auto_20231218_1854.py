# Generated by Django 3.2.11 on 2023-12-18 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_alter_lightnovel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightnovel',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.author', verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='lightnovel',
            name='illustrator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.illustrator', verbose_name='插画师'),
        ),
        migrations.AlterField(
            model_name='lightnovel',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.publisher', verbose_name='出版社'),
        ),
    ]
