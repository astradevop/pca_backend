# Payment Collection App – Django + DRF Backend

A REST API backend for the Payment Collection App, built with **Django** and **Django REST Framework (DRF)**.

---

## Project Structure

```
pca_backend/
├── manage.py
├── requirements.txt
├── db.sqlite3              ← auto-generated after migrations
├── pca_backend/            ← Django settings & config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── customers/              ← Customers app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
└── payments/               ← Payments app
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── admin.py
```

---

## Setup & Run Locally

### 1. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a superuser (for admin panel)
```bash
python manage.py createsuperuser
```

### 5. Start the development server
```bash
python manage.py runserver
```

Server runs at: `http://127.0.0.1:8000`

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/customers/` | List all customers and their loan details |
| POST | `/api/payments/` | Submit a payment for a customer |
| GET | `/api/payments/<account_number>/` | Get payment history for an account |

---

### GET `/api/customers/`

Returns a list of all customers.

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "account_number": "ACC001",
    "issue_date": "2024-01-15",
    "interest_rate": "8.50",
    "tenure": 24,
    "emi_due": "5000.00"
  }
]
```

---

### POST `/api/payments/`

Submit an EMI payment.

**Request Body:**
```json
{
  "account_number": "ACC001",
  "payment_amount": 5000.00,
  "status": "completed"
}
```

**Response (201 Created):**
```json
{
  "message": "Payment recorded successfully.",
  "payment": {
    "id": 1,
    "account_number": "ACC001",
    "payment_date": "2026-03-07",
    "payment_amount": "5000.00",
    "status": "completed"
  }
}
```

**Error (400 – invalid account):**
```json
{
  "account_number": ["Customer with this account number does not exist."]
}
```

---

### GET `/api/payments/<account_number>/`

Retrieve payment history for a specific account.

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "account_number": "ACC001",
    "payment_date": "2026-03-07",
    "payment_amount": "5000.00",
    "status": "completed"
  }
]
```

**Response (404 – no history):**
```json
{
  "message": "No payment history found for account ACC999."
}
```

---

## Admin Panel

Visit `http://127.0.0.1:8000/admin/` to manage customers and payments via the Django admin interface.

---

## Database

- Default: **SQLite** (`db.sqlite3`) – zero config, great for development
- To switch to **PostgreSQL**, update `DATABASES` in `pca_backend/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Then install: `pip install psycopg2-binary`
