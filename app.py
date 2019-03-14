from flask import Flask, render_template, request, redirect, url_for, flash
from db_functions import add_entry, get_entries, edit_entry, fetch_entry, search_entry
from datetime import datetime
from create_db import create_db
app = Flask(__name__)
app.secret_key = 'some_secret'



@app.route('/')
def index():
    entries = get_entries()
    msg = "Your entries.Happy Journalling"

    return render_template('index.html', entries=entries, msg=msg)


@app.route('/add', methods=['POST'])
def add():
    if request.method == "POST":
        date1 = datetime.date(datetime.now())
        entries = get_entries()
        print("date s" ,date1)
        add_entry(text1=request.form['title'], text2=request.form['details'], date1=datetime.date(datetime.now()))
        flash('Entry added successfully. If you want to make changes, please edit.')
        return redirect(url_for('index'))

    else:
        return redirect(url_for('index'))

    '''
    print(len(entries))
    print(entries)
    list1 = []
    for i in range(0,len(entries)):
        list1.append(entries[i][3])
    print("lists", list1)
        if str(date1) not in list1:

    '''







@app.route('/edit/<id>', methods=['GET','POST'])
def fetch(id):
    if request.method == "POST":
        text1=request.form['title']
        text2=request.form['details']

        entries = edit_entry(text1, text2, id=id)
        return redirect(url_for('index'))


    else:
        entries = fetch_entry(id)
        return render_template("edit.html", entries=entries)




@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':

        entries = search_entry(date1 =request.form['search_date'])
        if not entries:
            flash('Sorry!! No journal entry is available for the date')
            return render_template('search_results.html')

        print('search results',entries)
        return render_template('search_results.html', entries=entries)


if __name__ == '__main__':
    create_db()
    app.run(port = 8000 ,debug=True)