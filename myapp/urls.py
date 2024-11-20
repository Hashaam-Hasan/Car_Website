"""
URL configuration for car project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.se_project, name='se_project'),  # Landing page
    path('marketplace/', views.market_place, name='market_place'),
    path('selling/', views.selling_page, name='selling_page'),
    path('account/', views.user_account_page, name='user_account_page'),
    path('about/', views.about_us, name= 'about_us'),
    path('contribution', views.contribution, name= 'contribution'),
    path('login', views.login, name = 'login')
]

