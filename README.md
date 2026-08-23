# Django Email Sender API

A simple reusable REST API for sending emails through Gmail SMTP. It is built with Django and Django REST Framework and can be integrated into other projects for verification emails, OTP messages, password resets, alerts, and notifications.

## Features

- Send plain-text emails using a REST API
- Validate recipient email addresses
- Gmail SMTP integration
- MySQL database configuration
- Environment-based credential management
- Django REST Framework browsable API
- Reusable across Django, Flask, FastAPI, Node.js, and other applications

## Technology Stack

- Python
- Django
- Django REST Framework
- MySQL
- Gmail SMTP
- python-dotenv

## API Endpoint

```http
POST /api/send-email/
```

Local URL:

```text
http://127.0.0.1:8000/api/send-email/
```

### Request Body

```json
{
  "subject": "Account verification",
  "message": "Your verification code is 483921.",
  "recipient": "recipient@example.com"
}
```

### Successful Response

Status: `200 OK`

```json
{
  "message": "Email sent successfully"
}
```

### Validation Error

Status: `400 Bad Request`

```json
{
  "recipient": [
    "Enter a valid email address."
  ]
}
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/DevanshSolanki19/django-email-sender-api.git
cd django-email-sender-api
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file:

```bash
cp .env.example .env
```

Add your configuration to `.env`:

```env
DJANGO_SECRET_KEY=your-django-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=3306

EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

Never commit the `.env` file.

### 5. Create the MySQL database

```sql
CREATE DATABASE restapi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 6. Apply migrations

```bash
python3 manage.py migrate
```

### 7. Start the server

```bash
python3 manage.py runserver
```

## Testing with cURL

```bash
curl -X POST http://127.0.0.1:8000/api/send-email/ \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Test email",
    "message": "Hello, this email was sent using the Django Email Sender API.",
    "recipient": "recipient@example.com"
  }'
```

## Using the API from Another Python Project

Install Requests:

```bash
python3 -m pip install requests
```

Example:

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/api/send-email/",
    json={
        "subject": "Account verification",
        "message": "Your verification code is 483921.",
        "recipient": "recipient@example.com",
    },
    timeout=10,
)

response.raise_for_status()
print(response.json())
```

## Security Notice

The current version does not include API authentication or rate limiting. Do not expose it publicly until authentication, permissions, and request throttling have been added.

## Future Improvements

- Token or API-key authentication
- HTML email templates
- OTP and verification-link templates
- Password-reset emails
- Asynchronous email delivery
- Rate limiting
- Email delivery logs
- Automated tests
- Docker support

## Author

[Devansh Solanki](https://github.com/DevanshSolanki19)
