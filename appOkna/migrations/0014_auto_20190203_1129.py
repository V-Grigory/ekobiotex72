# Generated by Django 2.1.5 on 2019-02-03 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appOkna', '0013_auto_20181207_0832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryproduct',
            options={'verbose_name': 'Категория товара', 'verbose_name_plural': 'Категории товаров'},
        ),
        migrations.AlterModelOptions(
            name='informationarticles',
            options={'verbose_name': 'Информация', 'verbose_name_plural': 'Информация'},
        ),
        migrations.AlterModelOptions(
            name='partners',
            options={'verbose_name': 'Партнер', 'verbose_name_plural': 'Партнеры'},
        ),
        migrations.AlterModelOptions(
            name='servicearticles',
            options={'verbose_name': 'Сервис', 'verbose_name_plural': 'Сервисы'},
        ),
    ]
