from werkzeug.security import generate_password_hash


from app import create_app
from models.user import User
from models.database import db

app = create_app()


@app.cli.command('init_db')
def init_db():
    db.create_all()


@app.cli.command('fill_db')
def fill_db():
    admin = User(login='admin_login', email='admin@admin.ru', pswd=generate_password_hash('dfgdg'), is_staff=True)
    user = User(login='login', email='name@name.ru', pswd=generate_password_hash('dfgddfg'), is_staff=False)
    db.session.add(admin)
    db.session.add(user)
    db.session.commit()

if __name__== '__main__':
    app.run(host='0.0.0.0')