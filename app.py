from flask import Flask, render_template, request, redirect, url_for
from db_functions import add_entry, get_entries
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    entries = get_entries()
    return render_template('index.html', entries=entries)


@app.route('/add', methods=['POST'])
def add():
    add_entry(text1=request.form['title'], text2=request.form['details'], date1= datetime.date(datetime.now()))

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port = 8000 ,debug=True)