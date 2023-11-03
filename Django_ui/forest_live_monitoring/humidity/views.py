from django.shortcuts import render
from .models import sensorReadings, sensors
from django.http import JsonResponse

# Create your views here.
def home_view(request):
    # Get the latest sensor reading
    latest_reading = sensorReadings.objects.latest('Timestamp')
    sensors_with_latest_readings = []
    # get all sensors
    all_sensors = sensors.objects.all()
    for sensor in all_sensors:
        # Retrieve the latest reading for each sensor
        latest_reading = sensorReadings.objects.filter(Node_id=sensor).latest('Timestamp')
        # Append the sensor and its latest reading to the list
        sensors_with_latest_readings.append((sensor, latest_reading))
    context = {
        'latest_reading': latest_reading,
        'sensors_with_latest_readings': sensors_with_latest_readings
    }
    return render(request, 'home.html', context)


def latest_readings(request):
    latest_readings = sensorReadings.objects.all().order_by('-Timestamp')[:4]
    data = []
    for reading in latest_readings:
        data.append({
            'Temperature': reading.Temperature,
            'Humidity': reading.Humidity,
            'Location': f'{reading.Node_id.Latitude}, {reading.Node_id.Longitude}',
        })
    return JsonResponse({'latest_readings': data})