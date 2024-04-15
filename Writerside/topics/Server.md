# Server

Класс `Server` представляет собой сервер, который взаимодействует с API. Он предоставляет методы для выполнения различных операций с API.

## Конструктор

### Параметры

- `url` (str): URL адрес wg-easy. Пример: http://wg.example.com:51821
- `password` (str): Пароль для аутентификации.
- `session` (aiohttp.ClientSession, опционально): Экземпляр `aiohttp.ClientSession` для использования при выполнении HTTP-запросов. Если не указан, будет создан новый сеанс.

## Методы

### is_logged_in

- `async def is_logged_in(self) -> bool`

Проверяет, авторизован ли пользователь на сервере.

**Функция возвращает**: True, если пользователь авторизован, иначе False.

### login

- `async def login(self)`

Авторизует пользователя на сервере с использованием указанного пароля.

**Вызывает**: `AlreadyLoggedInError`, если пользователь уже авторизован.

**Возвращает**: Сессию.

### logout

- `async def logout(self)`

Выходит из системы на сервере.

**Вызывает**: `AlreadyLoggedInError`, если пользователь не авторизован.

### get_session

- `async def get_session(self)`

Получает информацию о сессии с сервера.

**Возвращает**: Сессию.

### get_clients

- `async def get_clients(self)`

Получает список клиентов с сервера.

**Возвращает**: Список экземпляров `Client`.

### remove_client

- `async def remove_client(self, uid: str)`

Удаляет клиента с сервера.

**Параметры**:
- `uid` (str): UID клиента для удаления.

### create_client

- `async def create_client(self, name: str)`

Создает нового клиента с указанным именем на сервере.

**Параметры**:
- `name` (str): Имя клиента.

### get_client

- `async def get_client(self, uid: str)`

Получает клиента с сервера с указанным UID.

**Параметры**:
- `uid` (str): UID клиента для получения.

**Возвращает**: Экземпляр `Client`, если найден, иначе None.
