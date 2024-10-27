from django.urls import path
from . import views
from .views import edit_listing, delete_listing, delete_booking

urlpatterns = [
    path('', views.home, name='home'),
    path('create_listing/', views.create_listing, name='create_listing'),
    path('manage_listings/', views.manage_listing, name='manage_listings'),
    path('listing/<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path('search_listings/', views.search_listings, name='search_listings'),
    path('edit_listing/<int:listing_id>/', edit_listing, name='edit_listing'),
    path('delete_listing/<int:listing_id>/',
         delete_listing, name='delete_listing'),
    path('listings/<int:listing_id>/book/',
         views.book_listing, name='book_listing'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('bookings/delete/<int:booking_id>/',
         delete_booking, name='delete_booking'),
    path('about-us/', views.about_us, name='about_us'),

]
