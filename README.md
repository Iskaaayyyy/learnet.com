# LearnNet - Learning Management System

A comprehensive, role-based Learning Management System built with Python, Flask, SQLAlchemy, and modern web technologies.

## Features

### 🎭 Three User Roles

- **Student**: Enroll in courses, complete lessons, take quizzes, and track progress
- **Instructor**: Create and manage courses, modules, lessons, quizzes, and labs
- **Admin**: Manage users, approve instructors, and oversee the platform

### 🔐 Authentication & Authorization

- Secure session-based authentication using Flask-Login
- Role-based access control with route protection
- Automatic role-based dashboard redirection after login

### 📚 Core Functionality

- **Course Management**: Create, edit, publish, and manage courses
- **Content Structure**: Organize content with modules and lessons
- **Progress Tracking**: Automatic progress tracking for students
- **Enrollment System**: Students can enroll in published courses
- **Student Management**: Instructors can view enrolled students and their progress

## Project Structure

```
LearnNet/
├── backend/
│   └── app/
│       ├── __init__.py          # Flask app initialization
│       ├── models/               # Database models
│       │   ├── user.py
│       │   ├── course.py
│       │   ├── module.py
│       │   ├── lesson.py
│       │   ├── enrollment.py
│       │   ├── progress.py
│       │   ├── quiz.py
│       │   ├── question.py
│       │   ├── lab.py
│       │   ├── cli_command.py
│       │   ├── announcement.py
│       │   └── attempt.py
│       ├── routes/               # Route handlers
│       │   ├── auth.py
│       │   ├── main.py
│       │   ├── student.py
│       │   ├── instructor.py
│       │   └── admin.py
│       ├── templates/           # Jinja2 templates
│       │   ├── base.html
│       │   ├── auth/
│       │   ├── student/
│       │   ├── instructor/
│       │   └── admin/
│       └── static/              # Static files
│           ├── css/
│           └── js/
├── run.py                        # Application entry point
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Installation

1. **Clone or navigate to the project directory**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables** (optional):
   ```bash
   # Windows PowerShell
   $env:SECRET_KEY="your-secret-key-here"
   $env:DATABASE_URL="sqlite:///learnnet.db"
   
   # Linux/Mac
   export SECRET_KEY="your-secret-key-here"
   export DATABASE_URL="sqlite:///learnnet.db"
   ```

6. **Run the application**:
   ```bash
   python run.py
   ```

7. **Access the application**:
   Open your browser and navigate to `http://localhost:5000`

## Default Admin Account

A default admin account is automatically created on first run:

- **Email**: `admin@learnnet.com`
- **Password**: `admin123`

**⚠️ Important**: Change the default admin password in production!

## Database

The application uses SQLite by default (for development). The database file `learnnet.db` will be created automatically on first run.

For production, you can use PostgreSQL or MySQL by setting the `DATABASE_URL` environment variable:

```bash
# PostgreSQL
export DATABASE_URL="postgresql://user:password@localhost/learnnet"

# MySQL
export DATABASE_URL="mysql://user:password@localhost/learnnet"
```

## Usage Guide

### For Students

1. Register a new account (or login if you have one)
2. Browse available courses
3. Enroll in courses
4. Complete lessons and track your progress
5. View your dashboard for statistics

### For Instructors

1. Register as an instructor (requires admin approval)
2. Once approved, login to access instructor dashboard
3. Create courses and add content (modules, lessons)
4. Publish courses when ready
5. View enrolled students and their progress

### For Admins

1. Login with admin credentials
2. Approve pending instructor accounts
3. Manage users (activate/deactivate)
4. Manage courses (activate/deactivate)
5. View system statistics

## Key Features

### ✅ Proper ORM Relationships

- No duplicate relationships
- Explicit foreign keys where needed
- Clean separation of concerns
- One source of truth for each relationship

### 🔒 Security

- Password hashing with Werkzeug
- Session-based authentication
- Role-based route protection
- SQL injection protection via SQLAlchemy ORM

### 🎨 Modern UI

- Responsive design
- Clean, professional styling
- Intuitive navigation
- Flash message notifications

## Development

### Running in Development Mode

```bash
python run.py
```

The app runs in debug mode by default, which provides:
- Auto-reload on code changes
- Detailed error pages
- Debug toolbar (if installed)

### Database Migrations

For production, consider using Flask-Migrate for database migrations:

```bash
pip install Flask-Migrate
```

## Technologies Used

- **Backend**: Python 3.8+, Flask 3.0
- **Database**: SQLAlchemy ORM (SQLite/PostgreSQL/MySQL)
- **Authentication**: Flask-Login
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Templating**: Jinja2

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please refer to the project documentation or create an issue in the repository.

---

**Built with ❤️ for learning and education**

