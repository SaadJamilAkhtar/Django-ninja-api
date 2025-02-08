# Background Tasks with Celery

This project uses **Celery** with **Redis** as a message broker to run background tasks.  
Celery allows long-running or asynchronous operations to be processed **without blocking API requests**.

---

## 🎯 Task API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/api/tasks/process/` | Submit a task to Celery |
| **GET** | `/api/tasks/status/{task_id}/` | Get the status & result of a Celery task |

### 📝 Example Requests:

#### **1️⃣ Submit a Background Task**
```bash
curl -X POST http://localhost:8001/api/tasks/process/ -H "Content-Type: application/json" -d '{
  "data": "hello"
}'
```

✅ **Expected Response:**
```json
{
    "task_id": "abc123"
}
```

---

#### **2️⃣ Check Task Status**
```bash
curl -X GET http://localhost:8001/api/tasks/status/abc123/
```

✅ **Possible Responses:**

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

---

## ⚙️ How Celery Works

1️⃣ A **task is sent to the Celery worker** via the API.  
2️⃣ The **worker picks up the task from Redis** and starts processing it.  
3️⃣ The client can **retrieve the task status** anytime using the task ID.  
4️⃣ Once completed, **the task result is stored in Redis** and available via API.

---

## 🔧 Configuring Celery in `settings.py`

Celery is **already pre-configured** inside `project/settings.py`:

```python
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
```

---

## 🚀 Running Celery with Docker

Celery is automatically started inside a **separate container** when using `docker-compose up`.

To **restart Celery manually**, run:
```bash
docker-compose restart celery
```

To **view Celery logs**, use:
```bash
docker-compose logs celery
```

---

## 🔒 Best Practices for Background Tasks

✔ **Use Celery for long-running tasks** (e.g., sending emails, processing files).  
✔ **Avoid returning large task results** in the response—store them in the database instead.  
✔ **Scale Celery workers** by running multiple instances (`celery -A djangoNinja worker --loglevel=info -c 4`).  

For API usage details, check **[API Documentation](api.md)**.
