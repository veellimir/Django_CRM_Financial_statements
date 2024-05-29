from django.db import models
from django.conf import settings


class Operations(models.Model):
    NEW_REPORT = 0
    VERIFY_REPORT = 1
    REJECTED = 2

    STATUSES = (
        (NEW_REPORT, 'Новый'),
        (VERIFY_REPORT, 'Проверено и отправлено'),
        (REJECTED, 'Отклонено администратором')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=False, blank=False,
                             verbose_name='Проектный менеджер')

    deal_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='ID Сделки')
    selectedDealName = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cделка')
    selectedDealCounterparty = models.CharField(max_length=200, blank=True, null=True, verbose_name='Контрагент')
    counterparty = models.CharField(max_length=200, blank=True, null=True, verbose_name='ID Контрагента')
    undisclosed = models.CharField(max_length=200, blank=True, null=True, verbose_name='Неразнесенное списание')

    value = models.CharField(max_length=200, blank=False, null=False, verbose_name='Сумма руб.')
    description = models.TextField(blank=False, null=False, verbose_name='Назначения платежа')
    image_cheque = models.ImageField(blank=False, null=False, verbose_name='Чек (фото)')
    during_period = models.DateTimeField(blank=False, null=False, verbose_name='За период')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    status = models.SmallIntegerField(default=NEW_REPORT, choices=STATUSES)

    class Meta:
        verbose_name = 'отчёт'
        verbose_name_plural = 'Отчёты'
