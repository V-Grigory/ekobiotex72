from django.db import models
from django.utils import timezone

def upload_directory(instance, filename):
    return 'appOkna/' + filename


class CategoryProduct (models.Model):
    title = models.CharField('Название', max_length=100)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

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
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ServiceArticles (models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Контент')
    image = models.FileField('Изображение', upload_to = upload_directory)
    created_date = models.DateTimeField('Дата создания', default = timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

class InformationArticles (models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Контент')
    image = models.FileField('Изображение', upload_to = upload_directory, blank = True)
    created_date = models.DateTimeField('Дата создания', default = timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'

class Partners (models.Model):
    title = models.CharField('Название', max_length=100)
    image = models.FileField('Изображение', upload_to = upload_directory)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

class Params (models.Model):
    product = models.OneToOneField(Products, on_delete = models.CASCADE, primary_key = False, default = None, blank = True, null = True)
    title = models.CharField('title', max_length = 100, default = '', blank = True)
    description = models.TextField('description', max_length = 1000, default = '', blank = True)
    keywords = models.TextField('keywords', max_length = 600, default = '', blank = True)

    def __str__(self):
        return 'Параметры'
    class Meta:
        verbose_name = 'Параметры'
        verbose_name_plural = 'Параметры'

class Mainpage (models.Model):
    title = models.CharField('title', max_length = 100, default = '', blank = True)
    description = models.TextField('description', max_length = 1000, default = '', blank = True)
    keywords = models.TextField('keywords', max_length = 600, default = '', blank = True)

    def __str__(self):
        return 'Главная страница'
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'
