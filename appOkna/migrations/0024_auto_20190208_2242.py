# Generated by Django 2.1.3 on 2019-02-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOkna', '0023_auto_20190208_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationarticles',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='partners',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='servicearticles',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
