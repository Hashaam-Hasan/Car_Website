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
    # Web pages
    path('', views.se_project, name='landing_page'),  # Landing page URL
    # path('login/', views.login_view, name='login'),
    # path('', views.se_project, name='se_project'),  # Landing page
    path('marketplace/', views.market_place, name='market_place'),
    path('selling/', views.selling_page, name='selling_page'),
    path('account/', views.user_account_page, name='user_account_page'),
    path('about/', views.about_us, name= 'about_us'),
    path('contribution', views.contribution, name= 'contribution'),
    # # Ye sara login page ka kaam
    # path('login/', views.login_view, name='login'),
    # path('signup/', views.signup_view, name='signup'),



    path('favorites/<int:car_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('user/favorites/', views.favorite_cars, name='favorite_cars'),

    
    # path('list_car/', views.list_car, name='list_car'),
    # path('success/', views.success, name='success'),


]

