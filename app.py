import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

@app.route('/skills')
def skills():
    # if request.method == 'POST':
    #     title = request.form['title']
    #     content = request.form['content']

    #     if not title:
    #         flash('Title is required!')
    #     else:
    #         conn = get_db_connection()
    #         conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
    #                      (title, content))
    #         conn.commit()
    #         conn.close()
    #         return redirect(url_for('index'))

    return render_template('skills.html')
@app.route('/studies')
def studies():
    # if request.method == 'POST':
    #     title = request.form['title']
    #     content = request.form['content']

    #     if not title:
    #         flash('Title is required!')
    #     else:
    #         conn = get_db_connection()
    #         conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
    #                      (title, content))
    #         conn.commit()
    #         conn.close()
    #         return redirect(url_for('index'))

    return render_template('studies.html')
@app.route('/')
def index():
    
    return render_template('index.html')
if __name__ =='__main__':  
    app.run(debug = True)  