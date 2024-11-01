import random
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from pars_wiki_web import wiki_pars_web


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()


@app.route('/')
@app.route('/home')
def index():
    with open("static/facts.txt") as inp:
        lines = inp.readlines()
        random_fact = random.choice(lines).strip()
    return render_template('index.html', random_fact=random_fact)


@app.route('/about')
def about():
    return render_template('contacts.html')


@app.route('/result', methods=['get', 'post'])
def result():
    if request.method == "POST":
        animal = request.form['text'].lower()
        animal.replace(' ', '_')
        results_of_search = wiki_pars_web(animal)
        is_dict = isinstance(results_of_search, dict)

        if is_dict:
            return render_template(
                "result.html",
                animal=animal,
                image_url=results_of_search['img_url'],
                article_url=results_of_search['article_url'],
                info=results_of_search['info']
            )
        else:
            return render_template("bad_result.html", bad_result=results_of_search)
    else:
        return "Get запрост"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
