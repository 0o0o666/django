from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def user_login(request):
    message = ""
    if request.method == "POST":
        if request.POST.get("register"):
            return redirect("register")

    if request.POST.get("login"):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "" or password == "":
            message = "帳號密碼不能為空"
        else:
            user = authenticate(request, username=username, password=password)
            if user:
                message = "登入成功"
                login(request, user)
            else:
                message = "帳號密碼錯誤-_-"

    return render(request, "user/login.html", {"message": message})


def usre_register(request):
    message = ""
    form = UserCreationForm()
    print(User.objects.filter(username="maan"))

    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        # 密碼長度8
        if len(password1) != 8 or len(password2) != 8:
            message = "密碼長度不等於8"
            print(password1)

        # 密碼相同
        elif password1 != password2:
            message = "密碼不相同"
            print(password2)
        else:
            # 比對使用者是否存在
            if User.objects.filter(username=username):
                message = "帳號已存在>_<"
            # 註冊使用者
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                message = "註冊成功-_-"

    return render(
        request,
        "user/register.html",
        {"form": form, "message": message},
    )
