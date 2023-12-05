from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


def login_request(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'account/login.html', {
                'error': 'Wrong username or password'
            })
    else:
        return render(request, 'account/login.html')


def register_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if password == repassword:
            if User.objects.filter(username = username).exists():
                return render(request, 'account/register.html', {'error': 'This username is taken'})
            else:
                if User.objects.filter(email = email).exists():
                    return render(request, 'account/register.html', {'error': 'This email is taken'})
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
        else:
            return render(request, 'account/register.html', {'error': 'Passwords not match'})
    else:
        return render(request, 'account/register.html')


def logout_request(request):
    logout(request)
    return redirect('index')
