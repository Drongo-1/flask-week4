from flask import render_template, request, Blueprint
from app.models import Post

main = Blueprint("main",__name__)


@main.route('/')
@main.route("/home")
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts, title="Home page")


@main.route("/about")
def about():
    return render_template("about.html", name="namess")

@main.route("/quote")
def quote():
    dict = {1:{'author':'Ngugidavid', 'title':'authords'},
            2:{'author':'Ngugidavid2', 'title':'authords2'}}
    res=key, val=random.choice(list(dict.items()))
    author=str(val['author'])
    render_template("quotes.html", author=author)
    