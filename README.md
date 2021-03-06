# Google API script
Данное приложение разработано в качестве тестового задания

## Запуск проекта
```
git clone https://github.com/krestovsky13/Script-Google-API
docker-compose build
docker-compose up -d
```
### About
Скрипт получает данные с документа при помощи Google API, сделанного в [Google Sheets](https://docs.google.com/spreadsheets/d/1ePBybqdcsNvbyiLHFNkAJ1iA1ln0Yw1OaGUwTB-xxrk/edit#gid=525364213), которые добавляются в БД (на основе PostgreSQL), в том же виде, что и в файле–источнике, с добавлением колонки «стоимость в руб.» Данные для перевода $ в рубли берутся по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).
    
Также разработан функционал проверки соблюдения «срока поставки» из таблицы. В случае, если срок прошел, скрипт отправляет уведомление в Telegram. ***(Для этого необходимо вставить свои API_ID и API_HASH в .env, раскомментировать строки 45 и 47 в kanalservis_script/postg.py и поменять номера на действующие в kanalservis_script/mes_teleg.py).***
    
В данном проекте предусмотрен доступ к некоторым настройкам через .env файл. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме.

Файл - [Google Sheets](https://docs.google.com/spreadsheets/d/1ePBybqdcsNvbyiLHFNkAJ1iA1ln0Yw1OaGUwTB-xxrk/edit#gid=525364213)
