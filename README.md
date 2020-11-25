ПО для автоматического отмечания на занятиях СПб ГУТ
----------------------------------------------------

ПО написано на языке программирования Python3.

Требования
----------

Установка зависимостей:

```
pip3 install -r requirements.txt 
```

Запуск
------
Для Linux/WSL
```
./main.py <login> <password>
```

Для Windows
```
python3 main.py <login> <password>
```

Опционально возможен запуск в фоновом режиме:

Для Linux/WSL
```
./main.py <login> <password> -d
```

Для Windows
```
python3 main.py <login> <password> -d
```

Авторы
------

Краскин Григорий <gribok1310@mail.ru>

Хакимов Роберт <ustyanov312018@gmail.com>

Contributors
------------

Гололобов Никита <repero11@hotmail.com>
