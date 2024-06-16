from django.core import mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.conf import settings


from .models import Hall, Seat, Ticket
from .forms import BookingForm
from main.models import GameSchedule


def booking(request):

    hall = Hall.objects.first()
    booked_seats = Seat.objects.filter(hall=hall)
    booked_seats_coordinates = [(seat.row, seat.column) for seat in booked_seats]
    game_days = GameSchedule.objects.filter(location=hall)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            game_id = form.cleaned_data['game_id']
            seat_data_content = eval(form.cleaned_data['seat_data'])

            if not is_tuple_of_tuples(seat_data_content):
                seat_data_content = (seat_data_content,)

            for seat in seat_data_content:
                seat = Seat.objects.create(row=seat[0],
                                           column=seat[1],
                                           hall=Hall.objects.first(),
                                           booked_by=request.user if request.user.is_authenticated else None)
                ticket = Ticket.objects.create(user=request.user if request.user.is_authenticated else None,
                                               first_name=first_name,
                                               email=email,
                                               game=GameSchedule.objects.get(id=game_id),
                                               phone=phone,
                                               booked_seat=seat)

                send_mail(subject=f'{first_name}, благодарим за заказ!',
                          to=email,
                          template='mail/send_ticket.html',
                          context={'ticket': ticket})
            
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


def send_mail(subject, to, template, context):
    subject = subject
    html_message = render_to_string(template, context=context)
    from_email = settings.EMAIL_HOST_USER
    to = to

    mail.send_mail(subject, '', from_email, [to], html_message=html_message)


def is_tuple_of_tuples(variable):
    if isinstance(variable, tuple):
        return all(isinstance(item, tuple) for item in variable)
    return False