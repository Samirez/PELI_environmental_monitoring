from django.shortcuts import render
from .models import sensorReadings, sensors
from django.http import JsonResponse
from django.db.models import Max

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


def latest_readings(request):
    latest_readings = sensorReadings.objects.values('Node_id').annotate(max_timestamp=Max('Timestamp')).order_by('Node_id')

    data = []
    for reading in latest_readings:
        latest_reading = sensorReadings.objects.filter(Node_id=reading['Node_id'], Timestamp=reading['max_timestamp']).first()
        if latest_reading:
            data.append({
                'Temperature': latest_reading.Temperature,
                'Humidity': latest_reading.Humidity,
                'Location': f"{latest_reading.Node_id.Latitude}, {latest_reading.Node_id.Longitude}",
            })

    return JsonResponse({'latest_readings': data})


def graph_view(request):
    all_sensors = sensors.objects.all()
    all_sensorReadings = []

    for sensor in all_sensors:
        sensor_readings = sensorReadings.objects.filter(Node_id=sensor)
        all_sensorReadings.extend(sensor_readings)

    context = {
        'all_sensors': all_sensorReadings
    }
    return render(request, 'graph.html', context)

def all_readings(request):
    all_sensors = sensors.objects.all()
    all_sensorReadings = []

    for sensor in all_sensors:
        sensor_readings = sensorReadings.objects.filter(Node_id=sensor)
        readings = []
        for reading in sensor_readings:
            readings.append({
                'Temperature': reading.Temperature,
                'Humidity': reading.Humidity,
                'Location': f'{reading.Node_id.Latitude}, {reading.Node_id.Longitude}',
            })
        all_sensorReadings.append({
            'Sensor': sensor,
            'Readings': readings
        })

    return JsonResponse({'all_readings': all_sensorReadings})
