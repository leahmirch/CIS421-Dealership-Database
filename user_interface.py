from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    tables = ['Car', 'Customer', 'Employee', 'CarTransaction', 'Dealership', 'ServiceAppointment', 'Part', 'CarParts', 'TestDrive']
    return render_template('index.html', tables=tables)

@app.route('/handle_query', methods=['POST'])
def handle_query():
    query_type = request.form['query_type']
        
    if query_type == 'view_table':
        selected_table = request.form['selected_table']
        return redirect(url_for('view_specific_table', table_name=selected_table))

    return redirect(url_for('index'))

@app.route('/view_specific_table', methods=['POST'])
def view_specific_table():
    table_name = request.form['selected_table']
    conn = sqlite3.connect('dealership.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    columns = [description[0] for description in c.description]
    conn.close()
    return render_template('view_table.html', rows=rows, table=table_name, columns=columns)

@app.route('/execute_query', methods=['POST'])
def execute_query():
    query = request.form.get('query', '')
    try:
        conn = sqlite3.connect('dealership.db')
        c = conn.cursor()
        c.execute(query)
        if query.lower().startswith('select'):
            rows = c.fetchall()
            columns = [desc[0] for desc in c.description]
            return render_template('query_results.html', rows=rows, columns=columns, error=None)
        else:
            conn.commit()
            return render_template('query_results.html', message="Query executed successfully.", error=None)
    except Exception as e:
        return render_template('query_results.html', error=str(e))
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
