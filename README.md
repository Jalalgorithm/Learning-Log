## Learning Log

Learning Log is a web application designed to help individuals track their learning journey. Whether you're studying a new skill, mastering a subject, or just want to document your daily progress, Learning Log allows you to record and organize your learning entries in a structured way.


## Features
* User-Friendly Interface: Easily create, view, and manage your learning logs.
* Organized Categories: Group your learning into topics for better organization.
* Daily Entries: Add daily entries to track your progress for each topic.
* Edit and Update Logs: Revise or expand your logs as your learning evolves.
* Secure Access: User authentication ensures that only you can access your logs.


## How It Works

* Sign Up: Create an account to start tracking your learning.
* Create Topics: Organize your learning by creating topics such as "Python Programming" or "Data Science."
* Add Entries: Log daily updates for each topic, documenting what you learned.
* Review and Reflect: Look back on your logs to review your progress and plan future learning.

## Technologies Used
- Backend: Django (Python framework)
- Frontend: HTML, CSS, and Bootstrap for responsive design
- Database: SQLite 
- Deployment: Hosted on PythonAnywhere

## Installation and Setup

  1.Clone the repository:
  ```bash
  git clone https://github.com/jalalgorithm/learning-log.git
  cd learning-log
```
2. Set up a Virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Apply database migrations:
   ```bash
   python manage.py migrate

5.Run the development server:
  ```bash
  python manage.py runserver
```
Access the app at http://127.0.0.1:8000/.
