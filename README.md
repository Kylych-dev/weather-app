# API Documentation

This document provides an overview of the API endpoints available in this project.

I didn't have time to do a lot of things, sorry

brief summary of the tools and platforms i used:

    Development Frameworks: Django
    API Documentation: Swagger, Redoc
    Version Control: Git
    Containerization: Docker
    Testing: Pytest, Unittest
    API Client: Postman

## Endpoints

| Endpoint                                 | Description                                           |
|------------------------------------------|-------------------------------------------------------|
| '`admin/`'                               | Admin panel                                           |
| '`swagger/`'                             | Swagger Document API endpoints, including parameters, request bodies, and response schemas.|
| '`redoc/`'                               | Redoc Document API endpoints, including parameters, request bodies, and response schemas.|
| '`api/v1/register/`'                    | Register a new user                                   |
| '`api/v1/login/`'                       | User login                                            |
| '`api/v1/logout/`'                      | User logout                                           |
| '`api/v1/user/retrieve/`'               | Retrieve authenticated user profile                   |
| '`api/v1/user/update/`'                 | Update authenticated user profile                     |
| '`api/weather/get-weather/`'                 | weather                    |

### Instruction to Run the Project

Clone the Repository:


```
git clone git@github.com:Kylych-dev/weather-app.git
cd weather-app
```

Set Up Docker:
Ensure Docker is installed and running on your machine.

Build and Run Docker Compose:

```
docker compose up --build 
```

This command builds the Docker images and starts the containers.

Access the API Documentation:
    Swagger Documentation: Visit http://localhost:8000/swagger/ in your web browser.
    Redoc Documentation: Visit http://localhost:8000/redoc/ in your web browser.

Examples of Requests

Register a New User: POST http://localhost:8000/api/v1/register/ <br>
User Login: POST http://localhost:8000/api/v1/login/ <br>
User Logout: POST http://localhost:8000/api/v1/logout/ <br>
Retrieve Authenticated User Profile: GET http://localhost:8000/api/v1/user/retrieve/ <br>
Update Authenticated User Profile: PUT http://localhost:8000/api/v1/user/update/ <br>
Get Weather Data: GET http://localhost:8000/api/weather/get-weather/ <br>



docker compose exec web ./manage.py test


### Run Tests:

Execute the following command to run the tests:

``` bash 
./manage pytest
```



## Contributing

telegram: **`@mirbekov0909`** <br>

email: **`tteest624@gmail.com`** <br>

email: **`mirbekov1kylych@gmail.com`**




