from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()


# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # Тип данных int, primary_key=True - уникальность каждого id
#     title = db.Column(db.String(100), nullable=False)
#     intro = db.Column(db.String(300), nullable=False)
#     # макс. 100/300 символов, nullable=False - нельзя указать пустое знач.
#     text = db.Column(db.Text, nullable=False)
#     # Text - потому что статья может быть много символов,
#     # nullable=False - нельзя указать пустое знач.
#     date = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Article %r' % self.id  # Article выдается сам объект и его id


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
