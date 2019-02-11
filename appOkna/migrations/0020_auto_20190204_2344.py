# Generated by Django 2.1.3 on 2019-02-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOkna', '0019_params_informationarticle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='params',
            name='informationarticle',
        ),
        migrations.RemoveField(
            model_name='params',
            name='product',
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='keywords',
            field=models.CharField(blank=True, default='', max_length=600, verbose_name='keywords'),
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='pagetitle',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='products',
            name='keywords',
            field=models.CharField(blank=True, default='', max_length=600, verbose_name='keywords'),
        ),
        migrations.AddField(
            model_name='products',
            name='pagetitle',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='title'),
        ),
        migrations.DeleteModel(
            name='Params',
        ),
    ]