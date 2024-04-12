from django.db import models
from django.conf import settings


class Operations(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=False, blank=False,
                             verbose_name='Проектный менеджер')

    deal_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Сделка')
    selectedDealName = models.CharField(max_length=200, blank=True, null=True, verbose_name='ID сделки')
    counterparty = models.CharField(max_length=200, blank=True, null=True, verbose_name='Контрагент')
    undisclosed = models.CharField(max_length=200, blank=True, null=True, verbose_name='Неразнесенное списание')

    value = models.CharField(max_length=200, blank=False, null=False, verbose_name='Сумма руб.')
    description = models.TextField(blank=False, null=False, verbose_name='Назначения платежа')
    image_cheque = models.ImageField(blank=False, null=False, verbose_name='Чек (фото)')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    # def __str__(self):
    #     return self.deal_name

    class Meta:
        verbose_name = 'отчёт'
        verbose_name_plural = 'Отчёты'
