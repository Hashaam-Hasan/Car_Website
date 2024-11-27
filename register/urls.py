from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin1/', admin.site.urls),
    path('signup',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
]