from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import Registration_Form, Login_Form
from django.contrib.auth import authenticate, login, logout
from .models import Custom_User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import random

# Create your views here.
def registration(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = Registration_Form()
    if request.method == 'POST':
        form = Registration_Form(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('login')
        print(form.errors)
    return render(request, 'account/registration.html', {'form': form})


def Login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = Login_Form()
    if request.method == 'POST':
        data = Login_Form(request.POST)
        print(data)
        username = data.cleaned_data['username']
        password = data.cleaned_data['password']
        if not Custom_User.objects.filter(username=username).exists():
            messages.warning(request, 'Invalid Username!')
            return redirect(request.META['HTTP_REFERER'])
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, "Password Doesn't Match!")
            return redirect(request.META['HTTP_REFERER'])
    
    return render(request, 'account/login.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('login')

def forget_password(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        otp = random.randint(111111, 999999)
        email = request.POST['email']
        if Custom_User.objects.filter(email=email).exists():
            user = get_object_or_404(Custom_User, email=email)
            user.otp = otp
            user.save()
            
            subject = "OTP Verificatino For Forget Password!"
            message = f"""Dear User,
            Your OTP is: {otp}
            """
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            
            return render(request, 'account/reset_password.html', {'email': email})
        else:
            messages.warning(request, 'Email Address Does Not Exists!')
            return redirect(request.META['HTTP_REFERER'])
    return render(request, 'account/forget_password.html')

def reset_password(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        email = request.POST['email']
        otp = request.POST['otp']
        password = request.POST['password']
        
        user = get_object_or_404(Custom_User, email=email)
        if user.otp != otp:
            messages.warning(request, 'Wrong OTP!')
            return redirect(request.META['HTTP_REFERER'])
        
        user.set_password(password)
        user.save()
        messages.success(request, 'Password Reset Successfully!')
        return redirect('login')
    return redirect('login')

