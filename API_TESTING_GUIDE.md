# Postman API Testing Guide

You can test the APIs in Postman using the imported collection or manually configuring the requests as shown below.

## Option 1: One-Click Import (Recommended)

I've generated a Postman Collection file for you: `PCA_Postman_Collection.json` (located in your backend folder).

1. Open Postman.
2. Click **Import** (top left).
3. Drag and drop the `PCA_Postman_Collection.json` file.
4. An imported folder named **"Payment Collection App (PCA)"** will appear containing all the APIs ready to use!

---

## Option 2: Manual Setup in Postman

If you prefer to create the requests manually, follow these steps. Make sure your local server is running by executing:
`python manage.py runserver 8000`

### 1. Get All Customers
- **Method:** `GET`
- **URL:** `http://127.0.0.1:8000/api/customers/`
- **Steps:** Just click "Send". 
- **Expected Return:** A list `[]` of all customers setup in the database so far.

*(Note: To actually see data here, you can add generic customers quickly via the Django Admin panel at `http://127.0.0.1:8000/admin/`, or via the python shell `python manage.py shell`.)*

---

### 2. Make a Payment
- **Method:** `POST`
- **URL:** `http://127.0.0.1:8000/api/payments/`
- **Headers:** `Content-Type: application/json` is automatically handled if you select "raw" -> "JSON" in the body.
- **Body:** Under the **Body** tab, choose **raw** and set the dropdown to **JSON**. Paste the exact JSON below:
    ```json
    {
        "account_number": "ACC123",
        "payment_amount": 1000.50,
        "status": "completed"
    }
    ```
- **Prerequisite:** Make sure the `account_number` you pass actually exists in the Customer database (e.g. `ACC123` via Admin Panel), otherwise you will get a 400 Validation Error.
- **Expected Return:** 
    ```json
    {
        "message": "Payment recorded successfully.",
        "payment": {
            "id": 1,
            "account_number": "ACC123",
            "payment_date": "2026-03-07",
            "payment_amount": "1000.50",
            "status": "completed"
        }
    }
    ```

---

### 3. Get Payment History
- **Method:** `GET`
- **URL:** `http://127.0.0.1:8000/api/payments/ACC123/`
- **Steps:** Replace `ACC123` in the URL with the actual account number you want to track history for.
- **Expected Return:** Returns a JSON list of all payments successfully recorded for that particular account number.
