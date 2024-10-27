from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Listing(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=7, decimal_places=2)
    location = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.guest} booked {self.listing} from {self.start_date} to {self.end_date}"

    def calc_total_price(self):
        days_booked = (self.end_date - self.start_date).days
        return days_booked * self.listing.price_per_day

    class Meta:
        """Ensure no overlapping bookings"""
        unique_together = ('listing', 'start_date', 'end_date')
