from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User
from .models import Bookings,Food,FoodBookings,Train

def train(request):
    obj=Train.objects.all()
    return render(request,"auctions/train.html",{"train":obj})

def order(request,listing_id):
    if(request.method=='POST'):
        order= Food.objects.get(pk=listing_id)
        user=request.user
        order_by=request.POST['name']
        item,created=Food.objects.get_or_create(name=request.POST['item'])
        date=request.POST['date']
        count=request.POST['co']
        contact=request.POST['contact']
        train=request.POST['Train']
        seat=request.POST['seat']
        station=request.POST['Station']
        # bookings=Bookings(user=user,From=from_add,to=to_add,Date=date,Count=count,mobile=contact)
        order=FoodBookings(user=user,name=item,order_by=order_by,phn=contact,train_no=train,seat_no=seat,station=station,count=count,journey_date=date)
        order.save()
        return render(request,"auctions/food.html")
    else:
        order= Food.objects.get(pk=listing_id)
        return render(request,"auctions/order.html",{"food":order})
def index(request):
    if(request.method=='POST'):
        # print()
        Train_no,created=Train.objects.get_or_create(train_no=request.POST['no'])
        user=request.user
        from_add=request.POST['from_add']
        to_add=request.POST['to_add']
        date=request.POST['date']
        count=request.POST['count']
        contact=request.POST['contact']
        bookings=Bookings(user=user,train_no=Train_no,From=from_add,to=to_add,Date=date,Count=count,mobile=contact)
        bookings.save()
        return render(request, "auctions/login.html")
    else:
         return render(request, "auctions/index.html")
def food(request):
    book=Food.objects.all()
    return render(request,"auctions/food.html",{"food":book})
def Booking(request):
    book=Bookings.objects.filter(user=request.user)
    # return HttpResponse(book)
    return render(request,"auctions/mybookings.html",{'books': book})
def display_food(request,listing_id):
    order= Food.objects.get(pk=listing_id)
    return render(request,"auctions/display.html",{'i': order})
    # return HttpResponse("HELLO")
def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

def book(request,listing_id):
    id=Train.objects.get(pk=listing_id)
    return render(request, "auctions/train_book.html",{"obj":id})

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "auctions/register.html")
def home(request):
    return render(request, "auctions/home.html")