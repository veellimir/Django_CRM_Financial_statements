from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from urllib.parse import unquote
from django.http import HttpResponseRedirect
from django.urls import reverse

import os
import datetime

from dotenv import load_dotenv

from .forms import OperationsForm
from .utils import (get_list_deal, get_list_counterparty, get_list_articles, add_outcome,
                    disk_resources_upload, admin_search_reports, get_list_money)

from .models import Operations

load_dotenv()


@user_passes_test(lambda u: not u.is_superuser, login_url='all_reports')
@login_required(login_url='login')
def home(request):
    deal_names = get_list_deal()
    counterparty_names = get_list_counterparty()
    undisclosed_write = get_list_articles()

    user_moneybag_id = request.user.moneybag_id

    if request.method == 'POST':
        form = OperationsForm(request.POST, request.FILES)

        if form.is_valid():
            operation = form.save(commit=False)
            operation.user = request.user
            operation.description = form.cleaned_data['description'].lower()

            if operation.deal_name:
                operation.deal_name = form.cleaned_data['selectedDealName'].lower()

            if operation.selectedDealCounterparty:
                operation.selectedDealCounterparty = form.cleaned_data['selectedDealCounterparty'].lower()

            instance = form.save(commit=False)
            during_period = form.cleaned_data['during_period']

            name_image = ('За_' + during_period.strftime('%d.%m.%Y') + '__'
                          + request.user.first_name + '__'
                          + form.cleaned_data['description'].replace(' ', '_'))

            new_file_name = name_image + os.path.splitext(instance.image_cheque.name)[1]
            instance.image_cheque.name = os.path.join(os.path.dirname(instance.image_cheque.name), new_file_name)
            description = form.cleaned_data['description'] + ' ' + os.getenv('URL_LINK') + '/media/' + new_file_name
            instance.save()

            add_outcome(request, form, user_moneybag_id, description, during_period)

            image_url = unquote(instance.image_cheque.url)
            path_image_media = '.' + image_url
            dir_path = f'/reports/{datetime.datetime.now().year}/'

            disk_resources_upload(path_image_media, name_image, dir_path)

            messages.success(request, 'Отчёт успешно отправлен')
            return redirect('home')
    else:
        form = OperationsForm()

    context = {
        'title': 'Загрузить отчёт',
        'form': form,
        'deal_names': deal_names,
        'counterparty_names': counterparty_names,
        'undisclosed_write': undisclosed_write
    }
    return render(request, 'mainapp/home.html', context)


@user_passes_test(lambda u: not u.is_superuser, login_url='all_reports')
@login_required(login_url='login')
def reports_user(request):
    user_reports = Operations.objects.filter(user=request.user).order_by('-status')
    search_query, user_operations = admin_search_reports(request)

    context = {
        'title': 'Мои отчёты',
        'user_operations': user_operations,
        'search_query': search_query
    }
    return render(request, 'mainapp/reports_users.html', context)


@login_required(login_url='login')
def all_reports(request, endpoint):
    """
    Динамическая функция для фильтрации
    :param request:
    :param endpoint:
    :return: Отфильтрованный список отчётов:
    """
    page = endpoint

    all_operations = Operations.objects.all().order_by('-status')
    search_query, all_operations = admin_search_reports(request)

    context = {
        'title': 'Все отчёты',
        'all_operations': all_operations,
        'search_query': search_query,
        'page': page
    }
    return render(request, 'mainapp/all_reports.html', context)


@login_required(login_url='login')
def new_report(request):
    return all_reports(request, 'new_report')


@login_required(login_url='login')
def verify_reports(request):
    return all_reports(request, 'verify_reports')


@login_required(login_url='login')
def verify_report(request, operation_id):
    operation = Operations.objects.get(id=operation_id)
    operation.status = Operations.VERIFY_REPORT

    messages.success(request, 'Отчёт успешно принят')
    operation.save()
    return redirect(request.META.get('HTTP_REFERER'))
