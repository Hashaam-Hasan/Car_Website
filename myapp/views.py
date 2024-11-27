from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# from .models import UserProfile
# from .forms import RegisterForm, LoginForm
from django.contrib import messages

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

# ye poora login page ka naya kaam
def login_view(request):
    if request.method == "POST":
        username_or_email = request.POST.get("username")
        password = request.POST.get("password")
        
        # Authenticate using either username or email
        user = authenticate(request, username=username_or_email, password=password) \
               or authenticate(request, email=username_or_email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the landing page after successful login
            return redirect('home')  # Replace 'landing_page' with your landing page URL name
        else:
            messages.error(request, "Invalid username/email or password.")
    
    return render(request, "login.html")

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if not User.objects.filter(username=email).exists():
                user = User.objects.create_user(username=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Email already exists.")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'login.html')










from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# from .models import UserProfile
from .forms import CarForm
from django.contrib import messages


from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm

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

# def login(request):
#     return render(request, 'login.html')






# Selling Page with Car Form
def selling_page(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('market_place')
    else:
        form = CarForm()
    return render(request, 'selling_page.html', {'form': form})

# Marketplace to Display Listed Cars
def market_place(request):
    cars = Car.objects.all()  # Fetch all cars from the database
    return render(request, 'market_place.html', {'cars': cars})















#ye favourite ka h k login k saath hi hoga sirf
from django.shortcuts import render, redirect
from .models import Car, FavoriteCar
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Add car to favorites
@login_required
def add_to_favorites(request, car_id):
    car = Car.objects.get(id=car_id)
    user = request.user
    # Check if car is already in the user's favorite list
    if FavoriteCar.objects.filter(user=user, car=car).exists():
        return HttpResponse("This car is already in your favorites!")
    # Add car to favorites
    FavoriteCar.objects.create(user=user, car=car)
    return redirect('marketplace')

# Remove car from favorites
@login_required
def remove_from_favorites(request, car_id):
    car = Car.objects.get(id=car_id)
    user = request.user
    # Remove the car from the user's favorites
    favorite_car = FavoriteCar.objects.filter(user=user, car=car)
    if favorite_car.exists():
        favorite_car.delete()
    return redirect('user_account')

# User's account page to view favorites
@login_required
def user_account(request):
    user = request.user
    favorite_cars = FavoriteCar.objects.filter(user=user)
    return render(request, 'user_account_page.html', {'favorite_cars': favorite_cars})








from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Car, FavoriteCar

@login_required
def toggle_favorite(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    favorite, created = FavoriteCar.objects.get_or_create(user=request.user, car=car)
    if not created:
        favorite.delete()  # If it already exists, unfavorite it
        return JsonResponse({'favorited': False})
    return JsonResponse({'favorited': True})

@login_required
def favorite_cars(request):
    favorites = FavoriteCar.objects.filter(user=request.user)
    return render(request, 'user_account_page.html', {'favorites': favorites})
