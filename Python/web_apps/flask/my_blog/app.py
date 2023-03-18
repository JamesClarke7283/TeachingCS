from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash


"""Steps to make
1. Make a login/register/logout system with Flask_Login
2. Make a Main Page
3. Make List of Posts
4. Button to make New Posts and delete old ones.
5. Make a commenting system.
"""

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

# Create the database object
db = SQLAlchemy(app)

# Create the database model


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.ForeignKey("users.id"), nullable=False)


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.ForeignKey("blog_posts.id"), nullable=False)
    author_id = db.Column(db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)


@app.route('/')
def index():
    blog_posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=blog_posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for('index'))
    else:
        flash('Invalid username or password.')
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
