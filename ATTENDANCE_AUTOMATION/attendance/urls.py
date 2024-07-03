from django.urls import path

from . import views

app_name = "attendance"

urlpatterns = [
    path("",views.index,name="index"),
    path("register",views.register,name="register"),
    path("attendance",views.take_attendance,name="take_attendance")
]