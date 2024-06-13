from django.shortcuts import render, redirect
from .models import Hall, Seat, Ticket
from .forms import BookingForm
from main.models import GameSchedule


def booking(request):

    hall = Hall.objects.first()
    all_seats = Seat.objects.filter(hall=hall)
    booked_seats = all_seats.filter(booked_by__isnull=False)
    booked_seats_coordinates = [(seat.row, seat.column) for seat in booked_seats]
    game_days = GameSchedule.objects.filter(location=hall)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            game_id = form.cleaned_data['game_id']
            seat_data_content = form.cleaned_data['seat_data']

            for seat in eval(seat_data_content):
                seat = Seat.objects.create(row=seat[0],
                                           column=seat[1],
                                           hall=Hall.objects.first(),
                                           booked_by=request.user if request.user.is_authenticated else None)
                Ticket.objects.create(user=request.user if request.user.is_authenticated else None,
                                               first_name=first_name,
                                               email=email,
                                               game=GameSchedule.objects.get(id=game_id),
                                               phone=phone,
                                               booked_seat=seat)
            
            if request.user.is_authenticated:
                return redirect('tickets')
            else:
                return render(request, 'booking/final.html')
        else:
            return render(request, 'booking/booking.html', context={'form': form,
                                                                    'game_days': game_days,
                                                                    'rows_range': range(1, hall.rows + 1),
                                                                    'columns_range': range(1, hall.columns + 1),
                                                                    'booked_seats_coordinates': booked_seats_coordinates,})

    form = BookingForm(user=request.user)

    context = {
        'game_days': game_days,
        'rows_range': range(1, hall.rows + 1),
        'columns_range': range(1, hall.columns + 1),
        'booked_seats_coordinates': booked_seats_coordinates,
        'form': form,
    }
    return render(request, 'booking/booking.html', context=context)