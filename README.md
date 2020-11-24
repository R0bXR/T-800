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
./KorolevskiyGrigorianskiyRoBOT.py <login> <password>
```
Опционально возможен запуск в виде скрытого приложения:

```
./KorolevskiyGrigorianskiyRoBOT.py <login> <password> -d
```
Для Windows
```
python3 KorolevskiyGrigorianskiyRoBOT.py <login> <password>
```
или
```
python3 KorolevskiyGrigorianskiyRoBOT.py <login> <password> -d
```
Автоматический запуск при включении компьютера
----------------------------------------------------------
Для Windows:
Необходимо отредактировать файл script.cmd:

```batch
pushd PATH/TO/PyFILE
start python3 KorolevskiyGrigorianskiyRoBOT.py
```
С помощью `WIN+R` открыть "Выполнить" и вписать команду `shell:startup`.
Поместить скрипт в открывшуюся папку и включить автозапуск скрипта.

Для Linux:

См. crontab

Авторы
------

Краскин Григорий <gribok1310@mail.ru>

Хакимов Роберт <ustyanov312018@gmail.com>

Contributors
------------

Гололобов Никита <repero11@hotmail.com>
