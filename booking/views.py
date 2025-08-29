from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from booking.models import TravelOption, Booking
from .forms import UserUpdateForm, CustomUserCreationForm, BookingForm
# Create your views here.


def home_view(request):
    """Public home page - accessible to everyone"""
    return render(request, 'home.html')


@login_required
def travel_view(request):
    """Travel options page - requires login"""
    travels = TravelOption.objects.all().order_by('date_time')

    # Filtering logic based on GET parameters
    travel_type = request.GET.get('type', '')
    source = request.GET.get('source', '')
    destination = request.GET.get('destination', '')

    if travel_type:
        travels = travels.filter(type=travel_type)
    if source:
        travels = travels.filter(source__icontains=source)
    if destination:
        travels = travels.filter(destination__icontains=destination)

    context = {'travels': travels}
    return render(request, 'travel.html', context)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, "Registration successful!")
            return redirect('travel') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})

@login_required
def create_booking(request, travel_id):
    travel_option = get_object_or_404(TravelOption, id=travel_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            number_of_seats = form.cleaned_data['number_of_seats']
            
            # Check if enough seats are available
            if number_of_seats > travel_option.available_seats:
                messages.error(request, f'Only {travel_option.available_seats} seats available.')
                return render(request, 'create_booking.html', {
                    'form': form, 
                    'travel_option': travel_option
                })
            
            # Calculate total price
            total_price = travel_option.price * number_of_seats
            
            try:
                with transaction.atomic():
                    # Create the booking
                    booking = Booking.objects.create(
                        user=request.user,
                        travel_option=travel_option,
                        number_of_seats=number_of_seats,
                        total_price=total_price
                    )
                    
                    # Update available seats
                    travel_option.available_seats -= number_of_seats
                    travel_option.save()
                    
                    messages.success(request, f'Booking confirmed! Your booking ID is {booking.id}')
                    return redirect('my_bookings')
                    
            except Exception as e:
                messages.error(request, 'An error occurred while creating the booking.')
                return render(request, 'create_booking.html', {
                    'form': form, 
                    'travel_option': travel_option
                })
    else:
        form = BookingForm()
    
    return render(request, 'create_booking.html', {
        'form': form, 
        'travel_option': travel_option
    })

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        if booking.status == 'Confirmed':
            try:
                with transaction.atomic():
                    # Update booking status
                    booking.status = 'Cancelled'
                    booking.save()
                    
                    # Return seats to available count
                    travel_option = booking.travel_option
                    travel_option.available_seats += booking.number_of_seats
                    travel_option.save()
                    
                    messages.success(request, 'Booking cancelled successfully!')
                return redirect('my_bookings')
            except Exception as e:
                messages.error(request, 'An error occurred while cancelling the booking.')
        else:
            messages.warning(request, 'This booking is already cancelled.')
    
    return render(request, 'cancel_booking.html', {'booking': booking})