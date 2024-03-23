import sqlite3

def setup_database():
    conn = sqlite3.connect('dealership.db')
    c = conn.cursor()

    # Create tables
    commands = [
        """CREATE TABLE IF NOT EXISTS Car (
            car_id INTEGER PRIMARY KEY,
            make TEXT,
            model TEXT,
            year INTEGER,
            VIN TEXT UNIQUE,
            purchase_price REAL,
            sale_price REAL,
            status TEXT CHECK(status IN ('available', 'sold', 'maintenance')),
            dealership_id INTEGER,
            FOREIGN KEY(dealership_id) REFERENCES Dealership(dealership_id)
        )""",
        """CREATE TABLE IF NOT EXISTS Customer (
            customer_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            phone TEXT UNIQUE,
            address TEXT
        )""",
        """CREATE TABLE IF NOT EXISTS Employee (
            employee_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            role TEXT,
            salary REAL,
            hire_date TEXT,
            dealership_id INTEGER,
            FOREIGN KEY(dealership_id) REFERENCES Dealership(dealership_id)
        )""",
        """CREATE TABLE IF NOT EXISTS CarTransaction (
            transaction_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            car_id INTEGER,
            employee_id INTEGER,
            transaction_date TEXT,
            type TEXT CHECK(type IN ('purchase', 'sale')),
            amount REAL,
            FOREIGN KEY(customer_id) REFERENCES Customer(customer_id),
            FOREIGN KEY(car_id) REFERENCES Car(car_id),
            FOREIGN KEY(employee_id) REFERENCES Employee(employee_id)
        )""",
        """CREATE TABLE IF NOT EXISTS Dealership (
            dealership_id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            capacity INTEGER
        )""",
        """CREATE TABLE IF NOT EXISTS ServiceAppointment (
            service_appointment_id INTEGER PRIMARY KEY,
            car_id INTEGER,
            appointment_date TEXT,
            description TEXT,
            service_cost REAL,
            employee_id INTEGER,
            FOREIGN KEY(car_id) REFERENCES Car(car_id),
            FOREIGN KEY(employee_id) REFERENCES Employee(employee_id)
        )""",
        """CREATE TABLE IF NOT EXISTS Part (
            part_id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL
        )""",
        """CREATE TABLE IF NOT EXISTS CarParts (
            car_parts_id INTEGER PRIMARY KEY,
            car_id INTEGER,
            part_id INTEGER,
            install_date TEXT,
            FOREIGN KEY(car_id) REFERENCES Car(car_id),
            FOREIGN KEY(part_id) REFERENCES Part(part_id)
        )""",
        """CREATE TABLE IF NOT EXISTS TestDrive (
            test_drive_id INTEGER PRIMARY KEY,
            car_id INTEGER,
            customer_id INTEGER,
            employee_id INTEGER,
            test_drive_date TEXT,
            duration INTEGER, -- Duration in minutes
            comments TEXT,
            FOREIGN KEY(car_id) REFERENCES Car(car_id),
            FOREIGN KEY(customer_id) REFERENCES Customer(customer_id),
            FOREIGN KEY(employee_id) REFERENCES Employee(employee_id)
        )"""
    ]

    # Execute table creation queries
    for command in commands:
        c.execute(command)

        # Inserting into Car table
        """INSERT INTO Car (make, model, year, VIN, purchase_price, sale_price, status, dealership_id) 
        VALUES
        ('Toyota', 'Camry', 2020, 'JT1234567891234567', 23000, 25000, 'available', 1),
        ('Honda', 'Civic', 2019, '2H1234567891234567', 18000, 20000, 'available', 1),
        ('Ford', 'Mustang', 2021, '1F1234567891234567', 28000, 30000, 'sold', 2),
        ('Chevrolet', 'Impala', 2018, '1G1234567891234567', 17000, 19000, 'maintenance', 2),
        ('BMW', '3 Series', 2022, 'WBA1234567891234567', 35000, 37000, 'available', 3); )"""

        # Inserting into Customer table
        """INSERT INTO Customer (first_name, last_name, email, phone, address) 
        VALUES
        ('John', 'Doe', 'john.doe@example.com', '555-1234', '123 Elm St, Somewhere'),
        ('Jane', 'Smith', 'jane.smith@example.com', '555-2345', '456 Oak St, Anytown'),
        ('Jim', 'Beam', 'jim.beam@example.com', '555-3456', '789 Pine St, Yourtown'),
        ('Jill', 'Hill', 'jill.hill@example.com', '555-4567', '321 Maple St, Thistown'),
        ('Jack', 'Black', 'jack.black@example.com', '555-5678', '654 Walnut St, Thatown'); )"""

        # Inserting into Employee table
        """INSERT INTO Employee (first_name, last_name, role, salary, hire_date, dealership_id) 
        VALUES
        ('Sam', 'Manager', 'Manager', 60000, '2019-06-01', 1),
        ('Alex', 'Salesperson', 'Sales', 45000, '2020-07-15', 1),
        ('Robin', 'Technician', 'Service', 40000, '2018-05-23', 2),
        ('Pat', 'Salesperson', 'Sales', 45000, '2021-01-11', 2),
        ('Taylor', 'Cleaner', 'Maintenance', 35000, '2022-02-01', 3); )"""

        # Inserting into CarTransaction table
        """INSERT INTO CarTransaction (customer_id, car_id, employee_id, transaction_date, type, amount) 
        VALUES
        (1, 1, 2, '2024-03-01', 'sale', 25000),
        (2, 2, 2, '2024-03-02', 'sale', 20000),
        (3, 3, 4, '2024-03-05', 'sale', 30000),
        (4, 4, 5, '2024-03-10', 'sale', 19000),
        (5, 5, 3, '2024-03-15', 'sale', 37000); )"""

        # Inserting into Dealership table
        """INSERT INTO Dealership (name, location, capacity) 
        VALUES
        ('AutoWorld', '123 Dealership Rd, Automarket', 200),
        ('MotorMart', '456 Dealership Ave, Autocity', 150),
        ('CarCenter', '789 Dealership Blvd, Autotown', 100); )"""

        # Inserting into ServiceAppointment table
        """INSERT INTO ServiceAppointment (car_id, appointment_date, description, service_cost, employee_id) 
        VALUES
        (1, '2024-04-01', 'Oil Change', 100, 3),
        (2, '2024-04-02', 'Tire Rotation', 75, 3),
        (3, '2024-04-03', 'Brake Inspection', 150, 3),
        (4, '2024-04-04', 'Engine Diagnostic', 200, 3),
        (5, '2024-04-05', 'Transmission Fluid Replacement', 250, 3); )"""

        # Inserting into Part table
        """INSERT INTO Part (name, price) 
        VALUES
        ('Oil Filter', 25.99),
        ('Air Filter', 19.99),
        ('Brake Pads', 35.99),
        ('Spark Plug', 9.99),
        ('Timing Belt', 45.99); )"""

        # Inserting into CarParts table
        """INSERT INTO CarParts (car_id, part_id, install_date) 
        VALUES
        (1, 1, '2024-04-01'),
        (2, 2, '2024-04-02'),
        (3, 3, '2024-04-03'),
        (4, 4, '2024-04-04'),
        (5, 5, '2024-04-05'); )"""

        # Inserting into TestDrive table
        """INSERT INTO TestDrive (car_id, customer_id, employee_id, test_drive_date, duration, comments) 
        VALUES
        (1, 1, 2, '2024-03-10', 30, 'Customer satisfied with the drive experience.'),
        (2, 2, 2, '2024-03-11', 45, 'Customer inquired about financing options.'),
        (3, 3, 4, '2024-03-12', 30, 'Customer interested in additional features.'),
        (4, 4, 5, '2024-03-13', 60, 'Customer requested a follow-up appointment.'),
        (5, 5, 3, '2024-03-14', 50, 'Customer compared multiple models.'); )"""

    conn.commit()
    conn.close()

setup_database()






# instructions for how to run / access the UI (on my MacOS)

# cd desktop/desktop/school/U\ of\ M\ Dearborn/4\ Winter\ 2024/CIS\ 421/project/Dealership\ Database/
# python3 setup_database.py
# python3 -m venv venv
# source venv/bin/activate
# pip install flask
# python3 user_interface.py
# paste http://127.0.0.1:5000 into a browser