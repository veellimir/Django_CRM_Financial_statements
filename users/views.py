from django.shortcuts import render, redirect
from django.contrib import auth, messages

from .forms import UserLoginForm


# def register_user(request):
#     page = 'register'
#     get_list_money()
#
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Добро пожаловать')
#             return redirect('home')
#     else:
#         form = UserRegisterForm()
#
#     context = {
#         'title': 'Регистрация',
#         'page': page,
#         'form': form,
#     }
#     return render(request, 'users/register_login.html', context)

def login_user(request):
    page = 'login'

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)

                messages.success(request, f'Здравствуйте {user}')
                return redirect('home')
    else:
        form = UserLoginForm()
    context = {
        'title': 'Войти',
        'page': page,
        'form': form,
    }
    return render(request, 'users/register_login.html', context)


def logout_user(request):
    auth.logout(request)
    messages.success(request, 'Вы вышли')
    return redirect('login')