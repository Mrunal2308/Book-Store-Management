from django.urls import path

from Account import views

urlpatterns = [

    path("login",views.login_function,name = "login"),

    path("register",views.register_function,name = "register"),

    path("logout",views.logout_function,name = "logout")

]


