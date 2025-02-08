# Todo API - Full CRUD with Meta & Config in Django Ninja

This project includes a **fully functional Todo API** to demonstrate the power of Django Ninja’s **Model Schemas** using both **Meta** and **Config** classes.

---

## ✅ Todo API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/api/todos/` | Create a new Todo |
| **GET** | `/api/todos/` | Get all Todos |
| **GET** | `/api/todos/{id}/` | Get a specific Todo |
| **PUT** | `/api/todos/{id}/` | Update a Todo (Partial Updates Allowed) |
| **DELETE** | `/api/todos/{id}/` | Delete a Todo |

### 📝 Example Requests:

#### **1️⃣ Create a New Todo**
```bash
curl -X POST http://localhost:8001/api/todos/ -H "Content-Type: application/json" -d '{
  "title": "Buy Eggs",
  "description": "Buy Eggs from market",
  "completed": false
}'
```

✅ **Expected Response:**
```json
{
    "id": 1,
    "title": "Buy Eggs",
    "description": "Buy Eggs from market",
    "completed": false,
    "created_at": "2025-02-08T12:00:00Z",
    "updated_at": "2025-02-08T12:00:00Z"
}
```

---

## ⚡ Using `Meta` vs `Config` for Schema Generation

Django Ninja provides two ways to **convert Django ORM models into API Schemas**:

### ** Using `Meta` (Auto Schema Generation)**
```python
class TodoSchemaMeta(ModelSchema):
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "completed"]
```

**Why Use `Meta`?**  
- Automatically generates schema from **Django models**.  
- Saves time **without needing to define fields manually**.  

---

### ** Using `Config` (More Control Over Schema)**
```python
class TodoSchemaConfig(Schema):
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: datetime  # Convert datetime to string
    updated_at: datetime

    class Config:
        from_attributes = True  # Ensures ORM objects are serialized correctly
        json_encoders = {
            datetime: lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S")
        }
```

**Why Use `Config`?**  
- Allows **custom serialization** (e.g., formatting `datetime` fields).  
- Offers **more control over API responses**.  
- Works **best for APIs needing customization**.  

---

## 🚀 Testing the API

### **2️⃣ Get All Todos**
```bash
curl -X GET http://localhost:8001/api/todos/ -H "accept: application/json"
```

### **3️⃣ Update a Todo (Partial Updates Allowed)**
```bash
curl -X PUT http://localhost:8001/api/todos/1/ -H "Content-Type: application/json" -d '{
  "title": "Buy Milk",
  "completed": true
}'
```

### **4️⃣ Delete a Todo**
```bash
curl -X DELETE http://localhost:8001/api/todos/1/
```

---

## 🔥 When to Use `Meta` vs `Config`?

| Feature | Meta | Config |
|---------|------|--------|
| **Auto Schema Generation** | ✅ Yes | ❌ No |
| **Custom Field Formatting** | ❌ No | ✅ Yes |
| **Best for Simple Models** | ✅ Yes | ❌ No |
| **Best for Advanced APIs** | ❌ No | ✅ Yes |

**✅ Use `Meta` when you need quick, simple APIs with minimal customization.**  
**✅ Use `Config` when you need more control over how data is formatted and returned.**  

For API usage details, check **[API Documentation](api.md)**.
