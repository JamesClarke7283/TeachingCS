from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///polling.db'
app.secret_key = "secret key"

db = SQLAlchemy(app)


class Poll(db.Model):
    __tablename__ = 'polls'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False, unique=True)
    options = db.relationship('Option', backref='polls', lazy=True)


class Option(db.Model):
    __tablename__ = 'options'
    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.String(200), nullable=False)
    option_count = db.Column(db.Integer, nullable=False, default=0)
    poll_id = db.Column(db.ForeignKey("polls.id"), nullable=False)


@app.route("/")
def home():
    polls = db.session.query(Poll).all()
    return render_template("home.html", polls=polls) 


@app.route("/new_poll", methods=["POST", "GET"])
def new_poll():
    if request.method == "POST":
        title = request.form["title"]
        poll = Poll(question=title)
        db.session.add(poll)
        db.session.commit()
        resp = make_response(redirect(url_for("home")))
        resp.set_cookie("poll_id", str(poll.id))
        return resp
    else:
        return redirect(url_for("home"))


@app.route("/new_option", methods=["POST", "GET"])
def new_option():
    if request.method == "POST":
        answer = request.form["answer"]
        option = Option(option=answer)
        db.session.add(option)
        db.session.commit()
        options = db.session.query(Option).all()
        return redirect(url_for("home", options=options))


def main():
    with app.app_context():
        db.create_all()
    app.run(debug=True)


if __name__ == "__main__":
    main()
