"""
Helper script to recreate the database with updated schema
Run this if you get column errors after model changes
"""
from backend.app import create_app, db
from backend.app.models import (
    User, Course, Module, Lesson, Enrollment, Progress,
    Quiz, Question, Lab, CLICommand, Announcement, Attempt
)

def recreate_database():
    """Drop all tables and recreate them with current schema"""
    app = create_app()
    
    with app.app_context():
        print("Dropping all tables...")
        db.drop_all()
        
        print("Creating all tables with updated schema...")
        db.create_all()
        
        # Recreate default admin
        from werkzeug.security import generate_password_hash
        admin = User(
            name='Admin User',
            email='admin@learnnet.com',
            password_hash=generate_password_hash('admin123'),
            role='admin',
            is_active=True,
            is_instructor_approved=True
        )
        db.session.add(admin)
        db.session.commit()
        
        print("Database recreated successfully!")
        print("Default admin user created:")
        print("   Email: admin@learnnet.com")
        print("   Password: admin123")
        print("\nYou can now run the seeding script to add networking content.")

if __name__ == '__main__':
    recreate_database()

