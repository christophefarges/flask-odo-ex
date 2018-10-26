from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import config

import ptvsd
ptvsd.enable_attach(address = ('0.0.0.0', 5678))


application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(application)

from models import Test

@application.route('/', methods=['GET', 'POST'])
def index():
    tests = Test.query.all()
    print(tests)
    return render_template('index.html', tests=tests)

if __name__ == "__main__":
    application.run()
