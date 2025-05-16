from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metroittop.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)



@app.route("/start_page")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/comment")
def comment():
    posts = Post.query.all()
    return render_template("comment.html", posts=posts)


@app.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        post = Post(title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            return 'При добавлении статьи произошла ошибка!'


    else:
        return render_template('create.html')


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/comparison")
def comparison():
    return render_template("comparison.html")

@app.route("/question")
def question():
    return render_template("question.html")

@app.route("/myself")
def myself():
    return render_template("myself.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
