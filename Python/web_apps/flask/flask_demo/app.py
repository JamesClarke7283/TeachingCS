from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    languages = ['Python', 'JavaScript', 'C#', 'C++', 'Java', 'PHP']
    return render_template('index.html', languages=languages)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
