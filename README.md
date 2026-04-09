notes application made with django
A simple, elegant web app for creating, managing, and searching personal notes. Built with Django, Bootstrap, and JavaScript, with user authentication and real-time search functionality.

Features:
-User Authentication:
  -Sign up, log in, and log out.
  -Each user sees only their notes.
  -Browser session expires on close for security.
-CRUD Notes:
  -Add, view, search, and delete notes.
  -Favorite important notes.
-Search Notes:
  -Real-time search using JavaScript.
  -Filter notes instantly as you type.
-Responsive Design:
  -Built with Bootstrap for mobile-friendly and desktop-friendly layouts.

  Tech Stack:
Backend: Django 5.2
Frontend: HTML, CSS, Bootstrap, JavaScript
Database: SQLite (default for Django projects)
Authentication: Django built-in User model
Version Control: Git & GitHub

Installation & Setup 
1. Clone the repo:
git clone https://github.com/juniperwoo/django-notes-app.git
cd django-notes-app/notesproject

2. Create a virtual environment and activate it:
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py migrate

5. Create a superuser (optional for admin access):
python manage.py createsuperuser

6. Run the development server:
python manage.py runserver

7. Open in browser: http://127.0.0.1:8000/

Usage:
-Sign up as a new user or log in with an existing account.
-Add notes using the input box and "Add" button.
-Delete notes using the X button and star butto to favorite your note.
-Use the search bar to filter your notes in real time.
-Log out to secure your account.

Author:

Juniper Poudyal

Computer Engineering Undergraduate
GitHub: https://github.com/juniperwoo