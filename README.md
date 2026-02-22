🌸 FlowerShop — Modern Django Web Application
FlowerShop is a modern Django web application designed as an online flower shop.
The project includes a product catalog, categories, product details, order creation, user accounts, and a clean, elegant interface.

✨ Key Features
🏠 Public Section
- Home page with store presentation
- Product listing
- Product detail view
- Category browsing and filtering
- Contact page

👤 User Management
- User registration
- Login
- User profile
- Logout

🗂️ Administration
- Full CRUD for products
- Full CRUD for categories
- Media file management (images)

🧱 Technologies Used
- Python 3
- Django
- HTML5 / CSS3
- Bootstrap 5
- SQLite (default database)
- Django Templates
- Static & Media file handling


┌──────────────────────────────────────────────────────────────┐
│                       PROJECT STRUCTURE                       │
└──────────────────────────────────────────────────────────────┘

Project/
│  manage.py
│  README.md
│  requirements.txt
│
├── Project/                     # Django configuration
│     ├── settings.py
│     ├── urls.py
│     └── wsgi.py
│
├── products/                    # Products, categories, orders
│     ├── models.py
│     ├── views.py
│     └── urls.py
│
├── account/                     # Authentication, profiles
│     ├── views.py
│     └── urls.py
│
├── common/                      # Home, static pages
│     ├── views.py
│     └── urls.py
│
├── static/                      # CSS, JS, images
│     └── css/
│         └── style.css
│
├── media/                       # Uploaded images
│     └── flowers/
│
└── templates/                   # HTML templates
      ├── base.html
      ├── home.html
      ├── 404.html
      ├── 500.html
      ├── products/
      └── account/

┌──────────────────────────────────────────────────────────────┐
│                        RUNNING THE PROJECT                    │
└──────────────────────────────────────────────────────────────┘

1) Activate virtual environment
   -------------------------------------------------------------
   .venv\Scripts\activate
   -------------------------------------------------------------

2) Install dependencies
   -------------------------------------------------------------
   pip install -r requirements.txt
   -------------------------------------------------------------

3) Start development server
   -------------------------------------------------------------
   python manage.py runserver
   -------------------------------------------------------------

Application available at:
http://127.0.0.1:8000/

┌──────────────────────────────────────────────────────────────┐
│                        CUSTOM ERROR PAGES                     │
└──────────────────────────────────────────────────────────────┘

404 Not Found Page:
   templates/404.html
   handler404 = 'products.views.custom_404'

500 Internal Server Error Page:
   templates/500.html
   handler500 = 'products.views.custom_500'

Both pages:
   - Fully customized
   - Integrated into Django routing
   - Styled consistently with the project

┌──────────────────────────────────────────────────────────────┐
│                              AUTHOR                           │
└──────────────────────────────────────────────────────────────┘

Project developed by:
   Mihaela Ivanova

Focus areas:
   - Web Development
   - Django Applications
   - UI/UX Design
   - Clean and maintainable code

This project is built with precision, structure,
and attention to detail.

