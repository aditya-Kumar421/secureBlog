
# SecureBlog

SecureBlog is a role-based access control (RBAC) blogging application designed for secure user authentication, authorization, and role-specific access to resources. The app ensures that roles like Admin, Editor, and Viewer have precise permissions tailored to their responsibilities, providing a streamlined and secure blogging platform.


## Tech Stack



**Framework:** Django Rest Framework

**Database:** SQLite

**Tools:** Postman for API testing, Swagger for API documentation

**Authentication:** JWT (JSON Web Token)


## Features

**Role-Based Access Control (RBAC):**

**Admin:**
Permissions: Full control over the application. Admin can create, view, update, and delete any blog post.
Can perform CRUD operations on all users’ blog posts.

**Editor:**
Permissions: Can create, view, update, and delete only their own posts.
Can view all posts but can only interact with their personal blog posts.

**Viewer:**
Permissions: Only authorized to view posts and cannot modify them.


## Installation


1. Clone the repository:

```CMD
git clone https://github.com/aditya-Kumar421/secureBlog.git
```

To run the server, you need to have Python installed on your machine. If you don't have it installed, you can follow the instructions [here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install it.

2. Install and Create a virtual environment:

```CMD
python -m venv env
```

3. Activate the virtual environment

```CMD
For Windows: env\Scripts\activate
For iOS:source env/bin/activate
cd blogapp
```


4. Install the dependencies:

```CMD
pip install -r requirements.txt
```

5. Set Up Database:

```
python manage.py migrate
```

6. Run the Development Server:

```
python manage.py runserver
```

7. Access the Endpoints:

```
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
```

    
## Documentation

The API endpoints for SecureBlog are fully documented and can be accessed through Swagger UI.

You can view the interactive API documentation and try out the endpoints by visiting the Swagger URL:
```CMD
http://127.0.0.1:8000/swagger/
```