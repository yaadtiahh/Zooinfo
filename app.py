from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from pars_wiki import wiki_pars_web


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('contacts.html')


@app.route('/result', methods=['get', 'post'])
def result():
    if request.method == "POST":
        animal = request.form['text']
        animal.replace(' ', '_')
        pars = wiki_pars_web(animal)
        return render_template(
            "result.html",
            animal=animal,
            image_url=f"https://{pars[0]}",
            article_url=pars[1],
            info=pars[2]
        )
    else:
        return "Get запрост"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
