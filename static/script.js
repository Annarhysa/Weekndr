function getWeekendPlans() {
    const location = document.getElementById('locationInput').value.trim();

    fetch('/suggest-plans?location=' + location)
        .then(response => response.json())
        .then(data => {
            // Clear any existing plans
            document.getElementById('plans').innerHTML = '';

            // Display the new plans
            for (var plan in data) {
                document.getElementById('plans').innerHTML += plan + ': ' + data[plan] + '<br>';
            }
        });
}
