from django.shortcuts import render,redirect
from .models import Profile,Ride
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        user=User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        Profile.objects.create(
            user=user,
            role=request.POST['role']
        )
        return redirect('login')
    return render(request,'register.html')

def loginuser(request):
    if request.method=='POST':
        user=authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request,user)
            return redirect('home')
    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required
def book_ride(request):
    if request.method=='POST':
        Ride.objects.create(
            customer=request.user,
            pickup_location=request.POST['pickup_location'],
            drop_location=request.POST['drop_location'],
            fare=150
        )
        return redirect('my_rides')
    return render(request,'book_ride.html')


@login_required
def my_rides(request):
    rides=Ride.objects.filter(
        customer=request.user,
    )
    return render(request,'my_rides.html',{'rides':rides})

@login_required
def available_rides(request):
    rides=Ride.objects.filter(
        status='REQUESTED'
    )
    return render(request,'available_rides.html',{'rides':rides})


@login_required
def accept_ride(request,ride_id):
    ride=Ride.objects.get(id=ride_id)
    ride.driver=request.user
    ride.status='ACCEPTED'
    ride.save()
    return redirect('drive_rides')

@login_required
def drive_rides(request):
    ride=Ride.objects.filter(
        driver=request.user
    )
    rides = Ride.objects.filter(driver=request.user)
    return render(request,'drive_rides.html',{'rides':rides})


@login_required
def update_status(request,ride_id,status):
    ride=Ride.objects.get(id=ride_id)
    ride.status=status
    ride.save()
    return redirect('drive_rides') 
