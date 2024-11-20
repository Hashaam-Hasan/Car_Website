from django.shortcuts import render

# Landing Page
def se_project(request):
    return render(request, 'se_project.html')

# Market Place Page
def market_place(request):
    return render(request, 'market_place.html')

# Selling Page
def selling_page(request):
    return render(request, 'selling_page.html')

# User Account Page
def user_account_page(request):
    return render(request, 'user_account_page.html')

def about_us(request):
    return render(request,'about.html')

def contribution(request):
    return render(request, 'cont.html')

def login(request):
    return render(request, 'login.html')