# 🌸 FlowerShop — Modern Django Web Application
FlowerShop is a modern Django web application designed as an online flower shop.
The project includes a product catalog, categories, product details, order creation, user accounts, and a clean, elegant interface.

# ✨ Key Features

🏠 Public Section
- Home page with featured products
- Product catalog
- Product details page
- Search and filtering
- Contact page
- User registration and login

🌸 Products (Flowers)
- List, detail, create, edit, delete
- Image upload
- Blooming season
- In stock indicator
- Category assignment
- Tags (Many-to-Many)
- Search functionality

🏷 Categories & Tags
- CRUD for categories
- CRUD for tags
- Category description
- Tag slugs
- Category delete confirmation form (read‑only

 👤 User Management
- User profile page
- Edit profile information
- Order history
- Create an order
- Add notes to an order
- Manage delivery address

🗂️ Administration
- Manage products
- Manage categories
- Manage orders
- Manage users
- Manage media files

⭐ Reviews
- Users can leave reviews for flowers
- Rating + comment
- Display reviews on product detail page
 
🧱 Technologies Used
- Python 3.13
- Django 6.0.2
- Django ORM
- Django Templates
- Django Forms / ModelForms


### Frontend
- HTML5
- CSS3
- Custom responsive layout

### Database
- PostgreSQL (Render managed database)

### Deployment
- Render Web Service
- Gunicorn
- Whitenoise
- Automatic staticfiles build
- Environment variables via `.env`


## 🔐 Permissions & Groups
Two user roles:
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
- PermissionRequiredMixin
- Template-level permission checks


🌐 REST API (DRF)
Endpoints:
GET /api/flowers/
Returns list of flowers.

Query parameters:
- category
- tag
- season
- search

GET /api/flowers/<id>/
Returns details for a single flower

## 🧪 Tests (optional)
15 tests covering:
- Models
- Forms
- Views
- API
- Template filter

# 📁 PROJECT STRUCTURE

<img src="images/project-structure.svg" width="400">

# ▶️ RUNNING THE PROJECT

<img src="images/running-the-project.svg" width="400">

# ❗ CUSTOM ERROR PAGES

<img src="images/custom-error-pages.svg" width="400">

# 👤 AUTHOR

<img src="images/author.svg" width="400">

## 🔐 Security

- SECRET_KEY stored in `.env`
- DEBUG=False in production
- Allowed Hosts configured
- CSRF protection enabled
- Password validators enabled
- PostgreSQL credentials stored as environment variables

## 🚀 Deployment (Render)

The project uses `render.yaml` for automated deployment:

- Automatic PostgreSQL database creation  
- Automatic environment variable binding  
- Build step with `collectstatic`  
- Gunicorn WSGI server  
- Whitenoise for static file serving  

## 📄 License
This project is created for educational purposes (SoftUni Django Exam).
