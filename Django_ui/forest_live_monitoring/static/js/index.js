function updateLatestReadings() {
    $.get('/latest_readings/', function(data) {
        const latestReadings = data.latest_readings;

        for (let i = 0; i < latestReadings.length; i++) {
            const reading = latestReadings[i];
            const deviceNumber = i + 1;

            // Update the content
            $('#temperature${deviceNumber}').text(reading.Temperature);
            $('#humidity${deviceNumber}').text(reading.Humidity);
            $('#location${deviceNumber}').text(reading.Location);
        }
    });
}

// Periodically update readings every 1 second
setInterval(updateLatestReadings, 1000);

// Initial update
updateLatestReadings();