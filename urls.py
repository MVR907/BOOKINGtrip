from django.contrib import admin
from django.urls import path
from Booking import views
from Bookmytrip import settings
from Bookmytrip.settings import *
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.function),
    path('about',views.about),
    path('services',views.services),
    path('booking',views.booking),
    path('contact',views.contact),
    path('bookingform',views.bookingform),
    path('sucess',views.sucess),
    path('img',views.img),
]
if DEBUG:
	urlpatterns+=static(MEDIA_URL,document_root=MEDIA_ROOT)
