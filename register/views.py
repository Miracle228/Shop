from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth import login as auth_login
from .forms import LoginForm,RegisterForm
# Create your views here.


def login(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" :form
    }
    if form.is_valid():
        print("loged in")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username = username, password=password)
        if user is not None:
            auth_login(request, user)
            context['form']=LoginForm
            return redirect("/homepage")
        else:
            print("error")
    return render (request,"register/login_page.html",context)

User = get_user_model()

def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" :form
    }
    if form.is_valid():
        print("register page")
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
    return render (request,"register/register_page.html",context)

def homepage(request):
    context = {
        "title": "You are in homepage",
    }
    if request.user.is_authenticated:
        context["users_content"] = "You are loged in"
    return render(request, "register/home_page.html",context)

def base(request):

    return render(request, "register/base.html",)
