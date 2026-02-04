document.getElementById('loginForm').addEventListener('submit', async function(event) {
    // 1. Отменяем стандартную отправку формы (чтобы страница не перезагружалась)
    event.preventDefault();

    // 2. Собираем данные из полей формы
    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries()); 
    // В data теперь лежит объект: { username: "ваше_имя", password: "ваш_пароль" }

    try {
        // 3. Отправляем запрос на сервер
        const response = await fetch('/login', { // Укажите ваш URL (например, http://localhost:8000/login)
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Обязательно указываем, что это JSON
            },
            body: JSON.stringify(data) // Превращаем объект JS в строку JSON
        });

        // 4. Обрабатываем ответ
        if (response.ok) {
            const result = await response.json();
            console.log('Успех:', result);
            alert('Вы успешно вошли!');
            // Здесь можно сделать редирект, например:
            // window.location.href = '/dashboard'; 
        } else {
            const error = await response.json();
            alert('Ошибка: ' + (error.detail || 'Неверный логин или пароль'));
        }
    } catch (error) {
        console.error('Ошибка сети:', error);
        alert('Не удалось соединиться с сервером');
    }
});