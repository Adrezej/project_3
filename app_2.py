from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database file
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(12), nullable=False)  # Updated to store phone numbers


@app.route('/')
def index():
    return render_template('phone_form.html')


@app.route('/', methods=['POST'])
def process_form():
    name = request.form.get('name')
    phone = request.form.get('phone')

    # Сохраняем данные в базу данных
    user = User(name=name, phone=phone)
    db.session.add(user)
    db.session.commit()

    return f'Thank you, {name}! Your phone number ({phone}) has been saved to the database.'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
