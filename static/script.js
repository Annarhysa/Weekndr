document.getElementById('inputForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the input value
    var inputValue = document.getElementById('inputField').value;

    // Send the input value to Flask using AJAX
    fetch('/suggest_plans', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: inputValue })
    })
    .then(response => response.json())
    .then(data => {
        // Redirect to the output page with plans data passed as a query parameter
        window.location.href = '/plans?plans=' + encodeURIComponent(JSON.stringify(data.plans));
    })
    .catch(error => console.error('Error:', error));
});
