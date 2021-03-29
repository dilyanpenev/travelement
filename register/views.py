from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponseRedirect


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/posts")
    else:
        if response.user.is_authenticated:
            return HttpResponseRedirect("/")
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
