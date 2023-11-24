let intervalId;

function updateLatestReadings() {
    if (document.visibilityState === 'visible' && window.location.pathname === '/') {
        $.get('/latest_readings/', function(data) {
            const latestReadings = data.latest_readings;

            for (let i = 0; i < latestReadings.length; i++) {
                const reading = latestReadings[i];
                const deviceNumber = i + 1;

                // Update the content
                $(`#temperature${deviceNumber}`).text(reading.Temperature);
                $(`#humidity${deviceNumber}`).text(reading.Humidity);
                $(`#location${deviceNumber}`).text(reading.Location);
            }
        });
    }
}


// Periodically update readings every 1 second
intervalId = setInterval(updateLatestReadings, 1000);

// Stop updating when the page is not visible
document.addEventListener('visibilitychange', function() {
    if (document.visibilityState === 'hidden') {
        clearInterval(intervalId);
    } else {
        intervalId = setInterval(updateLatestReadings, 1000);
    }
});


// Create the chart
const graph_plot = () => {
    $.get('/all_readings/', function(data) {
        const allReadings = data.all_readings;

        allReadings.forEach(sensorReading => {
            const sensor = sensorReading.Sensor;
            const readings = sensorReading.Readings;

            console.log(`Sensor ID: ${sensor.Node_id}`, readings); // Log readings to the console

            if (readings.length > 0) {
                const labels = readings.map((reading, index) => ` ${index + 1}`);
                const temperatureData = readings.map(reading => reading.Temperature);
                const humidityData = readings.map(reading => reading.Humidity);

                const canvas = document.createElement('canvas');
                canvas.id = `sensorGraph-${sensor.Node_id}`;
                document.getElementById('graphs-container').appendChild(canvas);

                const ctx = canvas.getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                label: `Sensor ID: ${sensor.Node_id} - Temperature`,
                                data: temperatureData,
                                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                                borderColor: 'rgba(255, 99, 132, 1)',
                                borderWidth: 1
                            },
                            {
                                label: `Sensor ID: ${sensor.Node_id} - Humidity`,
                                data: humidityData,
                                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                                borderColor: 'rgba(54, 162, 235, 1)',
                                borderWidth: 1
                            }
                        ]
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            }
        });
    });
};

$(document).ready(function() {
    setTimeout(function() {
        graph_plot();
    }, 1000);
});

$(document).ready(function() {
    setTimeout(function() {
        graph_plot();
    }, 1000);
});