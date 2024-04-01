from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key_here'

@app.route('/')
def index():
    tables = ['Car', 'Customer', 'Employee', 'CarTransaction', 'Dealership', 'ServiceAppointment', 'Part', 'CarParts', 'TestDrive']
    return render_template('index.html', tables=tables)

@app.route('/add_car', methods=['POST'])
def add_car():
    print(request.form)  
    try:
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        VIN = request.form['VIN']
        purchase_price = request.form['purchase_price']
        sale_price = request.form.get('sale_price', None)  # Optional field
        status = request.form['status']
        dealership_id = request.form['dealership_id']

        conn = sqlite3.connect('dealership.db')
        c = conn.cursor()
        c.execute('''INSERT INTO Car (make, model, year, VIN, purchase_price, sale_price, status, dealership_id)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                  (make, model, year, VIN, purchase_price, sale_price if sale_price else None, status, dealership_id))
        conn.commit()
        flash('Car added successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred: {e}', 'error')
    finally:
        conn.close()
    return redirect(url_for('index'))

@app.route('/add_customer', methods=['POST'])
def add_customer():
    print(request.form)  
    try:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        conn = sqlite3.connect('dealership.db')
        c = conn.cursor()
        c.execute('''INSERT INTO Customer (first_name, last_name, email, phone, address)
                     VALUES (?, ?, ?, ?, ?)''',
                  (first_name, last_name, email, phone, address))
        conn.commit()
        flash('Customer added successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred: {e}', 'error')
    finally:
        conn.close()
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
