from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3


app = Flask(__name__)

# Database initialization
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''
   CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      first_name TEXT NOT NULL,
      last_name TEXT NOT NULL,
      middle_name TEXT,
      iin TEXT NOT NULL,
      phone TEXT NOT NULL,
      email TEXT NOT NULL
   )
''')
conn.commit()
conn.close()


@app.route('/')
def index():
    return render_template('page1.html')


@app.route('/page1')
def page1():
    return render_template('page1.html')


@app.route('/page2', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        middle_name = request.form['middle-name']
        iin = request.form['iin']
        phone = request.form['phone']
        email = request.form['email']

        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO users (first_name, last_name, middle_name, iin, phone, email)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, middle_name, iin, phone, email))
        conn.commit()
        conn.close()

        return redirect(url_for('page4'))

    return render_template('page2.html')


@app.route('/page3')
def page3():
    return render_template('page3.html')


@app.route('/page4')
def page4():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    conn.close()

    return render_template('page4.html', data=data)


@app.route('/page5')
def page5():
    return render_template('page5.html')


if __name__ == "__main__":
    app.run()
