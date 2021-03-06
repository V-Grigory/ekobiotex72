# Generated by Django 2.1.3 on 2018-11-19 17:34

import appOkna.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appOkna', '0007_categoryproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Контент')),
                ('image', models.FileField(blank=True, upload_to=appOkna.models.upload_directory, verbose_name='Изображение')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete='CASCADE', to='appOkna.CategoryProduct')),
            ],
        ),
    ]
