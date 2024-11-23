from gc import get_objects
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login,logout
from .models import *
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import authenticate 


from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FoodItem, Cart

# View for displaying the menu
def menu(request):
    food_items = FoodItem.objects.all()
    return render(request, 'menu.html', {'food_items': food_items})

# View for adding an item to the cart
@login_required
def add_to_cart(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, food_item=food_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('menu')  # Redirect back to menu after adding to cart

# Create your views here.
def login_view(request):
    context={}
    if request.method == 'POST':
        username= request.POST.get('username')     
        password= request.POST.get('password')  
        print(username,password) 
        user= authenticate(username=username,password=password) 
             
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            context= {"MSG": "Invalid Credentials"}
    return render(request,'login.html',context)


def signup_view(request):
    if request.method == "POST" :
            first_name= request.POST.get("firstname")
            last_name= request.POST.get("lastname")
            email = request.POST.get("email")
            username=request.POST.get("username")
            password=request.POST.get("password")
            print(first_name,last_name,username,email,password,)
            my_user = User.objects.create_user(username=username,password=password,email=email)
            my_user.first_name=first_name
            my_user.last_name=last_name
            my_user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log in the user after signup
                return redirect('home')
    return render(request,'signup.html')


def blog_view(request):
    return render(request,'blog.html')

def services_view(request):
    return render(request,'services.html')

def about_view(request):
   return render(request,'about.html')


def home_view(request):
    return render(request, 'home.html')

def Italian_view(request):
   return render(request,'italian.html')

def Japanese_view(request):
   return render(request,'japanese.html')

def American_view(request):
   return render(request,'american.html')

def Beverages_view(request):
   return render(request,'beverages.html')

def oders_view(request):
   return render(request,'home.html')
def recent_view(request):
   return render(request,'home.html')
def order3months_view(request):
   return render(request,'home.html')
def order6months_view(request):
   return render(request,'home.html')
def alltime_view(request):
   return render(request,'home.html')


def contactus_view(request):
   return render(request,'contactus.html')


def profile_view(request):
   return render(request,'profile.html')

def userdetails_view(request):
    return render(request,'userdetails.html',)




def logout_view(request):
    logout(request)
    return redirect('login')



def del_view(request, id):
    user = User.objects.get(id=id)   

    if request.method == 'POST':
        user.delete()  
        logout(request) 
        return redirect('login')  

    return render(request, 'userdetails.html', {'user': user})  

# def update_view(request, id):
#     user = get_object_or_404(User, id=id) 
#     if request.method == 'POST':
#         user.username = request.POST.get('username', user.username)
#         user.email = request.POST.get('email', user.email)
#         user.first_name= request.POST.get("firstname",user.first_name)
#         user.last_name= request.POST.get("lastname",user.last_name)
#         user.save()
#         messages.success(request, 'Profile updated successfully!')
#         return redirect('userdetails', id=user.id)
#     return render(request, 'userdetails.html', {'user': user})