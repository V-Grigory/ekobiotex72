# Generated by Django 2.1.3 on 2019-02-04 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appOkna', '0018_auto_20190204_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='params',
            name='informationarticle',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='appOkna.InformationArticles'),
        ),
    ]
