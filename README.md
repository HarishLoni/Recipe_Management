
# Recipe_Management

A web application for managing and sharing a collection of recipes. The project allows users to add, view, edit, and share recipes with a user-friendly interface.




## Installation
Prerequisites :
Make sure you have the following installed: Python 3.x pip (Python's package installer) Virtual Environment (optional but recommended)

1] Clone the repository to your local machine:

```bash
  git clone https://github.com/your-username/Recipe_Management.git
```
2]Navigate to the project directory:
```bash
cd Recipe_Management
```
3]Create and activate a virtual environment:
```bash
python -m venv venv  
.\venv\Scripts\activate  # For Windows
```
4]Install the required dependencies:
```bash
pip install -r requirements.txt
```
5]Set up environment variables (if using django-environ or python-decouple):

Create a .env file in the root of the project.
Add your secret key and any other necessary variables:
```bash
THE_SECRET_KEY=your-secret-key
```
6]Apply migrations to set up the database:
```bash
python manage.py migrate
```
7]Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```
8]Run the development server:
```bash
python manage.py runserver
```
Now you can access the project at http://127.0.0.1:8000/.







