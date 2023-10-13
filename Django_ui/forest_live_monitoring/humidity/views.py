from django.shortcuts import render
from humidity.models import sensorReadings, sensors

def home_view(request):
    # Get the latest sensor reading
    latest_reading = sensorReadings.objects.latest('Timestamp')
    
    # Get the temperature and humidity values from the latest reading
    temperature = latest_reading.Temperature
    humidity = latest_reading.Humidity
    
    # Render the template with the temperature and humidity values
    return render(request, 'home.html', {'temperature': temperature, 'humidity': humidity})
     