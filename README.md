# JWT Authentication with FastAPI <br>
This project demonstrates how to implement JWT (JSON Web Token)-based authentication using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python. Authentication is the process of verifying users before granting them access to secured resources. Upon successful authentication, users are issued a JWT, which they can use to access protected endpoints.

## Features <br>
User Registration: Users can register with a username and password.

User Login: Users can log in to receive a JWT.

Protected Routes: Access to certain endpoints is restricted to authenticated users only.

Token Expiry: JWTs have an expiration time for enhanced security.

Password Hashing: User passwords are securely hashed using bcrypt.

## Installation <br>
Follow these steps to set up the project on your local machine.

Prerequisites
Python 3.7 or higher

pip (Python package installer)

Steps
* Install pipenv <br>
pipenv is a tool for managing Python virtual environments and dependencies. Install it globally using:

* pip install pipenv <br>
Create and Activate Virtual Environment
Navigate to the project directory and run:

* pipenv shell <br>
This creates and activates a virtual environment for the project.

## Install Dependencies <br>
Install all required dependencies listed in requirements.txt:
* pip install -r requirements.txt


## Run the Application <br>
Start the FastAPI application using uvicorn:
* uvicorn main:app --reload
The --reload flag enables auto-reloading during development.
## Technologies Used <br>
FastAPI: A modern, fast web framework for building APIs.

JWT (JSON Web Tokens): A compact, URL-safe means of representing claims to be transferred between two parties.

Bcrypt: A library for hashing passwords.

Uvicorn: A lightning-fast ASGI server for serving FastAPI applications.
