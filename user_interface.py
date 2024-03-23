from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    tables = ['Car', 'Customer', 'Employee', 'CarTransaction', 'Dealership', 'ServiceAppointment', 'Part', 'CarParts', 'TestDrive']
    return render_template('index.html', tables=tables)

@app.route('/handle_query', methods=['POST'])
def handle_query():
    query_type = request.form['query_type']

    if query_type == 'add_car':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        VIN = request.form['VIN']
        purchase_price = request.form['purchase_price']
        sale_price = request.form['sale_price']
        status = request.form['status']
        dealership_id = request.form['dealership_id']

        if not all([make, model, year, VIN, purchase_price, dealership_id]) or (status == 'sold' and not sale_price):
            flash('Error: Missing required fields.', 'error')
            return redirect(url_for('index'))
        
        conn = sqlite3.connect('dealership.db')
        c = conn.cursor()
        c.execute("""
            INSERT INTO Car (make, model, year, VIN, purchase_price, sale_price, status, dealership_id) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (make, model, year, VIN, purchase_price, sale_price if sale_price else None, status, dealership_id))
        conn.commit()
        conn.close()
        flash('Success: Car added to the database.', 'success')
        return redirect(url_for('index'))
        
    if query_type == 'add_customer':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        
        if not all([first_name, last_name, email, phone, address]):
            flash('Error: Missing required fields.', 'error')
            return redirect(url_for('index'))
        
        conn = sqlite3.connect('dealership.db')
        c = conn.cursor()
        c.execute("""
            INSERT INTO Customer (first_name, last_name, email, phone, address) 
            VALUES (?, ?, ?, ?, ?)
        """, (first_name, last_name, email, phone, address))
        conn.commit()
        conn.close()
        flash('Success: Customer added to the database.', 'success')
        return redirect(url_for('index'))
        
    elif query_type == 'view_table':
        selected_table = request.form['selected_table']
        return redirect(url_for('view_specific_table', table_name=selected_table))

    return redirect(url_for('index'))

@app.route('/view_specific_table/<table_name>')
def view_specific_table(table_name):
    conn = sqlite3.connect('dealership.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    columns = [description[0] for description in c.description]
    conn.close()
    return render_template('view_table.html', rows=rows, table=table_name, columns=columns)

if __name__ == '__main__':
    app.run(debug=True)
