# API Documentation

## 📝 Authentication APIs
| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/api/users/register/` | Register a new user |
| **POST** | `/api/users/login/` | Log in and receive an authentication token |
| **GET** | `/api/users/me/` | Retrieve authenticated user info |

### 🔒 Example Requests:

#### **Register a New User**
```bash
curl -X POST http://localhost:8001/api/users/register/ -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}'
```

#### **Log in and Get a Token**
```bash
curl -X POST http://localhost:8001/api/users/login/ -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}'
```

#### **Access Protected API with Token**
```bash
curl -H "Authorization: Bearer your-token-here" http://localhost:8001/api/users/me/
```

---

## ✅ Todo APIs (CRUD)

| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/api/todos/` | Create a new Todo |
| **GET** | `/api/todos/` | Get all Todos |
| **GET** | `/api/todos/{id}/` | Get a specific Todo |
| **PUT** | `/api/todos/{id}/` | Update a Todo (Partial Updates Allowed) |
| **DELETE** | `/api/todos/{id}/` | Delete a Todo |

### 📝 Example Requests:

#### **Create a New Todo**
```bash
curl -X POST http://localhost:8001/api/todos/ -H "Content-Type: application/json" -d '{
  "title": "Buy Eggs",
  "description": "Buy Eggs from market",
  "completed": false
}'
```

#### **Get All Todos**
```bash
curl -X GET http://localhost:8001/api/todos/ -H "accept: application/json"
```

#### **Update a Todo**
```bash
curl -X PUT http://localhost:8001/api/todos/1/ -H "Content-Type: application/json" -d '{
  "title": "Buy Milk",
  "completed": true
}'
```

#### **Delete a Todo**
```bash
curl -X DELETE http://localhost:8001/api/todos/1/
```

---

## 🌐 General APIs

### **Greet API**
| Method | Endpoint | Description |
|--------|----------|-------------|
| **GET** | `/api/greet/` | Simple API to check if the server is running |

#### 📝 Example Request:
```bash
curl -X GET http://localhost:8001/api/greet/
```

✅ **Expected Response:**
```json
{"message": "Hello, Django Ninja!"}
```

---

## 🎯 Task APIs (Background Tasks with Celery)

| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/api/tasks/process/` | Submit a task to Celery |
| **GET** | `/api/tasks/status/{task_id}/` | Get the status & result of a Celery task |

### 📝 Example Requests:

#### **Submit a Background Task**
```bash
curl -X POST http://localhost:8001/api/tasks/process/ -H "Content-Type: application/json" -d '{"data": "hello"}'
```
✅ Expected Response:
```json
{"task_id": "abc123"}
```

#### **Check Task Status**
```bash
curl -X GET http://localhost:8001/api/tasks/status/abc123/
```

✅ Possible Responses:

📌 **Task is still processing:**
```json
{
    "task_id": "abc123",
    "status": "PENDING",
    "result": null
}
```

📌 **Task has completed successfully:**
```json
{
    "task_id": "abc123",
    "status": "SUCCESS",
    "result": {"processed_data": "HELLO"}
}
```

For security details, check **[Authentication Guide](auth.md)**.
