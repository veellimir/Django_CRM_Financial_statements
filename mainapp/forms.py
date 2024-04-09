from django import forms

from .models import Operations


class OperationsForm(forms.ModelForm):
    class Meta:
        model = Operations
        fields = [
            'reports',
            'counterparty',
            'undisclosed_write',
            'value',
            'description',
            'image_cheque',
        ]
        labels = {
            'reports': 'Сделки',
            'counterparty': 'Контрагенты',
            'undisclosed_write': 'Неразнесенное списание',
            'value': 'Сумма',
            'description': 'Назначение платежа',
            'image_cheque': 'Чек',
        }

        # widgets = {
        #     'reports': forms.Select(),
        #     'counterparty': forms.Select(),
        # }
