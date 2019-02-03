# Generated by Django 2.1.5 on 2019-02-03 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appOkna', '0014_auto_20190203_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, verbose_name='title')),
                ('description', models.TextField(blank=True, default='', max_length=1000, verbose_name='description')),
                ('keywords', models.TextField(blank=True, default='', max_length=600, verbose_name='keywords')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
            },
        ),
        migrations.CreateModel(
            name='Params',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, verbose_name='title')),
                ('description', models.TextField(blank=True, default='', max_length=1000, verbose_name='description')),
                ('keywords', models.TextField(blank=True, default='', max_length=600, verbose_name='keywords')),
                ('product', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='appOkna.Products')),
            ],
            options={
                'verbose_name': 'Параметры',
                'verbose_name_plural': 'Параметры',
            },
        ),
    ]
