from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from flask import Flask
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('name')
    def validate_name(self,key,name):
        if not name:
            raise ValueError("All author must have a name")
        return name
    @validates('phone number')
    def validate_phone_number(self,key,phone_number):
        if len(phone_number)!=10:
            raise ValueError("Invalid phone number")
        return phone_number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  

    @validates('title')
    def validate_title(self,key,title):
        clickbait_keywords = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(keyword in title for keyword in clickbait_keywords):
            raise ValueError("Post title must contain one of the following: 'Won't Believe', 'Secret', 'Top', 'Guess'.")
        return title
    @validates('content')
    def validate_content(self, key,content):
        if len(content)<250:
            raise ValueError("Post content must be at least 250 characters")
        return content
    @validates('summary')
    def validate_summary(self,key, summary):
        if len(summary)>250:
            raise ValueError("Summary must be more than summary")
        return summary
    @validates('category')
    def validate_category(self, key, category):
        valid_categories = ['Fiction', 'Non-Fiction']
        if category not in valid_categories:
            raise ValueError("Post category must be either Fiction or Non-Fiction.")
        return category



    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
