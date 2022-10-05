from django import views
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import UserForm, LoginForm


class RegisterView(views.View):
    form_class = UserForm
    template_name = "register.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            print(form.errors)
            return render(request, self.template_name, {"form": form})
        form.save()
        return redirect("/")


class LoginView(views.View):
    form_class = LoginForm
    template_name = "login.html"
    success_redirect = "/"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if not user:
            return redirect("login")
        login(request, user)
        return redirect(self.success_redirect)


class LogoutView(views.View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")