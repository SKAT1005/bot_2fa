# 2FA bot

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- * [Author](#author)

## Description

Данный бот создан для подключения 2FA к сайтам

## Getting Started

Для начала работы требуется провести миграции базы данных командой создать виртуальное окружение командой `python -m venv venv` и активировать его.
Linux/MacOS - `source venv/bin/activate`
Windows = `venv\Scripts\activate.bat`
После чего требуется провести миграцию базы данных
`python manage.py makemigrations`
`python manage.py migrate`

### Installation

Перед началом работы вам требуется установить все зависимости
`pip install -r requirements.txt`

## Usage

Для запуска проекта вам требуется перейти в директорию bot_2fa и выполнить команду `python main.py`

Для проверки правильности введенного кода вам требуется отправить get запрос на сервер. Пример кода:
```
import requests

url = 'http://your_server_ip:8000/verify-user-code/'

data = {
    'id': 'user_unique_id',
    'code': 'code_for_check'
}
response = requests.get(url, data)
print(response.json())
```
Для того, чтобы добавить пользователя в бота, пользователю. требуется перейти по ссылке https://your_bot_link?start=user_unique_id
## Author

* **Skat1005** - *Developer* - [Skat1005](https://github.com/SKAT1005/) - *Python Backend Developer*
