from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import OperationsForm
from .utils import get_list_deal_id, get_list_counterparty, get_list_money, get_list_articles, add_outcome
from .models import Operations


@login_required(login_url='login')
def home(request):
    deal_names = get_list_deal_id()
    counterparty_names = get_list_counterparty()
    money_name = get_list_money()

    get_list_articles()

    user_moneybag_id = request.user.moneybag_id

    if request.method == 'POST':
        form = OperationsForm(request.POST, request.FILES)

        if form.is_valid():
            operation = form.save(commit=False)
            operation.user = request.user
            operation.reports = request.POST['reports']
            operation.save()

            add_outcome(form, user_moneybag_id)

            # form.save()
            messages.success(request, 'Отчёт успешно отправлен')
            return redirect('home')
        else:
            print('Ошибка отправки finatblo')
    else:
        form = OperationsForm()

    context = {
        'title': 'Отчёты',
        'form': form,
        'deal_names': deal_names,
        'counterparty_names': counterparty_names,
        'money_name': money_name,
    }
    return render(request, 'mainapp/home.html', context)


def reports_user(request):
    user_operations = Operations.objects.filter(user=request.user)

    context = {
        'title': 'Мои отчёты',
        'user_operations': user_operations,
    }
    return render(request, 'mainapp/reports_users.html', context)