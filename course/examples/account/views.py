from django.shortcuts import redirect, render


def login_request(request):
    return render(request, 'account/login.html')


def register_request(request):
    return render(request, 'account/register.html')


def logout(request):
    return redirect('index')
