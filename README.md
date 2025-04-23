# book_store_django
a book store e-commerce website using django 

# Bookstore Management System

## Overview
This is a **Bookstore Management System** built with **Django**. It allows users to view books, add them to a cart, and proceed with checkout. Admins can manage books, inventory, and view orders. This project includes features such as **user registration**, **login/logout**, **add/edit/delete books**, **cart management using sessions**, and more. The application is **Dockerized** for easy setup and deployment, and a **Jenkins pipeline** is provided for continuous integration and deployment.

## Features
- **User Authentication**: User registration, login, and logout functionality.
- **Admin Panel**: Custom admin panel for managing books, inventory, and orders.
- **Book Listing**: Users can browse and view a list of available books.
- **Book Details**: Users can view details of each book.
- **Cart Functionality**: Add/remove books to/from the cart, adjust quantities.
- **Responsive Design**: The UI is designed to work across devices.

## Tech Stack
- **Backend**: Django
- **Frontend**: HTML, CSS (Bootstrap)
- **Database**: PostgreSQL (configured in Docker)
- **Docker**: For containerization of the application and database
- **CI/CD**: Jenkins pipeline for build, test, and deployment
- **Version Control**: Git (GitHub repository)

## Setup Instructions

### Prerequisites
- **Docker**: Ensure Docker is installed on your machine. You can download it from [here](https://www.docker.com/get-started).
- **Jenkins** (Optional): If you wish to use Jenkins for the CI/CD pipeline, set up Jenkins and install necessary plugins like **Docker**.

### Steps to Run the Project Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/bookstore-project.git
    cd bookstore-project
    ```

2. **Build Docker images**:
    Make sure you have a valid `docker-compose.yml` and `Dockerfile` in your repository.
    ```bash
    docker-compose build
    ```

3. **Run the containers**:
    Start the application and the PostgreSQL database container.
    ```bash
    docker-compose up -d
    ```

4. **Apply database migrations**:
    Run the migrations to set up the database schema.
    ```bash
    docker-compose exec web python manage.py migrate
    ```

5. **Collect static files**:
    Collect static files for production.
    ```bash
    docker-compose exec web python manage.py collectstatic --noinput
    ```

6. **Access the application**:
    The app will be running on `http://localhost:8000` or the specified port.

### Running Tests
To run Django unit tests inside Docker, execute:
```bash
docker-compose exec web python manage.py test
```

### Admin Access
To access the Django admin panel:
1. Create a superuser by running the following command inside the container:
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```
2. Then visit the admin panel at `http://localhost:8000/admin/` and log in using your superuser credentials.

### Jenkins CI/CD Pipeline
- **Checkout Code**: Jenkins pulls code from GitHub automatically.
- **Build Docker Image**: Jenkins builds the Docker image for the app.
- **Run Tests**: Jenkins runs unit tests inside the Docker container.
- **Deploy**: Jenkins starts the Docker containers and applies migrations, collects static files, and deploys the app.

For more details, check the Jenkins configuration in the `Jenkinsfile`.

## Docker Configuration

### Dockerfile
The Dockerfile builds a Docker image for the Django project and sets up dependencies, environment variables, and web server configurations.

### docker-compose.yml
This file defines the services needed for the project, including:
- **web**: The Django app container.
- **db**: PostgreSQL database container.
- Ports are mapped to your local machine to access the app and database.

## Troubleshooting
- If you face issues with Docker containers, make sure your Docker Desktop is running and configured to use Linux containers.
- If you face connection issues with the database, ensure the container names in `docker-compose.yml` are correctly linked.

## License
This project is open-source and available under the MIT License.
