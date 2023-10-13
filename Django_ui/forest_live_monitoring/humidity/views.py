from django.shortcuts import render
from humidity.models import sensorReadings, sensors

def home_view(request):
    # Get the latest sensor reading
    latest_reading = sensorReadings.objects.latest('Timestamp')
    context = {
        'latest_reading': latest_reading
    }
    
    # Render the template with the temperature and humidity values
    return render(request, 'home.html', context)
     