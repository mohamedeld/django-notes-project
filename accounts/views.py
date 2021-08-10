from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Profile
from django.contrib import messages
from .forms import UserForm,ProfileForm
# Create your views here.
def home(request):
    return HttpResponse('hello world')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)

            return redirect('/notes')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{
        'form':form,
    })


def profile(request,slug):
    profile = get_object_or_404(Profile,slug=slug)

    return render(request,'profile.html',{
        'profile':profile,
    })

def edit_profile(request,slug):
    profile = get_object_or_404(Profile,slug=slug)
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            new_profile = profile_form.save()

            messages.success(request, 'Your Profile Updated Successfully')
            #new_profile.user = request.user
            #new_profile.save()
            return redirect('/')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance = profile)


    return render(request,'edit_profile.html',{
        'user_form':user_form,
        'profile_form':profile_form,
        'profile':profile,
    })

def change_password(request,slug):
    profile = get_object_or_404(Profile,slug=slug)

    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user,request.POST)
        if password_form.is_valid():
            password_form.save()
            return redirect('/')

    else:
        password_form = PasswordChangeForm(request.user)

    return render(request,'change_password.html',{
        'password_form':password_form,
        'profile': profile,
    })
