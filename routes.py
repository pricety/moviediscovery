from app import app, db
import random
import os

import flask
from flask_login import login_user, current_user, LoginManager, logout_user
from flask_login.utils import login_required
from models import User, Rating

from wikipedia import get_wiki_link
from tmdb import get_movie_data

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_name):
    return User.query.get(user_name)


@app.route("/signup")
def signup():
    return flask.render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    username = flask.request.form.get("username")
    user = User.query.filter_by(username=username).first()
    if user:
        pass
    else:
        user = User(username=username)
        db.session.add(user)
        db.session.commit()

    return flask.redirect(flask.url_for("login"))


@app.route("/login")
def login():
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    username = flask.request.form.get("username")
    user = User.query.filter_by(username=username).first()
    if user:
        login_user(user)
        return flask.redirect(flask.url_for("mainpage"))

    else:
        return flask.jsonify({"status": 401, "reason": "Username or Password Error"})


MOVIE_IDS = [
    354912, 10625, 8291, 9806
]


@app.route("/rate", methods=["POST"])
def rate():
    data = flask.request.form
    rating = data.get("rating")
    comment = data.get("comment")
    movie_id = data.get("movie_id")

    new_rating = Rating(
        username=current_user.username,
        rating=rating,
        comment=comment,
        movie_id=movie_id,
    )

    db.session.add(new_rating)
    db.session.commit()
    return flask.redirect("mainpage")


@app.route("/")
def landing():
    if current_user.is_authenticated:
        return flask.redirect("mainpage")
    return flask.redirect("login")


@app.route("/logout")
def logout():
    logout_user()
    return flask.redirect("login")


@app.route("/mainpage")
@login_required
def mainpage():
    movie_id = random.choice(MOVIE_IDS)

    # API calls
    (title, tagline, genre, poster_image) = get_movie_data(movie_id)
    wikipedia_url = get_wiki_link(title)

    ratings = Rating.query.filter_by(movie_id=movie_id).all()

    return flask.render_template(
        "mainpage.html",
        title=title,
        tagline=tagline,
        genre=genre,
        poster_image=poster_image,
        wiki_url=wikipedia_url,
        ratings=ratings,
        movie_id=movie_id,
    )


@app.route("/redirection")
def redirection():
    return flask.redirect("edit_comments")


bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

# route for serving React page
@bp.route("/edit_comments")
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")


@app.route("/editcomments", methods=["POST"])
def edit_comments():
    user_ratings = Rating.query.filter_by(username=current_user.username).all()
    num_ratings = len(user_ratings)
    return flask.jsonify(
        ratings=[
            (
                user_ratings[i].movie_id,
                user_ratings[i].comment,
                user_ratings[i].rating,
                user_ratings[i].id,
            )

            for i in range(num_ratings)
        ]
    )

@app.route("/save_changes", methods=["POST"])
def save_changes():
  user_ratings = Rating.query.filter_by(username=current_user.username).all()
  num_ratings = len(user_ratings)
  rating_data = flask.request.get_json()
  for i in range(num_ratings):
    for j in rating_data:
      if i == j:
        db.session.delete(user_ratings)
        db.session.commit()
    return ("SAVED", print(rating_data))

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
