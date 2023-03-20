from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash


"""Steps to make
1. Make a login/register/logout system with Flask_Login
2. Make a Main Page
3. Make List of Posts
4. Button to make New Posts and delete old ones.
5. Make a commenting system.
"""

app = Flask(__name__)
app.secret_key = 'secret key'
# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

# Create the database object
db = SQLAlchemy(app)

# Create login manager
login_manager = LoginManager()
login_manager.init_app(app)

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


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route('/')
def index():
    blog_posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=blog_posts, current_user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username != '' and password != '':
            user = User(username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            flash('Registered successfully.', category='success')
        else:
            flash('Please enter a username and password.', category='error')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', category="error")
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('index'))


@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    title = request.form['title']
    content = request.form['content']
    author_id = current_user.id
    post = BlogPost(title=title, content=content, author_id=author_id)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = BlogPost.query.filter_by(id=post_id).first()
    comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template('post.html', post=post, comments=comments, current_user=current_user, User=User)


@app.route('/delete_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = BlogPost.query.filter_by(id=post_id).first()
    if post.author_id == current_user.id:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('index'))


@app.route("/new_comment", methods=['GET', 'POST'])
@login_required
def new_comment():
    post_id = None
    if request.method == 'POST':
        post_id = request.form['post_id']
        content = request.form['content']
        author_id = current_user.id
        comment = Comment(post_id=post_id, content=content, author_id=author_id)
        db.session.add(comment)
        db.session.commit()
    else:
        post_id = request.args.get("post_id")
    return redirect(url_for('post', post_id=post_id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
