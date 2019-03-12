from flask import Flask, render_template, request, redirect, url_for, flash
from db_functions import add_entry, get_entries, edit_entry, fetch_entry
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    entries = get_entries()
    msg = "Your entries.Happy Journalling"

    return render_template('index.html', entries=entries, msg=msg)


@app.route('/add', methods=['POST'])
def add():
    date1 = datetime.date(datetime.now())
    entries = get_entries()
    print("date s" ,date1)
    print(len(entries))
    print(entries)
    list1 = []
    for i in range(0,len(entries)):
        list1.append(entries[i][3])
    print("lists", list1)


    if str(date1) not in list1:
        add_entry(text1=request.form['title'], text2=request.form['details'], date1=datetime.date(datetime.now()))
        flash('Entry added successfully. If you want to make changes, please edit.')

        return redirect(url_for('index'))
    else:

        flash('Oops!!! Journal entry exists for this day already. Would you like to edit?')
        return redirect(url_for('index'))




@app.route('/edit/<id>', methods=['GET','POST'])
def fetch(id):
    if request.method == "POST":
        print(request.method)
        text1=request.form['title']
        text2=request.form['details']
        print(text1)

        entries = edit_entry(text1, text2, id=id)
        print(entries)
        return redirect(url_for('index'))


    else:
        entries = fetch_entry(id)
        print(request.method)
        print("PICKING ENTRIES" ,entries)
        return render_template("edit.html", entries=entries)


if __name__ == '__main__':
    app.run(port = 8000 ,debug=True)