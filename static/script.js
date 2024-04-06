function getWeekendPlans() {
    const location = document.getElementById('locationInput').value.trim();

    if (!location) {
        alert('Please enter your location.');
        return;
    }

    fetch(`/suggest-plans?location=${encodeURIComponent(location)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch weekend plans');
            }
            return response.json();
        })
        .then(data => {
            const plansDiv = document.getElementById('plans');
            plansDiv.innerHTML = '';

            data.suggested_plans.plans.forEach((plan, index) => {
                const planHeading = document.createElement('h2');
                planHeading.textContent = plan;

                const descriptionParagraph = document.createElement('p');
                descriptionParagraph.textContent = data.suggested_plans.descriptions[index];

                const linkAnchor = document.createElement('a');
                linkAnchor.href = data.suggested_plans.links[index];
                linkAnchor.textContent = 'More Info';

                const planContainer = document.createElement('div');
                planContainer.classList.add('plan');
                planContainer.appendChild(planHeading);
                planContainer.appendChild(descriptionParagraph);
                planContainer.appendChild(linkAnchor);

                plansDiv.appendChild(planContainer);
            });
        })
        .catch(error => {
            console.error('Error fetching weekend plans:', error);
            alert('An error occurred while fetching weekend plans. Please try again later.');
        });
}
