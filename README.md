# FastAPI Backend – Posts, Authentication & Voting API

A production-style backend API built using FastAPI, PostgreSQL, and SQLAlchemy.
This project implements JWT-based authentication, user authorization, CRUD
operations on posts, and a voting system, following real-world backend best
practices.

This repository is suitable for learning, backend internships, and entry-level
backend engineering roles.

---

## Features

- JWT authentication using OAuth2 Password Bearer flow
- User registration and login
- Secure password hashing using bcrypt
- CRUD operations on posts
- Authorization (users can modify only their own posts)
- Voting system with duplicate-vote prevention
- PostgreSQL database with SQLAlchemy ORM
- Alembic database migrations
- Environment-based configuration using Pydantic
- Automatic API documentation via Swagger and ReDoc
- CORS enabled for frontend integration

---

## Tech Stack

Backend Framework: FastAPI  
Language: Python  
Database: PostgreSQL  
ORM: SQLAlchemy  
Migrations: Alembic  
Authentication: JWT (OAuth2 Password Flow)  
Password Hashing: Passlib (bcrypt)  
Validation: Pydantic  
ASGI Server: Uvicorn  

---

## Project Structure

fastapi/
├── app/
│ ├── main.py # Application entry point
│ ├── database.py # Database connection & session handling
│ ├── models.py # SQLAlchemy ORM models
│ ├── schemas.py # Pydantic schemas
│ ├── config.py # Environment-based configuration
│ ├── oauth2.py # JWT token creation & verification
│ ├── utils.py # Password hashing utilities
│ └── routers/
│ ├── post.py # Post CRUD routes
│ ├── user.py # User routes
│ ├── auth.py # Authentication routes
│ └── vote.py # Voting routes
│
├── alembic/ # Database migration scripts
├── alembic.ini
├── requirements.txt
└── README.md

---

## Authentication Flow

1. User logs in using email and password
2. Server returns a JWT access token
3. Token is sent in the request header as:

Authorization: Bearer <access_token>

4. Protected routes verify the token and fetch the current user

---

## Database Models

User
- id
- email
- password
- created_at

Post
- id
- title
- content
- published
- owner_id (foreign key to users)

Vote
- user_id (foreign key)
- post_id (foreign key)
- composite primary key prevents duplicate voting

---

## Environment Variables

Create a `.env` file in the project root:

DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=yourpassword
DATABASE_NAME=fastapi

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

---

## Setup and Run Locally

Clone the repository:

git clone https://github.com/Adii22-22/FASTAPI-POSTS-API.git

cd FASTAPI-POSTS-API

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # Linux / macOS
venv\Scripts\activate # Windows


Install dependencies:

pip install -r requirements.txt

Run database migrations:

alembic upgrade head
Start the development server:
uvicorn app.main:app --reload


The server will run at:
http://127.0.0.1:8000

---

## API Documentation

Swagger UI:
http://127.0.0.1:8000/docs


ReDoc:
http://127.0.0.1:8000/redoc

---

## Example Endpoints

POST /users -> Create user
POST /login -> Authenticate user
GET /posts -> Fetch all posts
POST /posts -> Create a post (authentication required)
POST /vote -> Vote on a post


---

## Future Improvements

- Refresh tokens
- Dockerization
- Unit and integration testing
- Role-based access control
- Pagination and filtering
- CI/CD pipeline using GitHub Actions

---

## License

This project is licensed under the MIT License.

