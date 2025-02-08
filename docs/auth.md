# Authentication & Security Guide

This project implements **token-based authentication** without relying on Django REST Framework (DRF).  
Users can register, log in, and access protected resources using **a custom token-based authentication system**.

---

## 🔐 User Authentication API

| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/api/users/register/` | Register a new user |
| **POST** | `/api/users/login/` | Log in and receive an authentication token |
| **GET** | `/api/users/me/` | Retrieve authenticated user info |

### 📝 Example Requests:

#### **1️⃣ Register a New User**
```bash
curl -X POST http://localhost:8001/api/users/register/ -H "Content-Type: application/json" -d '{
  "username": "admin",
  "password": "admin"
}'
```

✅ **Expected Response:**
```json
{
    "token": "your-secure-token-here"
}
```

---

#### **2️⃣ Log in to Get a Token**
```bash
curl -X POST http://localhost:8001/api/users/login/ -H "Content-Type: application/json" -d '{
  "username": "admin",
  "password": "admin"
}'
```

✅ **Expected Response:**
```json
{
    "token": "your-secure-token-here"
}
```

---

#### **3️⃣ Use the Token for API Requests**
Once you have the token, include it in the `Authorization` header for **protected API requests**.

```bash
curl -H "Authorization: Bearer your-secure-token-here" http://localhost:8001/api/users/me/
```

✅ **Expected Response:**
```json
{
    "username": "admin"
}
```

---

## ⚡ How Token Authentication Works

1️⃣ **User registers or logs in** → The API **generates a secure token**.  
2️⃣ The token is **stored in the database and associated with the user**.  
3️⃣ The client **includes the token in API requests** (`Authorization: Bearer <token>`).  
4️⃣ The API **validates the token and authenticates the user** before granting access.  

---

## 🔒 Security Best Practices

🔹 **Never store tokens in frontend code** (use secure storage like HTTP-only cookies).  
🔹 **Rotate tokens periodically** to reduce security risks.  
🔹 **Use HTTPS** to encrypt API traffic.  
🔹 **Limit token lifetime** (optional, can be implemented with expiry mechanisms).  

For API usage details, check **[API Documentation](api.md)**.
