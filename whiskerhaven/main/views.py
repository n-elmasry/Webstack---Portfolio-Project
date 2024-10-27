from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Listing, Booking
from .forms import ListingForm, BookingForm

# Create your views here.


def home(request):
    query = request.GET.get('location')
    if query:
        listings = Listing.objects.filter(location__icontains=query)
    else:
        listings = Listing.objects.all()

    return render(request, 'main/home.html', {'listings': listings})


@user_passes_test(lambda u: u.is_active and u.is_staff)
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.host = request.user
            listing.save()
            return redirect('listing_detail', listing_id=listing.id)
    else:
        form = ListingForm()

    return render(request, 'main/create_list.html', {'form': form})


@user_passes_test(lambda u: u.is_active and u.is_staff)
def manage_listing(request):
    listing = Listing.objects.all()
    return render(request, 'main/manage_listing.html', {'listings': listing})


@user_passes_test(lambda u: u.is_active and u.is_staff)
def edit_listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('manage_listings')
    else:
        form = ListingForm(instance=listing)
    return render(request, 'main/create_list.html', {'form': form})


@user_passes_test(lambda u: u.is_active and u.is_staff)
def delete_listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    listing.delete()
    return redirect('manage_listings')


def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'main/listing_detail.html', {'listing': listing})


def search_listings(request):
    query = request.GET.get('location')
    if query:
        listings = Listing.objects.filter(location__icontains=query)
    else:
        listings = Listing.objects.all()
    return render(request, 'main/search_listings.html', {'listings': listings})


@login_required
def book_listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    total_price = None

    if not listing.available:
        messages.error(
            request, 'This stay is currently not available for booking.')
        return redirect('listing_detail', listing_id=listing.id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.guest = request.user
            booking.listing = listing

            total_price = booking.calc_total_price()
            booking.total_price = total_price

            # Check for availability
            if not Booking.objects.filter(
                listing=listing,
                start_date__lt=booking.end_date,
                end_date__gt=booking.start_date
            ).exists():
                booking.save()
                total_price = booking.calc_total_price()
                messages.success(request, 'Booking confirmed!')
                return render(request, 'main/book_listing.html', {'listing': listing, 'form': form, 'total_price': total_price})
            else:
                messages.error(
                    request, 'The stay is not available for these dates. Please choose different dates.')
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = BookingForm()

    return render(request, 'main/book_listing.html', {'listing': listing, 'form': form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(guest=request.user)
    return render(request, 'main/my_bookings.html', {'bookings': bookings})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, guest=request.user)
    booking.delete()
    messages.success(request, 'Booking deleted successfully.')
    return redirect('my_bookings')


def about_us(request):
    return render(request, 'main/about_us.html')
