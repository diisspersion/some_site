document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const payload = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        // Пытаемся распарсить ответ как JSON в любом случае
        const data = await response.json();

        if (response.ok) {
            // Если сервер прислал ссылку для редиректа — переходим
            if (data.redirect_url) {
                window.location.href = data.redirect_url;
            }
        } else {
            // Обработка ошибки 401 или других
            alert(`Error: ${data.detail || 'Login failed'}`);
        }
    } catch (error) {
        console.error('Network or Parsing Error:', error);
        alert('Connection error. Please check server logs/console.');
    }
});