# Secure RESTful API Service (Flask)

A production-style **secure RESTful API** built using **Python Flask**, demonstrating authentication, authorization, validation, logging, error handling, automated testing, and API documentation.  
This project is designed to showcase **security-first backend development** and **real-world testing practices**.

---

## Project Overview

This project implements a secure REST API that allows users to:

- Register and authenticate using **JWT-based authentication**
- Access protected resources
- Validate inputs and handle errors gracefully
- Log security-relevant events
- Test all critical flows using **Pytest**
- Generate automated **test and coverage reports**

The API follows **REST principles**, uses **SQLite** for persistence, and includes **Swagger (OpenAPI)** documentation.

---

##  Use Case

This project demonstrates:

- Backend development competence
- Secure authentication & authorization design
- Test-driven and coverage-driven development
- Industry-standard project structuring
- Readiness for real-world backend roles

Ideal for:
- Developer portfolios
- Academic submission
- Backend / Full-stack interview demonstration

---

##  Tech Stack

| Category | Technology |
|--------|-----------|
| Language | Python 3.10 |
| Framework | Flask |
| Authentication | JWT (Flask-JWT-Extended) |
| Database | SQLite |
| ORM | SQLAlchemy |
| API Docs | Swagger (Flasgger) |
| Testing | Pytest |
| Coverage | pytest-cov |
| Reporting | pytest-html |
| Logging | Python logging |

---

##  Features

- JWT-based authentication
- Password hashing
- Input validation
- Centralized error handling
- Secure protected endpoints
- Swagger API documentation
- Isolated in-memory database testing
- Automated test & coverage reports
- SQLAlchemy 2.0 compatible

---

## Setup & Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/secure-rest-api.git
cd secure-rest-api
```
### Create Virtual Environment
``` cmd
python-m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### Install Dependencies
```pip install -r requirements.txt```

### Database Setup
flask db init
flask db migrate
flask db upgrade

SQLite database will be created automatically.

---

### Running the Application
```python run.py```

#### Server runs at:
```http://127.0.0.1:5000```

---
## API Documentation (Swagger)

### Swagger UI is available at:
```http://127.0.0.1:5000/apidocs/```

#### This provides:

Endpoint documentation

Request/response schemas

Live API testing interface

### API Endpoints
Authentication
Method	Endpoint	Description
POST	/api/auth/register	Register a new user
POST	/api/auth/login	Login & receive JWT
Protected Routes
Method	Endpoint	Description
GET	/api/users/me	Get authenticated user profile

### Testing Strategy

Testing is implemented using Pytest with:

In-memory SQLite database

Isolated test environment per test

Authentication and authorization coverage

Deterministic, repeatable tests

#### Run Tests
```pytest```

---

## Test Coverage

### Generate coverage report:

```pytest --cov=app --cov-report=term-missing```

Current Coverage

Total Coverage: 93%

Core business logic: 100%

Error paths excluded (non-critical)

### Generate HTML Test Report (Final Output)
```pytest \
--cov=app \
--cov-report=term-missing \
--cov-report=html \
--html=Test_Report.html \
--self-contained-html
```
---
### Output Files

```
Test_Report.html → Detailed test execution report

htmlcov/index.html → Line-by-line coverage report
```

These files serve as final submission artifacts.

---
### Security Considerations

Passwords are securely hashed

JWT tokens are signed and validated

Protected routes enforce authentication

Input validation prevents malformed data

Centralized error handling avoids data leakage

---
### Key Learnings

JWT identity serialization handling

Proper HTTP status code usage

Test isolation using Pytest fixtures

SQLAlchemy 2.0 compatibility

Coverage-driven backend development

---

### Future Enhancements

Role-Based Access Control (RBAC)

Rate limiting (Flask-Limiter)

Refresh tokens

Dockerization

CI/CD integration

Migration to PostgreSQL

---

### Final Outcome

Secure RESTful API built using Flask

JWT authentication implemented correctly

Automated testing with Pytest

93% code coverage achieved

HTML test & coverage reports generated

Production-style backend architecture

---

### Author
Davis Niranjan

---
###License
This project is licensed for educational use.

