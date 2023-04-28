from werkzeug.security import generate_password_hash
from flask_migrate import Migrate
from flask import render_template

from app import create_app
from models.user import User
from models.database import db

app = create_app()
migrate = Migrate(app, db, compare_type=True)


@app.route('/')
def index():
    return render_template("index.html")

@app.cli.command('init_db')
def init_db():
    db.create_all()


@app.cli.command('create_admin')
def create_admin():
    admin = User(login='admin_login', first_name='first_adm', last_name='last_adm', email='admin@admin.ru', is_staff=True, password='test')
    admin.password = 'adm_pass'
    db.session.add(admin)
    print("created admin:", admin)
    db.session.commit()



if __name__== '__main__':
    app.run(host='0.0.0.0')