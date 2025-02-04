from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm

# Create your views here.


def register_view(request): 
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'users/register.html',{"form":form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('posts:list')
    else:
       form = AuthenticationForm()
    return render(request, 'users/login.html',{"form":form})

