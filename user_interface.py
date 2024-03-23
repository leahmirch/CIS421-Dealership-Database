from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view/<table>')
def view_table(table):
    conn = sqlite3.connect('dealership.db')
    c = conn.cursor()
    query = f"SELECT * FROM {table}"
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    return render_template('view_table.html', rows=rows, table=table)

@app.route('/execute_query', methods=['POST'])
def execute_query():
    query = request.form['query']
    conn = sqlite3.connect('dealership.db')
    c = conn.cursor()
    c.execute(query)
    if query.lower().startswith('select'):
        rows = c.fetchall()
        return render_template('view_query_results.html', rows=rows)
    else:
        conn.commit()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
