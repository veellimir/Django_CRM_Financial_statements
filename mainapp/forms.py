from django import forms

from .models import Operations


class OperationsForm(forms.ModelForm):
    class Meta:
        model = Operations
        fields = [
            'deal_name',
            'counterparty',
            'undisclosed',
            'value',
            'description',
            'image_cheque'
        ]
        labels = {
            'deal_name': 'Сделки',
            'counterparty': 'Контрагенты',
            'undisclosed': 'Неразнесенное списание',
            'value': 'Сумма',
            'description': 'Назначение платежа',
            'image_cheque': 'Чек',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['moneybag_id'].initial = user.moneybag_id


