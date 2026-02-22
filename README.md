# 🌸 FlowerShop — Modern Django Web Application

FlowerShop е модерно Django уеб приложение за онлайн магазин за цветя.  
Проектът включва каталог с продукти, категории, детайли за цветя, поръчки, потребителски профили и красив, изчистен дизайн.

---

## ✨ Основни функционалности

### 🏠 Публична част
- Начална страница с представяне на магазина  
- Списък с продукти  
- Детайли за продукт  
- Категории и филтриране  
- Контактна страница  

### 👤 Потребители
- Регистрация  
- Вход  
- Потребителски профил  
- Изход  

### 🛒 Поръчки
- Създаване на поръчка  
- Валидиране на данни  
- Запис в базата  

### 🗂️ Администрация
- CRUD за продукти  
- CRUD за категории  
- Управление на снимки (media)  

---

## 🧱 Използвани технологии

- **Python 3**
- **Django**
- **HTML5 / CSS3**
- **Bootstrap 5**
- **SQLite** (по подразбиране)
- **Django Templates**
- **Static & Media файлове**

---

📁 Project Structure

Project/
│  manage.py
│  README.md
│  requirements.txt
│
├── Project/               ← Django настройки
│     ├── settings.py
│     ├── urls.py
│     └── wsgi.py
│
├── products/              ← Продукти, категории, поръчки
│     ├── models.py
│     ├── views.py
│     └── urls.py
│
├── account/               ← Регистрация, логин, профил
│     ├── views.py
│     └── urls.py
│
├── common/                ← Начална страница, статични страници
│     ├── views.py
│     └── urls.py
│
├── static/                ← CSS, изображения, JS
│     └── css/
│         └── style.css
│
├── media/                 ← Качени снимки
│     └── flowers/
│
└── templates/             ← HTML шаблони
      ├── base.html
      ├── home.html
      ├── products/
      └── account/

▶️ How to Run the Project

┌───────────────────────────────────────────────┐
│ 1) Activate virtual environment               │
│                                               │
│   .venv\Scripts\activate                      │
└───────────────────────────────────────────────┘

┌───────────────────────────────────────────────┐
│ 2) Install dependencies                       │
│                                               │
│   pip install -r requirements.txt             │
└───────────────────────────────────────────────┘

┌───────────────────────────────────────────────┐
│ 3) Run the development server                 │
│                                               │
│   python manage.py runserver                  │
└───────────────────────────────────────────────┘

📌 The project will be available at:
http://127.0.0.1:8000/