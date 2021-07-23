from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@127.0.0.1:5432/postgres"

db = SQLAlchemy()
db.init_app(app)

Migrate(app,db)

from models import user

@app.route('/')
def index():
    return 'ok'

if __name__ == "__main__":
    app.run()