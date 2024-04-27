# Django_CRM_Financial_statements

<p>
Приложение разработано для удобной загрузки отчетов в бизнес-консалтинговую 
платформу "Фин-табло". Теперь можно быстро загружать отчеты и 
автоматически отправлять их в раздел операций ДДС.
</p>
<hr>
<h3 align="center" style="color: darkcyan;">The stack used:</h3>

<div align="center" style="background-color: white; padding: 20px; border-radius: 5px;">
   <b><p style="color: black;">Python 3.10;</p></b>
   <b><p style="color: black;">Django 5.0.2;</p></b>
   <b><p style="color: black;">JavaScript;</p></b>
   <b><p style="color: black;">Html;</p></b>
   <b><p style="color: black;">Css;</p>
   <b><p style="color: black;">Pillow;</p></b>
   <b><p style="color: black;">Requests</p></b>
   <b><p style="color: black;">Python-dotenv</p></b>
   <b><p style="color: black;">REST API</p></b>
</div>
<hr>

## Functionality
   <h4>Done:</h4>
   :white_check_mark: Регистрация <br>
   :white_check_mark: Авторизация <br>
   :white_check_mark: Разлогинивание (<b>Необходимо войти</b>)<br>
   :white_check_mark: Загрузка отчёта в Базу Данных (<b>Необходимо войти</b>)<br>
   :white_check_mark: Раздел пользователя<br>
   :white_check_mark: Раздел администратора<br>
   :white_check_mark: Поисковая строка<br>
   :white_check_mark: Фильтрация<br>
   :white_check_mark: Изменение статуса отчёта<br>
   :white_check_mark: Оправка данных отчёта по API в ФинТабло<br>
   :white_check_mark: Оправка изображения по API на Я-Диск 
   (название картинки будет зависеть, от того что пользователь ввёл в форму)<br>
<hr>   

   <h4>Works:</h4>
   :black_square_button: Адаптация сайта под мобильные устройства<br>
<hr>

   <h4>Not ready:</h4>
   :negative_squared_cross_mark: Редактирования отчётов<br>
<hr>

<h3>Описание</h3>
<p>
На главной странице предоставлен удобный поиск с выпадающем списком, 
в котором содержатся данные из "Финтабло". Четыре последних поля 
обязательны для заполнения. Достаточно выбрать необходимые данные, 
прикрепить изображения и отправить форму.
</p>
<img src="./readme_media/1.png">
<img src="./readme_media/2.png">
<img src="./readme_media/3.png">
<img src="./readme_media/4.png">
<hr>
<p>Далее на портале "Финтабло" можно просмотреть загруженный отчёт о списание средствах
и ссылку на изображения в базе данных. 
</p>
<img src="./readme_media/5.png">
<p>Также изображение чека дублируется на Яндекс.Диск. В названии содержится дата, 
инициалы, а также информация о цели составления отчёта.</p>
<img src="./readme_media/6.png">
<hr>

<p>
Когда мы входим как обычные пользователи, у нас есть возможность 
перейти на страницу "Мои отчёты". На этой странице мы можем 
отследить все операции и выполнить поиск в пределах своего пользователя.
</p>
<img src="./readme_media/15.png">
<hr>

<p>
Когда мы входим как администратор, у нас есть возможность отслеживать 
все операции различных пользователей. Доступны удобные фильтры по 
категориям: "Все", "Новые" и "Проверено", а также поисковая строка 
для удобства навигации.
</p>
<img src="./readme_media/16.png">
<img src="./readme_media/17.png">
<img src="./readme_media/18.png">
<hr>

<p>
При нажатии на изображение, открывается модальное окно с изображением чека операции.
</p>
<img src="./readme_media/19.png">
<hr>

<p>
Также доступна мобильная версия приложения.
</p>
<img src="./readme_media/20.png">
<img src="./readme_media/21.png">
<hr>

<h3>Для разработки</h3>

#### Важно ! добавить файл .env с секретными ключами и токенами

#### Установить виртуальное окружения:
for Linux/Mac:

    python3 -m venv venv

for Windows

    venv\Scripts\activate

#### Активировать:
for Linux/Mac:

    source venv/bin/activate

for Windows:

    venv\Scripts\activate

#### Установить зависимости:
      pip3 install -r requirements.in

#### Локальный запуск
      python3 manage.py runserver
<hr>
<h3>Немного простых и важных правил по написанию кода для проекта</h3> 

### Html
<p>
Название классов должно построено следующим образом: <br>
Родительский контейнер class=wrapper--name;<br>
Дочерний контейнер class=ul--li-list_name;<br>
Собержимое называть понятным именем name_image, name_title и.т.д;<br>
Для JavaScript обращение желательно по id;<br>
При возможности называть классы одинаково в разных блоках, чтобы избежать написания лишней разметки и стилей;<br>

<img src="./readme_media/7.png">
</p>
<hr>

### Css
<p>
Параметры как цвета и шрифты выносить в переменные<br>
<img src="./readme_media/8.png">
Выносить повторяющиеся параметры стилей в группу<br>
<img src="./readme_media/9.png">
Строго обозначить в комментариях откуда начинаются параметры для блоков html<br>
<img src="./readme_media/10.png">
</p>
<hr>

### Python
<p>
Весь функционал должен храниться в файле utils.py, в views.py только
обращения в БД согласно документации фреймворка Django.<br>
utils.py
<img src="./readme_media/11.png">
views.py
<img src="./readme_media/12.png">
Структура страниц html и статических файлов и папок, должна быть построена строго согласно документации фреймворка Django<br>
mainapp/templates/mainapp/index.html<br>
<img src="./readme_media/13.png"><br>
Секретные ключи, пароли и токены хранить в файле .env, подключение осуществляется через 
константы и библиотеку python-dotenv<br><br>
Строго избегать дублирующийся код<br>
<img src="./readme_media/14.png"><br><br>
При выполнение задачи обязательно создать новую ветку на GitHub/GitLab !
</p>