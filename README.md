# 🌸 FlowerShop — Modern Django Web Application  
FlowerShop is a modern Django web application designed as an online flower shop.  
The project includes a product catalog, categories, product details, order creation, user accounts, reviews, and a clean, elegant interface.

---

# ✨ Key Features

## 🏠 Public Section
- Home page with featured flowers  
- Product catalog with filtering and search  
- Product details page  
- Contact form  
- User registration & login  
- Custom 404 & 500 pages  

## 🌸 Products (Flowers)
- List, detail, create, edit, delete  
- Image upload  
- Blooming season  
- In‑stock indicator  
- Category assignment  
- Tags (Many‑to‑Many)  
- Search functionality  

## 🏷 Categories & Tags
- Full CRUD for categories  
- Full CRUD for tags  
- Category delete confirmation form (read‑only)  
- Tag slugs  

## 👤 User Management
- User registration & login  
- User profile page  
- Edit profile information  
- Order creation  
- Order notes  
- Delivery address  

## ⭐ Reviews
- Authenticated users can leave reviews  
- Rating + comment  
- Reviews displayed on product detail page  

## 🗂️ Administration
- Manage products  
- Manage categories  
- Manage tags  
- Manage orders  
- Manage users  
- Manage media files  

---

# 🧱 Technologies Used

### Backend
- Python 3.13  
- Django 6.0.2  
- Django ORM  
- Django Templates  
- Django Forms / ModelForms  
- Django REST Framework  
- Celery (async tasks)  

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
- Environment variables via `.env`  

---

# 🔐 Permissions & Groups

Two user roles:

### Store Manager
- Add/edit/delete flowers  
- Manage categories  
- Manage tags  
- View orders  

### Customer
- Place orders  
- Write reviews  
- Edit profile  

Permissions enforced via:
- Django Groups  
- PermissionRequiredMixin  
- Template-level permission checks  

---

# 🌐 REST API (DRF)

### GET `/api/flowers/`
Returns list of flowers.

Query parameters:
- `category`
- `tag`
- `season`
- `search`

### GET `/api/flowers/<id>/`
Returns details for a single flower.

---

# 🧪 Tests  

The project includes **15 automated tests** covering:

- Models  
- Forms  
- Views  
- API  
- Template filters  

---

# 📁 Project Structure

<img src="images/project-structure.svg" width="400">

---

# ▶️ Running the Project (Local Development)

<img src="images/running-the-project.svg" width="400">

### 1️⃣ Clone the repository
```bash
git clone <repo-url>
cd project_flower_shop

2️⃣ Create and activate virtual environmen
python -m venv .venv
.\.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure environment variables
Create a .env file in the project root
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_password

5️⃣ Apply migrations
python manage.py migrate

6️⃣ Create superuser
python manage.py createsuperuser

7️⃣ Start the development server
python manage.py runserver

8️⃣ Start Celery worker
celery -A Project worker -l info

🗄️ Database Diagram (ERD)
    <img src="images/erd.svg" width="500">

🧭 Navigation Map
![5.png](../5.png)

❗ Custom Error Pages
<img src="images/custom-error-pages.svg" width="400">

👤 Author
<img src="images/author.svg" width="400">

🔐 Security
• 	SECRET_KEY stored in 
• 	DEBUG=False in production
• 	Allowed Hosts configured
• 	CSRF protection enabled
• 	Password validators enabled
• 	PostgreSQL credentials stored as environment variables

🚀 Deployment (Render)
The project uses  for automated deployment:
• 	Automatic PostgreSQL database creation
• 	Automatic environment variable binding
• 	Build step with 
• 	Gunicorn WSGI server
• 	Whitenoise for static file serving


📄 License
This project is created for educational purposes (SoftUni Django Exam).
