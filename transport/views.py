from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import TransportScheduleForm, FeedbackForm  # Assuming you have a form for feedback
from .models import TransportSchedule  # Assuming your model for transport schedule is TransportSchedule
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Views for Login, Registration, Transport Schedule, etc.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('schedule_transport')  # Redirect to schedule
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('login_view')

    return render(request, 'transport/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('login_view')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)

    else:
        form = UserCreationForm()

    return render(request, 'transport/register.html', {'form': form})


def schedule_transport(request):
    if request.method == 'POST':
        form = TransportScheduleForm(request.POST)
        if form.is_valid():
            transport = form.save()
            request.session['last_transport_id'] = transport.id
            messages.success(request, 'Transport schedule created successfully!')
            return redirect('confirmation')
    else:
        form = TransportScheduleForm()

    return render(request, 'transport/schedule.html', {'form': form})


def confirmation(request):
    transport_id = request.session.get('last_transport_id')
    if transport_id:
        transport_schedule = TransportSchedule.objects.get(id=transport_id)
    else:
        transport_schedule = None

    return render(request, 'transport/confirmation.html', {'transport_schedule': transport_schedule})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')  # 🔁 Looks for a URL named 'login_view'




# Home View
@login_required
def home(request):
    return render(request, 'transport/home.html')
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import TransportSchedule
from .forms import TransportScheduleForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import TransportSchedule
from .forms import TransportScheduleForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import TransportSchedule
from .forms import TransportScheduleForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import TransportSchedule
from .forms import TransportScheduleForm

def edit_transport(request, transport_id):
 
    transport = get_object_or_404(TransportSchedule, id=transport_id)

    if request.method == 'POST':
        form = TransportScheduleForm(request.POST, instance=transport)
        
        if form.is_valid():
            form.save()
            return redirect('schedule_list') 
    else:
      
        form = TransportScheduleForm(instance=transport)

    return render(request, 'transport/edit_transport.html', {'form': form})




from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import TransportSchedule

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TransportSchedule

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TransportSchedule
def cancel_transport(request, transport_id):
    # No need to actually cancel anything in the database
    # Just show success message and redirect
    
    # You could add a success message if you're using Django's messages framework
    from django.contrib import messages
    messages.success(request, "Transport booking cancelled successfully!")
    
    # Redirect to the rate_experience view with the same transport_id
    from django.shortcuts import redirect
    return redirect('rate_experience', transport_id=transport_id)
# Static Pages (About, Terms, Privacy, Contact)
from django.shortcuts import render

def terms(request):
    return render(request, 'transport/terms.html')

def about(request):
    return render(request, 'transport/about.html')

def privacy(request):
    return render(request, 'transport/privacy.html')

def contact(request):
    return render(request, 'transport/contact.html')


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required



def contact(request):
    return render(request, 'transport/contact.html')
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages

def rate_experience(request):
    if request.method == 'POST':
        # Get the rating value from the form
        rating = request.POST.get('rating')

        # Save the rating to the database or process it as needed
        # For example, you can associate this rating with the user or a specific transport schedule.
        # Here we're just displaying the rating for demonstration.
        if rating:
            messages.success(request, f"Thank you for your rating: {rating} stars!")
        else:
            messages.error(request, "Please select a rating.")

        # After submitting the rating, redirect to the homepage
        return redirect('home')  # Assuming 'home' is the name of your homepage URL

    return render(request, 'transport/rate_experience.html')

def cancel_transport(request, transport_id):
    # Add success message if using messages framework
    from django.contrib import messages
    messages.success(request, "Transport booking cancelled successfully!")
    
    # Redirect without parameters
    from django.shortcuts import redirect
    return redirect('rate_experience')
