from django.db import models
from django.utils import timezone

def upload_directory(instance, filename):
    return 'appOkna/' + filename


class CategoryProduct (models.Model):
    title = models.CharField('Название', max_length=100)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.title

class Products (models.Model):
    category = models.ForeignKey(CategoryProduct, on_delete='CASCADE', verbose_name='Категория товара')
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Контент')
    price = models.CharField('Стоимость', max_length=10, default = '')
    image = models.FileField('Изображение', upload_to = upload_directory, blank = True)
    is_popular = models.BooleanField('Популярный товар?', default = False)
    created_date = models.DateTimeField('Дата создания', default = timezone.now)

    def __str__(self):
        return self.title

class ServiceArticles (models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Контент')
    image = models.FileField('Изображение', upload_to = upload_directory)
    created_date = models.DateTimeField('Дата создания', default = timezone.now)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title

class InformationArticles (models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Контент')
    image = models.FileField('Изображение', upload_to = upload_directory, blank = True)
    created_date = models.DateTimeField('Дата создания', default = timezone.now)

    def __str__(self):
        return self.title

class Partners (models.Model):
    title = models.CharField('Название', max_length=100)
    image = models.FileField('Изображение', upload_to = upload_directory)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.title