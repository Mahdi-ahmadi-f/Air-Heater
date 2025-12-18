from django.urls import path
from .views import user_register, user_login, user_logout, index, temperature,live_temperature

urlpatterns = [
    path("", index, name="index"),
# urls.py
    path("api/live-temperature/", live_temperature, name="live_temperature"),

    path("register/", user_register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("temperature/", temperature, name="temperature"),
]

