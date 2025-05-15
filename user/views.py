from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    message = ""
    username = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)

        # 驗證帳號密碼
        user = authenticate(request, username=username, password=password)
        if not user:
            message = "Invalid username or password!"
        else:
            message = "Login successful!"
            login(request, user)
            return redirect("todo_list")

    return render(
        request, "user/login.html", {"message": message, "username": username}
    )


def user_logout(request):
    logout(request)
    return redirect("todo")


# Create your views here.
def user_register(request):
    message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(username, password1, password2)

        if password1 != password2:
            message = "Passwords do not match!"

        elif len(password1) < 8:
            message = "Password must be at least 8 characters long!"

        else:
            # 是否重複
            user = User.objects.filter(username=username)
            if user:
                message = "Username already exists!"
            else:
                # 創建帳號
                user = User.objects.create_user(username=username, password=password1)
                user.save
                message = "Registration successful!"
    else:
        form = UserCreationForm()

    return render(request, "user/register.html", {"form": form, "message": message})
