# Итоговый проект "TaskManager" (по умолчанию)

## Описание задания

Реализовать приложение **"TaskManager"** для работы с тасками (задачами).

### Минимальный функционал:

- управление задачами (создание\изменение (в том числе переход по статусам и назначение исполнителя) \удаление)
- управление статусами задачи (создание\изменение (в том числе последовательности статусов) \удаление)
- разделение задач по проектам (+ создание\изменение\удаление проектов)
- разделение задач по спринтам внутри проектов (+создание\изменение\удаление спринтов)
- просмотр истории изменения задач
- оповещение исполнителя об изменении текущего статуса задачи

- должна быть авторизация
- должно быть не менее одной модели. Между моделями (необязательно всеми) должна существовать связь.
- должны быть юнит-тесты
- должно быть rest api и использоваться сериализаторы drf.
- должно быть логирование
- должно быть графическое представление для пользователей, которого хватает для управления функционалом приложения

## Реализация

### Используемые языки, системы и библиотеки:

- Интерпретатор [Python v 3.11](https://www.python.org/).
- Фреймворк [Django v. 4.1.7](https://www.djangoproject.com/).
- СУБД [PostgreSQL 15](https://www.postgresql.org/).
- Модуль [Django REST framework v. 3.14](https://www.django-rest-framework.org/).
- и другие модули [requirements.txt](requirements.txt)

### Работа

#### Общее

Менеджер имеет три основных составляющих модели: **проект**, **спринт** и **задача**. Спринт обязательно принадлежит проекту.
Задача обязательно принадлежит проекту и может принадлежать спринту.

Все пользователи могут просматривать всю информацию в интерфейсе и получать данные с помощью API.
Создавать новые записи могут авторизованные пользователи с правом создания записей в определённой категории.
Редактировать и удалять записи может их автор. Исполнитель задания может изменить дату завершения задания.
Суперпользователь имеет полные права на все действия.

При изменении проекта, спринта или задачи, записывается информация в истории зависимых не закрытых задач,
и отправляется email-оповещение всем авторам и исполнителям зависимых не закрытых спринтов и задач.

По умолчанию, выводится список из десяти записей на страницу. В API - так же - десять записей.

При открытии сайта или выборе пункта меню ***"Главная"*** выводится список незавершенных задач.

#### Проекты

При выборе пункта меню ***"Проекты"*** выводится список незавершенных проектов.
Отфильтровать проекты можно по статусу кнопками: *"Весь список"*, *"Выполнено"*, *"В работе"*.
Авторизованные пользователи могут дополнительно отобрать проекты кнопками *"Автор"* или *"Без отбора"*. В зависимости от прав будет отображена кнопка *"Добавить"*, а также кнопки *"Редактироваь"* и *"Удалить"* у проектов в списке.

При выборе проекта из списка, откроется страница детальной информации. На ней так же будут отображены
списки спринтов и задач проекта. Так же, в зависимости от прав, будут отображены кнопки *"Добавить"*, *"Редактироваь"* и *"Удалить"*.

Проект нельзя закрыть, пока есть не завершенные спринты и задачи. Минимальная дата закрытия вычисляется
исходя из даты создания проекта и дат закрытия спринтов и задач проекта.

Удаление проекта удаляет все зависимые спринты и задачи.

#### Спринты

При выборе пункта меню ***"Спринты"***, выводится список незавершенных спринтов.
Кнопки отображаются согласно правам пользователя. При выборе спринта из списка, откроется страница детальной информации.

Спринт нельзя закрыть, пока есть не завершенные задачи, связанные с ним. Минимальная дата закрытия
вычисляется исходя из даты создания спринта и дат закрытия задач спринта.

Планируемая дата вычисляется, как минимальная от планируемых дат выполнения проекта или спринта.

При удалении спринта, удаляет все связанные с ним задачи.

При редактировании спринта, проект выбирается из списка не закрытых проектов.

При использовании кнопки "Добавить", со страницы детальной информации, в создаваемом сприте
автоматически подставляется проект текущего спринта.

#### Задачи

При выборе пункта меню ***"Задачи"***, выводится список незавершенных задач. Кнопки отображаются
согласно правам пользователя. При выборе задачи из списка, откроется страница детальной информации.
В фильтрах по пользователю добавляется пункт *"Исполнитель"*.

На странице детальной информации отображается список зависимых задач, если они есть,
и история изменения задачи, а так же история изменений в родительской задаче, спринте и проекте.
Автор и исполнитель задачи могут добавить информацию в историю.

Задача имеющая зависимые задачи не может сама быть зависимой.

Планируемая дата вычисляется, как минимальная от планируемых дат выполнения проекта, спринта или задачи.

При редактировании задачи, проект выбирается из списка не закрытых проектов.
Спринт выбирается из списка не закрытых спринтов проекта.
Родительская задача выбирается из списка не закрытых задач спринта, если выбран спринт.
Или из списка задач проекта, если спринт не выбран. Список задач пересоздаётся при выборе проекта или спринта.

Исполнитель может изменить только дату закрытия задачи.

При использовании кнопки "Добавить" со страницы детальной информации, в создаваемой задаче автоматически
подставятся проект и спринт текущей задачи.

#### Поиск

При выборе пункта меню ***"Поиск"***, выводятся списки незавершенных проектов, спринтов и задач.
Кнопки отображаются согласно правам пользователя. Поиск производится не зависимо от регистра
в названиях проектов, спринтов и задач.

#### API

При выборе пункта меню ***"API"***, выводится вэб интерфейс фреймворка Django REST framework.
Работает простой фильтр по имени поля и точному совпадению значений. Например:  
`/api/tasks/?date_end=none&date_beg=2023-04-12`  
Можно только получать информацию. Создания и редактирования записей через API нет.

#### Авторизация

Если пользователь не авторизирован, то в правом верхнем углу отображается пункт меню *"Вход"*.
При его выборе, открывается страница авторизации. При успешной авторизации, пользователь перенаправляется
на главную страницу.

Если пользователь авторизирован, то в правом верхнем углу отображается имя пользователя и пункты меню
*"Сменить пользователя"* и *"Выход"*. При выборе пункта *"Сменить пользователя"*, открывается страница
авторизации. При выборе *"Выход"* пользователь переводится в статус не авторизованного. При успешной
авторизации или выходе, пользователь перенаправляется на главную страницу.

### Особенности

#### Настройки Базы данных:
В проекте реализовано подключение к локальной базе данных PosgreSQL

Настройки БД и сервера:

        "NAME": "task_db",
        "USER": "postgres",
        "PASSWORD": "pgadmin",
        "HOST": "127.0.0.1",
        "PORT": "5432",

Если у Вас сервер развернут с другими настройками, то Вам необходимо заменить отличающиеся параметры в строках 107-111
файла settings.py и провести миграцию. Для генерации данных в БД, можно воспользоваться функцией генерации данных (описание ниже)
Также, есть возможность использования SQLite и MySQL, но в крайних версиях проекта корректность их работы не проверялась.

#### Запуск проекта

Команда для запуска проекта:
`python manage.py runserver`

#### Тестирование

Команда для запуска тестов:  
`python manage.py test`
В тестировании имеется два блока.
В обоих блоках генерируются случайные данные, если база пустая

В первом блоке проверяется корректность записанной информации в базе.

Во втором блоке имитируется открытие страниц со списками проектов, спринтов и задач.
Проверяется наличие шаблона и корректность выбранных данных.

#### Генерация данных

Проект позволяет сгенерировать данные. Можно воспользоваться командой:  
`python manage.py shell -c="from app_task.services import gen_data; gen_data(cnt=25, close=75, clear=True, parent=True, clear_user=True)"`  
Запустится функция `gen_data` из модуля `app_task.services`.

Параметры по умолчанию, если они не указаны при отправке команды.
- `cnt=0` - Количество генерируемых проектов,
- `close=0` - Процент закрытия проектов и спринтов
- `clear=False` - Очищать базу перед генерацией
- `parent=False` - Создавать зависимые задачи
- `clear_user=False` - Удалить тестовых пользователей

Даты для данных выбираются из диапазона +\\- 3 месяца от текущей даты.
Шаблон начала имени тестового пользователя указан в настройках `MY_TEST_USER`. Если его нет, то - `test_user`.
Пароль - `MY_TEST_PASS` или, если нет, то - `password`. Шаги генерации данных:

1. Если есть очистка базы, то удаляются все проекты, все зависимые спринты и задачи, авторами которых
являются тестовые пользователи.
1. Если есть удаление тестовых пользователей, то удаляются пользователи совпадающие с шаблоном.
1. Если количество генерируемых проектов не равно нулю и не найдены тестовые пользователи, то генерируются трое тестовых
пользователей с данными авторизации:  
Логин - из настройки`<MY_TEST_USER><i (0-3)>`  
Пароль - из настройки `MY_TEST_PASS`
1. Создается указанное число проектов. Для проекта указывается случайные: автор, дата создания и планируемая дата закрытия.  
1. Создается удвоенное число спринтов. Для спринтов указывается случайные: автор, проект, дата создания и планируемая дата закрытия.  
1. Создается десятикратное число задач. Для задач указывается: случайные автор, исполнитель, проект, спринт, дата создания
и планируемая дата закрытия.
1. Если есть зависимые задачи, попытка в проекте создать их. Выбираются две случайные задачи проекта главная и зависимая.
1. Попытка закрыть указанное число спринтов. Выбираются случайные даты закрытия задач (не всех) и спринта.  
1. Попытка закрыть указанное число проектов. Выбирается случайные даты закрытия задач (не всех) и проекта.
