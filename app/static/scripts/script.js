document.getElementById('loginForm').addEventListener('submit', async function(event) {
    // Prevent the default form submission (page reload)
    event.preventDefault();

    // Collect form data and convert it into a plain JavaScript object
    const formData = new FormData(this);
    const payload = Object.fromEntries(formData.entries());

    try {
        // Send a POST request to the login endpoint
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        // Parse the JSON response body
        const data = await response.json();

        if (response.ok) {
            // Check if the server provided a redirect URL upon successful login
            if (data.redirect_url) {
                window.location.href = data.redirect_url;
            }
        } else {
            // Handle server-side errors (e.g., 401 Unauthorized, 400 Bad Request)
            alert(`Error: ${data.detail || 'Login failed'}`);
        }
    } catch (error) {
        // Handle network issues or JSON parsing failures
        console.error('Network or Parsing Error:', error);
        alert('Connection error. Please check server logs/console.');
    }
});