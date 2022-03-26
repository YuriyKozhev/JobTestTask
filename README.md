# Job test task

### Original wording
```
Написать программу, состоящую из следующих компонентов: 
Все компоненты должны быть обёрнуты в docker-контейнер. 
БД: MySQL
Брокер сообщений: RabbitMQ
Контейнеризация: docker-ce 
1) Продюсер
Обязанность которого сканировать папку и в случае появления там файлов передавать сообщение через брокера RabbitMQ в случае, если файл текстовый, то в очередь "Parsing", иначе в очередь "Errors".
2) Консумер "Parser":
Слушает очередь "Parsing". Его цель считывать содержимое файла и подсчитывать количество буквенных слов и заносить количество в базу. Если в базе есть данное слово, то прибавить к количеству новое число.
3) Консумер "Error Handler":
Слушает очередь "Errors". Его обязанность оповещать администратора по почте в случае получения сообщения из очереди.
4) Модуль записи в CSV:
Чтение данных, записанных в базе. При достижении n слов и более удалять запись из базы и заносить в csv таблицу: слово, которое преодолело лимит, имена файлов, которые содержали это слово. Запись делать в новой строке каждый раз при достижении n слов.

Дополнительно:
Модуль генерации файлов:
Должен проводить вебскрапинг по указанному сайту и текстовое содержимое страниц записывать в файлы для Продюсера.
```

### Requirements
- All components should be executed inside a Docker container
- Containerization: Docker CE
- Database: MySQL
- Message broker: RabbitMQ

### Description
- `Producer scans a folder. 
When there is a file in the folder, Producer sends a message in a queue via RabbitMQ broker. 
In case of a text file, the queue is 'Parsing'; otherwise it is 'Errors'.`
- `'Parser' consumer listens to the 'Parsing' queue. 
'Parser' reads the content of a file, 
counts the numbers of words consisting of alphabetic characters
and write them to a database. 
If there is already the given word in the database, 
the corresponding number is added to the existing one.`
- `'Error Handler' consumer listens to 'Errors' queue. 
'Error Handler' sends an e-mail notification to an admin 
when a message from the queue is received.`
- `CSV-writer module reads the data from the database. 
When the number of occurences for a word is greater then or equal to n
the module deletes the corresponding database entry. 
And then the module appends a new line to a CSV-file with
the word under consideration and the names of the files that contain it.
The module always appends a new line regardless of whether or not the csv-file contains the given word.`
- `Files generation module perfoms web scrapping.
The module retrieves text content of the pages from the given website 
and saves it to files for Producer.`

### Stack
- Python 3.10
- Docker Desktop 4.3.0
- MySQL 8.0
- RabbitMQ 3.9.14