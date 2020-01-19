from django.shortcuts import render, HttpResponse, redirect

from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def add_user(request):
    if(request.method == 'POST'):
        form = UserForm(request.POST)
        if(form.is_valid()):
            u = form.save()
            u.set_password(u.password)
            u.save()
            return HttpResponse('Usuário Cadastrado!')
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', {'form': form})


def user_login(request):
    if(request.method =='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if(user):
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
    return render(request, 'accounts/user_login.html')

def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')
