from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as alogin

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if username == "" or email == "" or password == "":
            messages.warning(request, "กรุณาป้อนข้อมูลให้ครบ")
            return redirect("/register")
        else:
            if User.objects.filter(username=username).exists():
                messages.warning(request, "ชื่อผู้ใช้ถูกใช้งานแล้ว")
                return redirect("/register")
            else:
                user = User.objects.create(
                    username=username, email=email, password=password
                )
                user.save()
                messages.success(request, "สร้างบัญชีผู้ใช้เรียบร้อย")
                return redirect("/register")
    else:
        return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "" or password == "":
            messages.warning(request, "กรุณาป้อนข้อมูลให้ครบ")
            return redirect("/login")

        else:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                alogin(request, user)
                return redirect("/")
            else:
                messages.warning(request, "ไม่พบข้อมูลผู้ใช้")
                return redirect("/login")

            # try:
            #     password_auth = User.objects.get(username=username)

            #     if password != password_auth.password:
            #         messages.warning(request, "รหัสผ่านหรือชื่อผู้ใช้งานไม่ถูกต้อง")
            #         return redirect("/login")

            # except User.DoesNotExist:
            #     messages.warning(request, "รหัสผ่านหรือชื่อผู้ใช้งานไม่ถูกต้อง")
            #     return redirect("/login")

    else:
        return render(request, "login.html")


def logout(request):
    pass
