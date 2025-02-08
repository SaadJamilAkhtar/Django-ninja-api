# Django Ninja API - Production Ready 🚀

This is a **fully functional Django Ninja API** built with:

✅ **Django Ninja** - High-performance API framework  
✅ **PostgreSQL** - Relational database  
✅ **Celery + Redis** - Background task processing  
✅ **JWT Authentication** - Secure user authentication  
✅ **Docker + Docker Compose** - Multi-container deployment  

---

## 📖 Documentation

This guide is split into multiple files:

📂 [Installation & Setup](docs/setup.md)  
📂 [API Documentation](docs/api.md)  
📂 [Authentication & Security](docs/auth.md)  
📂 [Background Tasks with Celery](docs/tasks.md)  
📂 [Todo CRUD API](docs/todo.md)

---

## 🚀 Quick Start  

### 1️⃣ Clone the Repository

### 2️⃣ Rename .env.sample to .env  
```bash
mv .env.sample .env
```

### 3️⃣ Build and Start the Docker Containers  
```bash
docker-compose up --build
```

### 4️⃣ Apply Migrations & Create Superuser  
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 5️⃣ Open API Docs in Browser  
[http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

---

## ⚙️ Project Structure  
```
📂 djangoNinja                 # Main Django project
📂 api                         # API app
📂 users                       # User authentication
📂 tasks                       # Celery background tasks
📂 todo                        # Todo CRUD API
📄 docker-compose.yml          # Multi-container setup
📄 Dockerfile                  # Application container
📄 .env.sample                 # Sample environment file
```

For more details, check out **[Installation & Setup](docs/setup.md)**.
