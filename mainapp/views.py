from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from urllib.parse import unquote

import os

from dotenv import load_dotenv

from .forms import OperationsForm
from .utils import (get_list_deal, get_list_counterparty, get_list_money,
                    get_list_articles, add_outcome, disk_resources_upload)
from .models import Operations

load_dotenv()


@login_required(login_url='login')
def home(request):
    deal_names = get_list_deal()
    counterparty_names = get_list_counterparty()
    money_name = get_list_money()
    undisclosed_write = get_list_articles()

    user_moneybag_id = request.user.moneybag_id

    if request.method == 'POST':
        form = OperationsForm(request.POST, request.FILES)

        if form.is_valid():
            operation = form.save(commit=False)
            operation.user = request.user
            operation.deal_name = form.cleaned_data['selectedDealName']

            instance = form.save()
            instance.image_cheque_link = os.getenv('URL_LINK') + instance.image_cheque.url
            instance.save()

            description = form.cleaned_data['description'] + ' ' + instance.image_cheque_link
            during_period = form.cleaned_data['during_period']

            add_outcome(request, form, user_moneybag_id, description, during_period)

            image_url = unquote(instance.image_cheque.url)
            path_image_media = '.' + image_url

            dir_path = f'/reports'
            disk_resources_upload(path_image_media, dir_path)

            messages.success(request, 'Отчёт успешно отправлен')
            return redirect('home')
    else:
        form = OperationsForm()

    context = {
        'title': 'Отчёты',
        'form': form,
        'deal_names': deal_names,
        'counterparty_names': counterparty_names,
        'money_name': money_name,
        'undisclosed_write': undisclosed_write
    }
    return render(request, 'mainapp/home.html', context)


def reports_user(request):
    user_operations = Operations.objects.filter(user=request.user)

    context = {
        'title': 'Мои отчёты',
        'user_operations': user_operations,
    }
    return render(request, 'mainapp/reports_users.html', context)
