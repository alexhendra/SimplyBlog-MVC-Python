import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://simplyuser:lupa123pass@postgres:5432/simplyBlogDB'
SECRET_KEY = os.urandom(24)
SQLALCHEMY_TRACK_MODIFICATIONS = False
