# FastAPI Starter Template

FastAPI Starter Template is a solid, modular foundation for building modern, scalable web APIs with [FastAPI](https://fastapi.tiangolo.com/). This template includes a clean, decoupled architecture, ready for development and production deployment. It includes JWT authentication, environment variable configuration, CORS handling, integration with PostgreSQL, and Docker containers for easy orchestration and portability.

Ideal for those who want to start new projects without repeating configurations from scratch. Simply clone, configure, and start building.

## 🚀 Technologies

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)[![SQLModel](https://img.shields.io/badge/SQLModel-6DB33F?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://sqlmodel.tiangolo.com/)[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)[![Pydantic](https://img.shields.io/badge/Pydantic-FF4A00?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)[![CORS](https://img.shields.io/badge/CORS-333333?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/tutorial/cors/)[![PyJWT](https://img.shields.io/badge/PyJWT-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://pyjwt.readthedocs.io/en/stable/)[![Alembic](https://img.shields.io/badge/Alembic-4B8BBE?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://alembic.sqlalchemy.org/)


## 🗂️ Project Structure

```
fastapi-template/
├── alembic/                # Alembic configuration and migration scripts directory
│   ├── versions/           # Folder where generated migration files are stored
│   ├── env.py              # Alembic's main configuration script
│   └── script.py.mako      # Template used to generate new migration scripts
├── app/
│   ├── core/
│   │   ├── config.py       # Global settings
│   │   ├── database.py     # Database engine & session
│   │   ├── jwt.py          # JWT token creation & verification
│   │   └── security.py     # Password hashing utilities
│   ├── dependencies/
│   │   └── auth.py         # Auth-related dependencies (get_current_user)
│   ├── models/             # SQLModel ORM models
│   ├── routers/            # API route definitions
│   ├── schemas/            # Pydantic request/response schemas
│   ├── utils/              # Helper utilities
│   └── main.py             # Application entrypoint
├── docker/
│   ├── docker-compose.yml  # Development & testing orchestration
│   └── Dockerfile          # Production image definition
├── tests/                  # PyTest test cases
│   ├── integration/        # Integration tests (test API endpoints, DB, etc.)
│   └── unit/               # Unit tests (test individual functions/classes)
├── .env                    # Environment variables
├── .gitignore              # Git ignored files
├── alembic.ini             # Main Alembic configuration file
├── pytest.ini              # Global configuration for Pytest
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/JohannGaviria/fastapi-template.git
   cd fastapi-template
   ```

2. **Create a `.env` file**
   Copy the example or create your own:

   ```bash
   cp .env.example .env
   ```

   Fill in the required variables in `.env`.

### Local Environment

#### Prerequisites

* Python 3.8+
* PostgreSQL running and accessible
* Git installed
* (Optional) Poetry or pip

#### Steps


1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize and run Alembic migrations**

   If you make changes to your database models, you should create and apply migrations:

   ```bash
   # Create a new migration (autogenerate)
   alembic revision --autogenerate -m "your migration message"

   # Apply all pending migrations
   alembic upgrade head
   ```

3. **Run the application**

   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access the API**

   * Open your browser at `http://127.0.0.1:8000/docs` for interactive API docs (Swagger UI).
   * Open your browser at `http://127.0.0.1:8000/redoc` for alternative API documentation (ReDoc).

5. **Run tests**

   ```bash
   pytest
   ```

### Docker Environment

#### Prerequisites

* Docker & Docker Compose installed
* Git installed

#### Steps

1. **Start services with Docker Compose**

   ```bash
   docker compose --env-file .env -f docker/docker-compose.yml up --build
   ```

2. **Initialize and run Alembic migrations**

   You can run Alembic migrations inside the container after it is up.

   ```bash
   # Locally (requires dependencies installed)
   docker compose exec -it <app_service_name> alembic revision --autogenerate -m "your migration message"

   docker compose exec -it <app_service_name> alembic upgrade head
   ```

3. **Access the API**

   * Open your browser at `http://0.0.0.0:8000/docs` for interactive API docs (Swagger UI).
   * Open your browser at `http://0.0.0.0:8000/redoc` for alternative API documentation (ReDoc).

4. **Run tests**

   ```bash
   docker compose exec -it <app_service_name> pytest
   ```

## ✨ Features

* **RESTful endpoints** organized by routers
* **JWT authentication** with token generation & verification
* **SQLModel** models with automatic migrations support
* **CORS** middleware configured for development
* **Dockerized** setup: separate app & database services
* **PyTest** integration for unit & integration tests
* **Environment-based configuration** with Pydantic `BaseSettings`
* **Alembic migrations** for version-controlled database schema changes

## 🔧 Usage

* **Generate an access token (JWT)**
  Implement your login endpoint to call `create_access_token(data)` from `core/jwt.py`.

* **Protect routes**

   ```python
   from fastapi import Depends
   from app.dependencies.auth import get_current_user

   @app.get("/protected")
   def protected_route(current_user=Depends(get_current_user)):
      return {"message": "Hello, protected user!", "user": current_user}
   ```

## 🔒 Environment Variables

| Key                           | Description                                         |
|-------------------------------|-----------------------------------------------------|
| `SECRET_KEY`                  | Secret key for signing JWT tokens                   |
| `DB_USER`                     | Database username                                   |
| `DB_PASSWORD`                 | Database password                                   |
| `DB_HOST`                     | Database server host (e.g., `db` for Docker)        |
| `DB_PORT`                     | Database port (default: 5432)                       |
| `DB_NAME`                     | Database name                                       |
| `DATABASE_URL`                | Full database connection URL                        |
| `APP_NAME`                    | Application name                                    |
| `APP_SUMMARY`                 | Short summary of the application                    |
| `APP_DESCRIPTION`             | Detailed description of the application             |
| `APP_VERSION`                 | Application version                                 |
| `DEBUG`                       | Enable debug mode (`True` or `False`)               |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT access token expiration time in minutes         |
| `ALGORITHM`                   | JWT signing algorithm (e.g., HS256)                 |
| `CORS_ALLOW_ORIGINS`          | Allowed CORS origins (comma-separated)              |
| `CORS_ALLOW_CREDENTIALS`      | Allow CORS credentials (`True` or `False`)          |
| `CORS_ALLOW_METHODS`          | Allowed CORS methods (comma-separated)              |
| `CORS_ALLOW_HEADERS`          | Allowed CORS headers (comma-separated)              |

## 📄 License

This project is licensed under the [MIT License](LICENSE.txt). Feel free to use, modify, and distribute.

---

> Made with ❤️ by [JohanGaviria](https://github.com/JohannGaviria)
