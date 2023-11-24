from django.shortcuts import render
from .models import sensorReadings, sensors
from django.http import JsonResponse

def home_view(request):
    # Get the latest sensor reading
    sensors_with_latest_readings = []
    # get all sensors
    all_sensors = sensors.objects.all()

    for sensor in all_sensors:
        # Retrieve the latest reading for each sensor
        latest_reading = sensorReadings.objects.filter(Node_id=sensor).latest('Timestamp')

        # Append the sensor and its latest reading to the list
        sensors_with_latest_readings.append((sensor, latest_reading))

    context = {
        'sensors_with_latest_readings': sensors_with_latest_readings
    }
    
    # Render the template with the sensor readings
    return render(request, 'home.html', context)

# create JSON response for the latest readings
def latest_readings(request):
    latest_readings = sensorReadings.objects.select_related('Node_id_id').order_by('-Timestamp')[:4]

    data = []
    for reading in latest_readings:
        data.append({
            'Temperature': reading.Temperature,
            'Humidity': reading.Humidity,
            'Location': f'{reading.Node_id.Latitude}, {reading.Node_id.Longitude}',
        })

    return JsonResponse({'latest_readings': data})
     