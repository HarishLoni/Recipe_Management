# Recipe_Management
 A web application for managing and sharing a collection of recipes. The project allows users to add, view, edit, and share recipes with a user-friendly interface
# Installation
# Prerequisites
Make sure you have the following installed:
Python 3.x
pip (Python's package installer)
Virtual Environment (optional but recommended)
\n
#Steps to Install
Clone the repository to your local machine:
Copy code
git clone https://github.com/your-username/Recipe_Management.git

Navigate to the project directory:
Copy code
cd Recipe_Management

Create and activate a virtual environment:
Copy code
python -m venv venv
.\venv\Scripts\activate   # For Windows

Install the required dependencies:
Copy code
pip install -r requirements.txt

Set up environment variables (if using django-environ or python-decouple):
Create a .env file in the root of the project.
Add your secret key and any other necessary variables:
Copy code
THE_SECRET_KEY=your-secret-key

Apply migrations to set up the database:
Copy code
python manage.py migrate

Create a superuser (optional, for admin access):
Copy code
python manage.py createsuperuser

Run the development server:
Copy code
python manage.py runserver
Now you can access the project at http://127.0.0.1:8000/
