# PCA Backend - Django REST Framework

The robust API engine for the Payment Collection App (PCA). Built to handle loan management, customer data, and secure payment processing.

---

## 🚀 API Features

- **JWT Auth**: Uses `djangorestframework-simplejwt` for secure, stateless authentication.
- **RESTful Endpoints**: Clean API structure for Customers and Payments.
- **MySQL Integration**: Persistent storage for loan and payment records.
- **Automated Deployment**: CI/CD ready via GitHub Actions and Gunicorn.

---

## 🚪 API Endpoints

### Authentication
- `POST /api/token/`: Obtain JWT Access & Refresh tokens.
- `POST /api/token/refresh/`: Refresh an expired access token.

### Customers
- `GET /api/customers/`: List all customers (Auth required).
- `POST /api/customers/`: Create a new customer record.

### Payments
- `POST /api/payments/`: Record a new EMI payment.
- `GET /api/payments/<account_number>/`: Retrieve payment history for an account.

---

## 🔑 Admin Setup

To log in to the system, you must have a superuser account. Create one via the EC2 terminal:

```bash
python manage.py createsuperuser
```

**Default Evaluation Credentials:**
- **Username**: `admin`
- **Password**: `admin123`

---

## 🛠️ Installation & Deployment

### 1. Local Setup
```bash
# Clone
git clone https://github.com/astradevop/pca_backend.git
cd PCA_BACKEND

# Environment
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate on Windows
pip install -r requirements.txt

# Database
python manage.py makemigrations
python manage.py migrate

# Server
python manage.py runserver
```

### 2. Live Server Architecture
- **Web Server**: Nginx (Reverse Proxy)
- **WSGI**: Gunicorn (Unix Socket)
- **Database**: MySQL Server
- **OS**: Ubuntu 22.04 LTS (AWS EC2)

---

## ⚙️ CI/CD (GitHub Actions)
The backend is automatically deployed to AWS on every push to the `main` branch. The workflow:
1. SSH into EC2.
2. Pull latest code.
3. Install dependencies.
4. Apply migrations.
5. Restart the Gunicorn service.

---

## 📄 License
MIT License.
