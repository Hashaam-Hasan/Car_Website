from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# from .models import UserProfile
# from .forms import RegisterForm, LoginForm
from django.contrib import messages

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Car, FavoriteCar

# from .models import UserProfile
from .forms import CarForm


#ye favourite ka h k login k saath hi hoga sirf
from django.shortcuts import render, redirect
from django.http import HttpResponse

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
# def remove_from_favorites(request, car_id):
#     car = Car.objects.get(id=car_id)
#     user = request.user
#     # Remove the car from the user's favorites
#     favorite_car = FavoriteCar.objects.filter(user=user, car=car)
#     if favorite_car.exists():
#         favorite_car.delete()
#     return redirect('user_account')

# User's account page to view favorites
@login_required
def user_account(request):
    user = request.user
    favorite_cars = FavoriteCar.objects.filter(user=user)
    return render(request, 'user_account_page.html', {'favorite_cars': favorite_cars})










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










#ye wali filetr









from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Car, FavoriteCar

# Add car to favorites
@login_required
def add_to_favorites(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    user = request.user
    
    # Check if car is already in the user's favorite list
    if FavoriteCar.objects.filter(user=user, car=car).exists():
        messages.info(request, "This car is already in your favorites!")
        return redirect('market_place')  # Redirect back to marketplace
    
    # Add car to favorites
    FavoriteCar.objects.create(user=user, car=car)
    messages.success(request, "Car added to your favorites!")
    return redirect('market_place')  # Redirect back to marketplace

# Remove car from favorites
@login_required
# def remove_from_favorites(request, car_id):
#     car = get_object_or_404(Car, id=car_id)
#     user = request.user
    
#     # Remove the car from the user's favorites
#     favorite_car = FavoriteCar.objects.filter(user=user, car=car)
#     if favorite_car.exists():
#         favorite_car.delete()
#         messages.success(request, "Car removed from your favorites!")
#     else:
#         messages.info(request, "This car is not in your favorites!")
    
#     return redirect('user_account')  # Redirect to the user's account page

# User's account page to view favorites
@login_required
def user_account(request):
    user = request.user
    favorite_cars = FavoriteCar.objects.filter(user=user)
    return render(request, 'user_account_page.html', {'favorite_cars': favorite_cars})

# Toggle favorite status (AJAX for like/unlike functionality)
@login_required
def toggle_favorite(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    favorite, created = FavoriteCar.objects.get_or_create(user=request.user, car=car)
    
    if not created:
        favorite.delete()  # If it already exists, unfavorite it
        return JsonResponse({'favorited': False})
    
    return JsonResponse({'favorited': True})

















from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Car, FavoriteCar

# Add car to favorites
@login_required
def add_to_favorites(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    user = request.user
    
    # Check if car is already in the user's favorite list
    if FavoriteCar.objects.filter(user=user, car=car).exists():
        messages.info(request, "This car is already in your favorites!")
        return redirect('market_place')  # Redirect back to marketplace
    
    # Add car to favorites
    FavoriteCar.objects.create(user=user, car=car)
    messages.success(request, "Car added to your favorites!")
    return redirect('market_place')  # Redirect back to marketplace

# Remove car from favorites
@login_required
# def remove_from_favorites(request, car_id):
#     car = get_object_or_404(Car, id=car_id)
#     user = request.user
    
#     # Remove the car from the user's favorites
#     favorite_car = FavoriteCar.objects.filter(user=user, car=car)
#     if favorite_car.exists():
#         favorite_car.delete()
#         messages.success(request, "Car removed from your favorites!")
#     else:
#         messages.info(request, "This car is not in your favorites!")
    
#     return redirect('user_account')  # Redirect to the user's account page

# User's account page to view favorites
@login_required
def user_account(request):
    user = request.user
    favorite_cars = FavoriteCar.objects.filter(user=user)
    return render(request, 'user_account_page.html', {'favorite_cars': favorite_cars})

# Toggle favorite status (AJAX for like/unlike functionality)
@login_required
def toggle_favorite(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    favorite, created = FavoriteCar.objects.get_or_create(user=request.user, car=car)
    
    if not created:
        favorite.delete()  # If it already exists, unfavorite it
        return JsonResponse({'favorited': False})
    
    return JsonResponse({'favorited': True})











from django.shortcuts import render
from django.db.models.functions import Lower
from .models import FavoriteCar

def user_account_page(request):
    if request.user.is_authenticated:
        favorite_cars = FavoriteCar.objects.filter(user=request.user).select_related('car')
        unique_brands = (
        FavoriteCar.objects.filter(user=request.user)
        .values_list('car__brand_name', flat=True)
        .distinct()
    )
    else:
        favorite_cars = []

    context = {
        'favorite_cars': favorite_cars,
        'unique_brands': unique_brands,
    }
    return render(request, 'user_account_page.html', context)


# def user_account_page(request):
#     favorites = FavoriteCar.objects.filter(user=request.user).select_related('car')
#     unique_brands = (
#         FavoriteCar.objects.filter(user=request.user)
#         .values_list('car__brand_name', flat=True)
#         .distinct()
#     )
#     context = {
#         'favorites': favorites,
#         'unique_brands': unique_brands,
#     }
#     return render(request, 'user_account_page.html', context)








# #for removing fav in user
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from .models import FavoriteCar

# def remove_from_favorite(request, favorite_id):
#     if request.method == 'POST':
#         favorite = get_object_or_404(FavoriteCar, id=favorite_id, user=request.user)
#         favorite.delete()
#         return JsonResponse({'success': True, 'message': 'Removed from favorites.'})
#     return JsonResponse({'success': False, 'message': 'Invalid request.'})




def car_search_results(request):
    query = request.GET.get('title', '').strip()  # Get the title from the request
    cars = Car.objects.filter(title__icontains=query) if query else Car.objects.all()  # Filter or show all
    return render(request, 'car_search_results.html', {'cars': cars, 'query': query})




def search_cars(request):
    query = request.GET.get('query', '').strip()
    if query:
        cars = Car.objects.filter(title__icontains=query)
        car_list = [
            {
                'title': car.title,
                'brand': car.brand_name,
                'model': car.model,
                'year': car.year,
                'mileage': car.mileage,
                'price': car.price,
            }
            for car in cars
        ]
        return JsonResponse({'results': car_list})
    return JsonResponse({'results': []})