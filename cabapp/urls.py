from django.contrib import admin
from django.urls import path
from cabapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('book/',views.book_ride,name='book_ride'),
    path('my_rides/',views.my_rides,name='my_rides'),
    path('available_rides/',views.available_rides,name='available_rides'),
    path('accept/<int:ride_id>/',views.accept_ride,name='accept_ride'),
    path('drive_rides/',views.drive_rides,name='drive_rides'),
    path('status/<int:ride_id>/<str:status>/',views.update_status,name='update_status')
]