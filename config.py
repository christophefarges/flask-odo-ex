import os

SQLALCHEMY_DATABASE_URI = "postgresql://"+os.environ["username"]+":"+os.environ["password"]+"@postgresql:5432/"+os.environ["database_name"]
