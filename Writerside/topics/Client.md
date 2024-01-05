# Client

Класс `Client` представляет собой клиента, связанного с сервером. Он предоставляет методы для выполнения различных операций с клиентом.

## Конструктор

### Параметры

- `address` (str): Адрес клиента.
- `created_at` (str): Дата и время создания клиента в формате ISO 8601.
- `enabled` (bool): Индикатор, указывающий, включен ли клиент.
- `uid` (str): UID клиента.
- `last_handshake_at` (str): Дата и время последнего "handshake" с клиентом в формате ISO 8601.
- `name` (str): Имя клиента.
- `persistent_keepalive` (str): Значение "persistent keepalive" клиента.
- `public_key` (str): Публичный ключ клиента.
- `transfer_rx` (int): Количество полученных данных в байтах.
- `transfer_tx` (int): Количество переданных данных в байтах.
- `updated_at` (str): Дата и время обновления клиента в формате ISO 8601.
- `session` (aiohttp.ClientSession): Экземпляр `aiohttp.ClientSession` для использования при выполнении HTTP-запросов.
- `server` (Server): Экземпляр `Server`, связанный с клиентом.

## Методы

### enable

- `async def enable(self)`

Включает клиента.

**Вызывает**: `ValueError`, если клиент уже включен.

### disable

- `async def disable(self)`

Отключает клиента.

**Вызывает**: `ValueError`, если клиент уже выключен.

### get_qr_code (в работе)

- `async def get_qr_code(self)`

Получает QR-код для клиента.

**Возвращает**: Экземпляр `aiohttp.ClientResponse`.

### get_configuration

- `async def get_configuration(self)`

Получает файл конфигурации для клиента.

**Возвращает**: Файл конфигурации в виде текста.
