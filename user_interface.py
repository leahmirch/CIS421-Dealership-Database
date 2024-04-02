from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key_here'

@app.route('/')
def index():
    tables = ['Car', 'Customer', 'Employee', 'CarTransaction', 'Dealership', 'ServiceAppointment', 'Part', 'CarParts', 'TestDrive']
    conn = sqlite3.connect('dealership.db')
    c = conn.cursor()
    c.execute("SELECT customer_id, first_name, last_name FROM Customer ORDER BY last_name, first_name")
    customers = c.fetchall()
    c.execute("SELECT dealership_id, name FROM Dealership ORDER BY name")
    dealerships = c.fetchall()
    conn.close()
    return render_template('index.html', tables=tables, customers=customers, dealerships=dealerships)

# add car
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

# add customer
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

# view transaction
@app.route('/view_customer_transaction', methods=['POST'])
def view_customer_transaction():
    print("Attempting to view customer transactions...")
    customer_id = request.form['customer_id']
    print(f"Received customer_id: {customer_id}")
    
    try:
        conn = sqlite3.connect('dealership.db')
        c = conn.cursor()
        query = '''
                SELECT CarTransaction.transaction_id, Car.make, Car.model, Car.year, Employee.first_name, 
                CarTransaction.transaction_date, CarTransaction.type, CarTransaction.amount
                FROM CarTransaction
                JOIN Customer ON CarTransaction.customer_id = Customer.customer_id
                JOIN Car ON CarTransaction.car_id = Car.car_id
                JOIN Employee ON CarTransaction.employee_id = Employee.employee_id
                WHERE Customer.customer_id = ?
                '''
        print(f"Executing query: {query} with customer_id = {customer_id}")
        
        c.execute(query, (customer_id,))
        transactions = c.fetchall()
        print(f"Found {len(transactions)} transactions for customer_id = {customer_id}")
        
        columns = ['Transaction ID', 'Make', 'Model', 'Year', 'Employee First Name', 'Transaction Date', 'Type', 'Amount']
    except Exception as e:
        transactions = []
        print(f"An error occurred: {e}") 
        flash(f'An error occurred: {e}', 'error')
    finally:
        conn.close()

    return render_template('view_customer_transaction.html', transactions=transactions, columns=columns)

# view table
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
