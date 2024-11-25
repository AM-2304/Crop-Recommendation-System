$(document).ready(function() {
    // Fetch the district options from the Flask application
    fetch('/get-options')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const districtDropdown = document.getElementById('district-dropdown');

            // Check if districts exist in the response
            if (data.districts && Array.isArray(data.districts)) {
                // Populate the district dropdown
                data.districts.forEach(district => {
                    const option = document.createElement('option');
                    option.value = district;
                    option.text = district;
                    districtDropdown.appendChild(option);
                });
            } else {
                console.error('Invalid data format:', data);
                districtDropdown.innerHTML = '<option value="">No districts available</option>';
            }
        })
        .catch(error => {
            console.error('Error fetching options:', error);
            $('#district-dropdown').html('<option value="">Error loading districts</option>');
        });

    // Handle the form submission
    $('#recommendation-form').submit(function(event) {
        event.preventDefault();
        const formData = $(this).serialize();

        $.ajax({
            url: '/get-recommendation',
            type: 'POST',
            data: formData,
            success: function(data) {
                console.log('Recommendation:', data);
                if (data.error) {
                    $('#recommendation-result').html(`
                        <h2>Error</h2>
                        <p>${data.error}</p>
                    `);
                } else {
                    $('#recommendation-result').html(`
                        <h2>Recommended Crop: ${data.recommended_crop}</h2>
                        <p>Predicted Yield: ${data.predicted_yield}</p>
                    `);
                }
            },
            error: function(error) {
                console.error('Error getting recommendation:', error);
                $('#recommendation-result').text('Error getting recommendation. Please try again later.');
            }
        });
    });
});
