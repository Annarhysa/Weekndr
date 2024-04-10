document.addEventListener('DOMContentLoaded', function() {
    const locationInput = document.getElementById('location');
    const suggestionsDiv = document.getElementById('suggestions');

    locationInput.addEventListener('input', function() {
        const inputText = this.value.toLowerCase();
        const suggestions = getFilteredSuggestions(inputText);

        // Clear previous suggestions
        suggestionsDiv.innerHTML = '';

        // Add new suggestions
        suggestions.forEach(function(suggestion) {
            const option = document.createElement('div');
            option.textContent = suggestion;
            option.addEventListener('click', function() {
                locationInput.value = this.textContent;
                suggestionsDiv.innerHTML = '';
            });
            suggestionsDiv.appendChild(option);
        });
    });

    function getFilteredSuggestions(inputText) {
        // Example: Fetch suggestions from a server based on inputText
        const allSuggestions = ['new york', 'los angeles', 'chicago', 'san francisco', 'seattle'];
        return allSuggestions.filter(function(suggestion) {
            return suggestion.toLowerCase().startsWith(inputText);
        });
    }
});
