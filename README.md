# ImplementacionPylintBlack

## Project Overview

This project aims to implement a FastAPI-based backend with a Dockerized MySQL database and proper coding standards enforced using **Pylint** and **Black**. The application is structured to follow best programming practices and code quality standards, including the use of PEP8 conventions.

The project provides CRUD operations for three main entities: **Project**, **Employee**, and **Task**, and ensures that all APIs are protected using an API key.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Database Configuration](#database-configuration)
- [How to Run](#how-to-run)
- [Code Quality](#code-quality)
- [API Documentation](#api-documentation)

## Features

1. **Dockerized MySQL Database**:
   - A fully containerized MySQL database using Docker.
   - Configured with a `docker-compose.yml` to start the database and other services easily.
   
2. **Full CRUD API**:
   - CRUD operations for `Project`, `Employee`, and `Task` entities.
   
3. **API Key Authentication**:
   - All API routes are protected with an API key to ensure secure access.
   
4. **Pylint and Black**:
   - Code linting and formatting with Pylint and Black to maintain code quality.
   - Minimum Pylint score: 7 points or higher.

## Project Structure

```
├── FastAPI/                    # Backend folder
│   ├── app/                    # FastAPI app directory
│   ├── Dockerfile              # Dockerfile for FastAPI service
├── MySQL/                      # MySQL setup folder
│   ├── volumes/                # Volume to persist MySQL data
│   ├── Dockerfile              # Dockerfile for MySQL service
├── docker-compose.yml          # Docker Compose configuration
├── Makefile                    # Makefile for deploying services
├── .pylintrc                   # Pylint configuration
├── README.md                   # Project documentation (this file)
└── requirements.txt            # Python dependencies
```

## Dependencies

Key Python dependencies used in this project:

- **FastAPI** (0.112.1): Web framework to build APIs quickly.
- **SQLAlchemy** (2.0.35): ORM for handling database models and queries.
- **Pydantic** (2.8.2): Data validation and settings management.
- **Alembic** (1.13.2): Database migration tool.
- **Pylint** (3.2.7): Linter to enforce code quality.
- **Black** (24.8.0): Code formatter for PEP8 compliance.
- **Uvicorn** (0.30.6): ASGI server for FastAPI.
- **MySQL**: Database service running in a Docker container.

Other dependencies are listed in `requirements.txt` for your reference.

## Database Configuration

The project uses a MySQL database managed by Docker. The database schema includes three tables: **Project**, **Employee**, and **Task**.

- **Project**: id, name, description, start_date, end_date
- **Employee**: id, name, email, phone, position
- **Task**: id, project_id (FK), employee_id (FK), title, description, deadline, status

### Docker Compose

The following services are defined in `docker-compose.yml`:

```yaml
services:
  db:
    build:
      context: ./MySQL
      dockerfile: Dockerfile
    container_name: database
    restart: always
    ports:
      - 3307:3306
    volumes:
      - ./MySQL/volumes:/var/lib/mysql
    hostname: eam_database
    networks:
      - net_eam_database
    healthcheck:
      test: ["CMD", "mysql", "-u", "root", "-proot"]
      interval: 30s
      timeout: 10s
      retries: 5
  
  adminer:
    image: adminer
    container_name: adminer_eam
    restart: always
    ports:
      - 8080:8080
    networks:
      - net_eam_database

  fastapi:
    build:
      context: ./FastAPI
      dockerfile: Dockerfile
    container_name: backend
    restart: always
    ports:
      - "8000:80"
    depends_on:
      db:
        condition: service_healthy
    networks:
      - net_eam_database

networks:
  net_eam_database:
    driver: bridge
    name: net_eam_database
```

### Entity Relationships

- Each **Project** can have multiple **Tasks**.
- Each **Employee** can be assigned multiple **Tasks**.

## How to Run

### Using `make` (Linux only)

To deploy the project, simply run:

```bash
make deploy
```

This command will:
- Build and run the Docker services for the backend and the database.
- Use `docker-compose build` and `docker-compose up -d` commands.

> **Note:** `make` may only work on Linux or Unix-based systems. If you are using Windows, you can run the following commands manually:

```bash
docker-compose build
docker-compose up -d
```

### Accessing the Application

- FastAPI will be available at `http://localhost:8000`.
- Adminer (database management tool) will be available at `http://localhost:8080`.

## Code Quality

To ensure code quality and compliance with PEP8, the project uses:

- **Pylint**: For linting and enforcing code quality.
- **Black**: For automatic code formatting.

### Running Pylint

You can run Pylint with the following command:

```bash
pylint FastAPI/app
```

Make sure to maintain a score of 7 or higher, as it's a requirement for this project.

### Running Black

To format the code using Black, run:

```bash
black FastAPI/app
```

## API Documentation

FastAPI automatically generates interactive API documentation. Once the application is running, you can access the following:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

These interfaces allow you to explore the API and test the available endpoints.

## Conclusion

This project demonstrates how to build a scalable backend using **FastAPI**, manage a **MySQL** database with Docker, and enforce coding standards using **Pylint** and **Black**. The project structure and configurations follow best practices to ensure maintainability and security.

Feel free to explore the repository and make contributions!

---

Happy Coding! 🎉
```
