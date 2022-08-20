from django.db import models
from django.utils.translation import gettext_lazy as l_

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name=l_('Родительская категория'),
                               related_name='child', on_delete=models.SET_NULL)
    name = models.CharField(max_length=550)

    class Meta:
        verbose_name = l_('Категория товаров')
        verbose_name_plural = l_('Категории товаров')


class MeasureUnit(models.Model):
    name = models.CharField(max_length=255, verbose_name=l_('Название'))
    full_name = models.CharField(max_length=255, blank=True, default='', verbose_name=l_('Полное название'))

    class Meta:
        verbose_name = l_('Единица измерения')
        verbose_name_plural = l_('Единицы измерения')


class Product(models.Model):
    PRODUCT = 0
    SERVICE = 1

    TYPES = (
        (PRODUCT, l_('Товар')),
        (SERVICE, l_('Услуга')),
    )

    category = TreeForeignKey(Category, null=True, blank=True, related_name='products',
                              on_delete=models.SET_NULL, verbose_name=l_('Категория'))
    code = models.CharField(max_length=255, verbose_name=l_('Артикул'), blank=True, null=True, default='')
    name = models.CharField(max_length=1024, verbose_name=l_('Наименование'))
    description = models.TextField(blank=True, null=True, verbose_name=l_('Описание'))
    product_type = models.IntegerField(choices=TYPES, default=PRODUCT, verbose_name=l_('Тип номенклатуры'))
    rate_nds = models.FloatField(default=20, verbose_name=l_('Ставка НДС'))
    measure_unit = models.ForeignKey(MeasureUnit, null=True, blank=True, verbose_name=l_('Единица измерения'),
                                     on_delete=models.SET_NULL)
    hidden = models.BooleanField(default=False, verbose_name=l_('Скрывать товар в Agora'), db_index=True)

    class Meta:
        verbose_name = l_('Товар')
        verbose_name_plural = l_('Товары')
