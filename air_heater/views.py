from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Temperature
import redis
from django.http import JsonResponse
from django.utils import timezone

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def live_temperature(request):
    value = r.get("latest_temperature") or "N/A"
    ts = r.get("latest_temperature_ts") or timezone.localtime().isoformat()
    return JsonResponse({
        "value": value,
        "ts": ts
    })
def index(request):
    return render(request, "air_heater/index.html")

@login_required
def temperature(request):
    temps = Temperature.objects.order_by("created_at")
    labels = [t.created_at.strftime("%H:%M") for t in temps]
    data = [t.value for t in temps]


    return render(request, "air_heater/temperature.html", {
        "labels": labels,
        "data": data,

    })








def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "air_heater/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("temperature")
    return render(request, "air_heater/login.html")

def user_logout(request):
    logout(request)
    return redirect("index")
