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


function graph_plot() {
    $.get('all_readings/', function(data) {
        const sensorReadings = data.sensorReadings;

        // Loop through each sensor reading
        sensorReadings.forEach(reading => {
            // Prepare data for the chart
            const labels = reading.values.map((value, index) => `Reading ${index + 1}`);
            const data = reading.values;

            // Create a canvas element for each sensor
            const canvas = document.createElement('canvas');
            canvas.id = `sensorGraph-${reading.sensor}`;
            document.body.appendChild(canvas);

            // Create the chart
            const ctx = canvas.getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: reading.sensor,
                        data: data,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });
    });
}