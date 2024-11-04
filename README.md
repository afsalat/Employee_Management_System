# Employee Management System

A Django-based Employee Management System that allows administrators to manage employees, assign roles, and configure permissions. The application leverages Django's built-in groups and permissions for role-based access control.

## Features

- **User Authentication and Authorization**: Uses Django's authentication system with custom roles (`Admin` and `Employee`).
- **Role-Based Access Control**: Allows role-based access to different features and views.
- **CRUD Operations**: Full CRUD support for managing employee records.
- **Custom User Model**: Extends Django’s `AbstractUser` to include custom roles.
- **Clean and Responsive UI**: Provides a user-friendly interface for managing employees and their roles.

## Prerequisites

- **Python 3.9+**
- **Django 4.2+**
- **SQLite (for local development)** or any preferred database
- **pip** for dependency management

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/employee-management-system.git
cd employee-management-system



2. Set Up a Virtual Environment
Using a virtual environment is recommended.

bash
Copy code
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure Environment Variables

env
Copy code
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, localhost
5. Run Migrations
Apply migrations to set up the database tables.

bash
Copy code
python manage.py migrate
6. Create a Superuser
Set up an admin account for the Django admin interface.

bash
Copy code
python manage.py createsuperuser
7. Run the Development Server
Start the Django development server.

bash
Copy code
python manage.py runserver
Navigate to http://127.0.0.1:8000 in your browser to access the application.


Usage
Managing Roles and Permissions
Admin Access: Use the Django admin interface to create groups and assign permissions to each group.
Assigning Roles: Users can have a role in the custom User model (either admin or employee).
Automatic Group Assignment: Users are automatically assigned to groups based on their role, allowing specific access rights.
Custom Permissions
You can add custom permissions in the Employee model via the Meta class:

python
Copy code
class Meta:
    permissions = [
        ("can_view_salary", "Can view employee salary"),
        ("can_edit_position", "Can edit employee position"),
    ]
Role Management Interface
The UI includes options to:

Edit and delete roles.
View all assigned permissions for each role.
Create new roles directly from the interface.
