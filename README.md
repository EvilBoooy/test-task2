# Задание
Создать docker-compose.yml разворачивающий приложение на python с простой реализацией REST API.

## Требования
Решение должно состоять из двух контейнеров:

а) Любая NoSQL DB.

б) Приложение на python, с использованием Flask, которое слушает на порту 8080 и принимает только методы GET, POST, PUT.

в) Создаем значение ключ=значение, изменяем ключ=новое_значение, читаем значение ключа.

г) Вновь созданные объекты должны создаваться, изменяться и читаться из NoSQL DB.

## Установка и запуск
1. Убедитесь, что у вас установлен Docker.
2. Склонируйте репозиторий на свой локальный компьютер:
- `git clone git@github.com:EvilBoooy/test-task2.git`
3. Перейдите в директорию проекта:
- `cd test-task2`
4. Запустите проект с помощью Docker Compose:
  - `docker-compose up`: Это создаст и запустит контейнеры для вашего приложения и базы данных MongoDB.
5. Откройте браузер и перейдите по адресу http://localhost:8080, чтобы использовать приложение.

## Проверка
Вы можете использовать инструменты для отправки HTTP-запросов, такие как cURL, Postman или Python-библиотеки, чтобы проверить, что значения успешно создаются, обновляются и читаются из NoSQL-базы данных.

## Готовый пример для проверки
Например, чтобы создать значение с ключом "mykey" и значением "myvalue", вы можете отправить POST-запрос на / с JSON-телом:
{
  "key": "mykey",
  "value": "myvalue"
}
Аналогично, чтобы обновить значение с ключом "mykey" на новое значение "newvalue", вы можете отправить PUT-запрос на /mykey с JSON-телом:
{
  "value": "newvalue"
}
Чтобы получить значение по ключу "mykey", вы можете отправить GET-запрос на /mykey.
