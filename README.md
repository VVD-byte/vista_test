# vista_test
Подготовка:<\br>
    -в vista_test.service поменять дирректории и пользоателя<\br>
    -в config.yaml указать данные для подключения к бд
    -создать бд - ```sudo mysql```, затем в оболочке mysql - ```create database vista```
    -переносим vista_test.service (нужно находиться в дирректории с этим файлом) - ```cp vista_test /etc/systemd/system/```
    -```sudo systemctl daemon-reload && sudo systemctl enable vista_test.service && sudo systemctl start vista_test.service```
    -Проверяем работу сервиса - ```sudo systemctl status vista_test.service```
Использование:
