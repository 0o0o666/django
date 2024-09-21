from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    message = ""
    form = UserCreationForm()
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
        # 比對使用者是否存在

        # 註冊使用者

    return render(
        request,
        "user/register.html",
        {"form": form, "message": message},
    )
