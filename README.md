# Поиск дубликатов

Скрипт позволяет найти всех дублирующие файлы в указанной папке и всех подпапках внутри и выдает список найденных файлов.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

~~~
python duplicates.py [путь к папке]
~~~

Пример выполнения программы

~~~
File "bars.py" found in following directories:
    D:\Разработка\devman\bars.py
    D:\Разработка\devman\3_bars-master\bars.py
File "json.txt" found in following directories:
    D:\Разработка\devman\json.txt
    D:\Разработка\devman\11_duplicates-master\json.txt
~~~


Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
