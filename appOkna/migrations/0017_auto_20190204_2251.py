# Generated by Django 2.1.3 on 2019-02-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOkna', '0016_auto_20190204_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='keywords',
            field=models.TextField(max_length=600, verbose_name='keywords'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
    ]
