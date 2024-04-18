from django import forms

from .models import Operations


class OperationsForm(forms.ModelForm):
    class Meta:
        model = Operations
        fields = [
            'deal_name',
            'selectedDealName',
            'counterparty',
            'undisclosed',
            'value',
            'description',
            'image_cheque',
            'during_period',
        ]
        labels = {
            'deal_name': 'Сделки',
            'counterparty': 'Контрагенты',
            'selectedDealName': 'Имя сделки',
            'undisclosed': 'Неразнесенное списание',
            'value': 'Сумма',
            'description': 'Назначение платежа',
            'image_cheque': 'Чек',
            'during_period': 'За период'
        }

    during_period = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['moneybag_id'].initial = user.moneybag_id


