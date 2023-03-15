from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, mapped_column, relationship
from werkzeug.security import check_password_hash, generate_password_hash

Base = declarative_base()
app = Flask(__name__)
app.secret_key = 'secret key'

# Configure SQLAlchemy
engine = create_engine('sqlite:///example.db', echo=True)
Session = sessionmaker(bind=engine)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Define User model
class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(100))

    def __repr__(self):
        return f"<User(username='{self.username}')>"


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Todo(title='{self.title}', description='{self.description}')>"

Base.metadata.create_all(engine)


@login_manager.user_loader
def load_user(user_id):
    session = Session()
    user = session.query(User).get(int(user_id))
    session.close()
    return user


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session = Session()
        user = session.query(User).filter_by(username=username).first()
        session.close()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session = Session()
        if session.query(User).filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('register'))
        user = User(username=username, password=generate_password_hash(password))
        session.add(user)
        session.commit()
        session.close()
        flash('Registered successfully. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/dashboard')
@login_required
def dashboard():
    session = Session()
    user_id = session.query(User).filter_by(username=current_user.username).first().id
    todo_list = session.query(Todo).filter_by(user_id=user_id).all()
    session.close()
    return render_template('dashboard.html', todos=todo_list)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        session = Session()
        id = session.query(User).filter_by(username=current_user.username).first().id
        title = request.form['title']
        description = request.form['description']
        todo = Todo(title=title, description=description, user_id=id)
        session.add(todo)
        session.commit()
        session.close()
    return redirect(url_for('dashboard'))


@app.route('/remove', methods=['GET', 'POST'])
@login_required
def delete():
    id = request.args.get('id')
    session = Session()
    todo = session.query(Todo).filter_by(id=id).first()
    session.delete(todo)
    session.commit()
    session.close()
    return redirect(url_for('dashboard'))


@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    id = request.args.get('id')
    new_title = request.args.get['title']
    session = Session()
    todo = session.query(Todo).filter_by(id=id).first()
    todo.title = new_title
    session.commit()
    session.close()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
