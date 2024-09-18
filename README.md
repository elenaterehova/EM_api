# GitHub API
Автоматический тест для проверки работы с GitHub API на языке Python. 
Тест создает, проверяет наличие и удаляет репозиторий на GitHub. 

## Установка
1. Склонируйте репозиторий
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Создайте виртуальную среду и активируйте ее
   ```sh
   python -m venv venv
   'venv\Scripts\activate'
   ```
2. Установите зависимости
   ```sh
    pip install -r requirements.txt
   ```
3. Создайте файл .env в корневом каталоге проекта и укажите в нем свои переменные окружения
   ```sh
    USER_NAME = "..."
    TOKEN = "..."
    REPO_NAME = "..."
   ```
4. Запустите тестовый скрипт
   ```sh
    python test_api.py
   ```