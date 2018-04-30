#!/usr/bin/env python3
from flask import Flask, render_template
import psycopg2
app = Flask(__name__)


@app.route('/')
def gett():
    db = psycopg2.connect(database='forum', user='bhanu', password='bhanu')
    d = db.cursor()
    c = db.cursor()
    e = db.cursor()
    c.execute("select * from query1vf limit 3;")
    d.execute("select * from query2vf limit 3;")
    e.execute('''select date, cast(error as decimal(10,2)) from query3vf
                 where query3vf.error > 1;''')
    error = e.fetchall()
    visits = d.fetchall()
    rows = c.fetchall()
    c.close
    d.close()
    e.close()
    return render_template('home.html', rows=rows, visits=visits, error=error)
    
    db.close()
if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug='true')

