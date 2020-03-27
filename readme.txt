Для развертывани приложения через docker нужно

переименовать 
.env.temp -> .env
заплнить переменые.
выполнить docker-compose build
после сборки выполнить команду:
    make migr

выполнить docker-compose up
приложение должно запустится.




ссылки и методы.
регистрация ползователя.
register user
http://127.0.0.1:8001/djoser-auth/users/

json: method post

{
    "username": "",
    "password": ""
}

получение токена
login user
http://127.0.0.1:8001/djoser-auth/token/login/
json method post:
{
    "username": "",
    "password": ""
}

создание приложения
http://127.0.0.1:8001/api/apikey/create/
json post:

{
    "name": "app name test"
}

апдейт api key
http://127.0.0.1:8001/api/apikey/update/1/
json method put

{
    "detail": "Authentication credentials were not provided."
}


{
    "name": "app name test"
}


данные о приложении по api-key
http://127.0.0.1:8001/api/test/api-key/
method get

