from flask import render_template, request, Blueprint
from app.models import Post, Quotes

main = Blueprint("main",__name__)


@main.route('/')
@main.route("/home")
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts, title="Home page")


@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/quotes")
def quotes():
    render_template("quotes",newauthor=newauthor)


