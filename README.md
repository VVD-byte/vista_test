# vista_test
Реализована апи для записной книги с базовой аутинтефикацией, к сожалению не успел реализовать работу с записями (возможна работа с пользоателем и книгми пользователя) </br></br>
Подготовка: </br>
    -в vista_test.service поменять дирректории и пользоателя </br>
    -в config.yaml указать данные для подключения к бд </br>
    -создать бд - ```sudo mysql```, затем в оболочке mysql - ```create database vista``` </br>
    -переносим vista_test.service (нужно находиться в дирректории с этим файлом) - ```cp vista_test /etc/systemd/system/``` </br>
    -```sudo systemctl daemon-reload && sudo systemctl enable vista_test.service && sudo systemctl start vista_test.service``` </br>
    -Проверяем работу сервиса - ```sudo systemctl status vista_test.service``` </br></br>
Использование (реализованы методы GET, POST, PUT, DELETE. Все данные передаются в Form Data): </br>
    -работа с пользователем ```/register/``` </br>
    -работа с записными книгами пользователя ```/notebook/``` </br></br>
Приммеры использования лежат в test.txt
