#!/usr/bin/env python3
"""
Management script for the Flask application.
Useful for database operations and deployment tasks.
"""
import os
import sys
from flask.cli import FlaskGroup
from app import create_app, db
from app.models import User, CodeSubmission
from flask_migrate import upgrade

app = create_app()
cli = FlaskGroup(app)

@cli.command("init-db")
def init_db():
    """Initialize the database."""
    with app.app_context():
        db.create_all()
        print("Database initialized!")

@cli.command("migrate-db")
def migrate_db():
    """Run database migrations."""
    with app.app_context():
        upgrade()
        print("Database migrations completed!")

@cli.command("create-admin")
def create_admin():
    """Create an admin user."""
    with app.app_context():
        email = input("Enter admin email: ")
        password = input("Enter admin password: ")
        name = input("Enter admin name: ")
        
        user = User.query.filter_by(email=email).first()
        if user:
            print("User already exists!")
            return
        
        user = User(email=email, name=name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print(f"Admin user {email} created successfully!")

@cli.command("deploy-setup")
def deploy_setup():
    """Setup the application for deployment."""
    with app.app_context():
        # Create tables
        db.create_all()
        print("Database tables created!")
        
        # Run migrations
        try:
            upgrade()
            print("Database migrations completed!")
        except Exception as e:
            print(f"Migration warning: {e}")
        
        print("Deployment setup completed!")

if __name__ == '__main__':
    cli() 