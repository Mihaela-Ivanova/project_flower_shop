# 🌸 FlowerShop 
Modern Django Web Application
FlowerShop is a modern, full‑featured Django web application designed as an online flower shop.
It provides a complete product catalog, categories, tags, product details, order creation, user accounts, reviews, REST API, admin management, and a clean, elegant UI.

# 🌐 Live Demo
🔗 flowershop-hsawd4anb2h0h5h7.spaincentral-01.azurewebsites.net

# ✨ Key Features
# 🏠 Public Section
- Home page with featured flowers
- Product catalog with search and filtering
- Product detail pages
- Contact form
- User registration & login
- Custom 404 & 500 error pages

# 🌸 Products (Flowers)
- Full CRUD (create, read, update, delete)
- Image upload
- Blooming season
- In‑stock indicator
- Category assignment
- Tags (Many‑to‑Many)
- Search functionality
- Clean Architecture: services + selectors

# 🏷 Categories & Tags
- Full CRUD for categories
- Full CRUD for tags
- Delete confirmation pages
- Slug support for tags
- Category listing page

# ⭐ Reviews
- Authenticated users can leave reviews
- Rating (1–5) + comment
- Reviews displayed on product detail page
- Admins can delete reviews

# 🛒 Orders
- Order creation from product detail page
- Customer name, email, phone, address, notes
- Quantity selection
- OrderItem model (supports multiple items per order)
- Email confirmation via Celery (async task)

# 👤 User Management
- User registration
- Login / logout
- Profile page
- Edit profile information
- Customers can:
- place orders
- write reviews
- update their profile

# 🔐 Permissions & Roles

The project uses Django Groups to define two roles:

Store Manager
- Add/edit/delete flowers
- Manage categories
- Manage tags
- View orders

Customer
- Place orders
- Write reviews
- Edit profile

Permissions enforced via:
- Django Groups
- Permissino Required Mixin
- Template‑level permission checks

# 🧱 Technologies Used

Backend
- Python 3.13
- Django 6.0.2
- Django ORM
- Django Templates
- Django Forms / ModelForms
- Django REST Framework
- Celery (asynchronous tasks)

Frontend
- HTML5
- CSS3
- Custom responsive layout

Database
- PostgreSQL (Render managed database)

Deployment
- Render Web Service
- Gunicorn
- Whitenoise
- Environment variables via .env

# 🌐 REST API (DRF)

GET /api/flowers/
Returns a list of flowers.

Query parameters:
- category
- tag
- season
- search

GET /api/flowers/<id>/
Returns details for a single flower.

# 🧪 Tests
The project includes automated tests covering:
- Models
- Forms
- Views
- API endpoints
- Template filters
- Permissions

# 📁 Project Structure

Project

<img width="677" height="612" alt="structure" src="https://github.com/user-attachments/assets/ef023278-40fd-45d1-8437-38b66f076a01" />


# ▶️ Running the Project (Local Development)

1. Clone the repository
    git clone <repo-url>
    cd Project

2. Create a virtual environment
    python -m venv .venv
    source .venv/bin/activate      # Linux/Mac
    .venv\Scripts\activate         # Windows

3. Install dependencies
    pip install -r requirements.txt
   
5. Apply migrations
   python manage.py migrate
   
7. Create a superuser
   python manage.py createsuperuser
   
9. Run the development server
   python manage.py runserver

# 🚀 Future Improvements

- Wishlist / Favorites
- Shopping cart
- Stripe payments
- Email verification
- Full REST API for orders
- Store Manager dashboard
- Product recommendations
