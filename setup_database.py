import sqlite3

def setup_database():
    conn = sqlite3.connect('dealership.db')
    c = conn.cursor()

    # Create tables
    command = [
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
            phone TEXT,
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
    for command in command:
        c.execute(command)


    # Create tables
    sample_data = [
        # Inserting into Car table
        "INSERT INTO Car (make, model, year, VIN, purchase_price, sale_price, status, dealership_id) VALUES ('Toyota', 'Camry', 2020, 'JT1234567891234568', 23000, NULL, 'available', 1)",
        "INSERT INTO Car (make, model, year, VIN, purchase_price, sale_price, status, dealership_id) VALUES ('Honda', 'Civic', 2019, '2H1234567891234569', 18000, NULL, 'available', 1)",
        "INSERT INTO Car (make, model, year, VIN, purchase_price, sale_price, status, dealership_id) VALUES ('Ford', 'Mustang', 2021, '1F1234567891234570', 28000, 30000, 'sold', 2)",
        "INSERT INTO Car (make, model, year, VIN, purchase_price, sale_price, status, dealership_id) VALUES ('Chevrolet', 'Impala', 2018, '1G1234567891234571', 17000, NULL, 'maintenance', 2)",
        "INSERT INTO Car (make, model, year, VIN, purchase_price, sale_price, status, dealership_id) VALUES ('BMW', '3 Series', 2022, 'WBA1234567891234572', 35000, NULL, 'available', 3)",

        # Inserting into Customer table
        "INSERT INTO Customer (first_name, last_name, email, phone, address) VALUES ('John', 'Doe', 'john.doe@example.com', '555-1234', '123 Elm St, Somewhere')",
        "INSERT INTO Customer (first_name, last_name, email, phone, address) VALUES ('Jane', 'Smith', 'jane.smith@example.com', '555-2345', '456 Oak St, Anytown')",
        "INSERT INTO Customer (first_name, last_name, email, phone, address) VALUES ('Jim', 'Beam', 'jim.beam@example.com', '555-3456', '789 Pine St, Yourtown')",
        "INSERT INTO Customer (first_name, last_name, email, phone, address) VALUES ('Jill', 'Hill', 'jill.hill@example.com', '555-4567', '321 Maple St, Thistown')",
        "INSERT INTO Customer (first_name, last_name, email, phone, address) VALUES ('Jack', 'Black', 'jack.black@example.com', '555-5678', '654 Walnut St, Thatown')",

        # Inserting into Employee table
        "INSERT INTO Employee (first_name, last_name, role, salary, hire_date, dealership_id) VALUES ('Sam', 'Manager', 'manager', 60000, '2019-06-01', 1)",
        "INSERT INTO Employee (first_name, last_name, role, salary, hire_date, dealership_id) VALUES ('Alex', 'Salesperson', 'sales', 45000, '2020-07-15', 1)",
        "INSERT INTO Employee (first_name, last_name, role, salary, hire_date, dealership_id) VALUES ('Robin', 'Technician', 'service', 40000, '2018-05-23', 2)",
        "INSERT INTO Employee (first_name, last_name, role, salary, hire_date, dealership_id) VALUES ('Pat', 'Salesperson', 'sales', 45000, '2021-01-11', 2)",
        "INSERT INTO Employee (first_name, last_name, role, salary, hire_date, dealership_id) VALUES ('Taylor', 'Cleaner', 'maintenance', 35000, '2022-02-01', 3)",

        # Inserting into CarTransaction table
        "INSERT INTO CarTransaction (customer_id, car_id, employee_id, transaction_date, type, amount) VALUES (1, 1, 2, '2024-03-01', 'sale', 25000)",
        "INSERT INTO CarTransaction (customer_id, car_id, employee_id, transaction_date, type, amount) VALUES (2, 2, 2, '2024-03-02', 'sale', 20000)",
        "INSERT INTO CarTransaction (customer_id, car_id, employee_id, transaction_date, type, amount) VALUES (3, 3, 4, '2024-03-05', 'sale', 30000)",
        "INSERT INTO CarTransaction (customer_id, car_id, employee_id, transaction_date, type, amount) VALUES (4, 4, 5, '2024-03-10', 'sale', 19000)",
        "INSERT INTO CarTransaction (customer_id, car_id, employee_id, transaction_date, type, amount) VALUES (5, 5, 3, '2024-03-15', 'sale', 37000)",

        # Inserting into Dealership table
        "INSERT INTO Dealership (name, location, capacity) VALUES ('AutoWorld', '123 Dealership Rd, Automarket', 200)",
        "INSERT INTO Dealership (name, location, capacity) VALUES ('MotorMart', '456 Dealership Ave, Autocity', 150)",
        "INSERT INTO Dealership (name, location, capacity) VALUES ('CarCenter', '789 Dealership Blvd, Autotown', 100)",

        # Inserting into ServiceAppointment table
        "INSERT INTO ServiceAppointment (car_id, appointment_date, description, service_cost, employee_id) VALUES (1, '2024-04-01', 'Oil Change', 100, 3)",
        "INSERT INTO ServiceAppointment (car_id, appointment_date, description, service_cost, employee_id) VALUES (2, '2024-04-02', 'Tire Rotation', 75, 3)",
        "INSERT INTO ServiceAppointment (car_id, appointment_date, description, service_cost, employee_id) VALUES (3, '2024-04-03', 'Brake Inspection', 150, 3)",
        "INSERT INTO ServiceAppointment (car_id, appointment_date, description, service_cost, employee_id) VALUES (4, '2024-04-04', 'Engine Diagnostic', 200, 3)",
        "INSERT INTO ServiceAppointment (car_id, appointment_date, description, service_cost, employee_id) VALUES (5, '2024-04-05', 'Transmission Fluid Replacement', 250, 3)",

        # Inserting into Part table
        "INSERT INTO Part (name, price) VALUES ('Oil Filter', 25.99)",
        "INSERT INTO Part (name, price) VALUES ('Air Filter', 19.99)",
        "INSERT INTO Part (name, price) VALUES ('Brake Pads', 35.99)",
        "INSERT INTO Part (name, price) VALUES ('Spark Plug', 9.99)",
        "INSERT INTO Part (name, price) VALUES ('Timing Belt', 45.99)",

        # Inserting into CarParts table
        "INSERT INTO CarParts (car_id, part_id, install_date) VALUES (1, 1, '2024-04-01')",
        "INSERT INTO CarParts (car_id, part_id, install_date) VALUES (2, 2, '2024-04-02')",
        "INSERT INTO CarParts (car_id, part_id, install_date) VALUES (3, 3, '2024-04-03')",
        "INSERT INTO CarParts (car_id, part_id, install_date) VALUES (4, 4, '2024-04-04')",
        "INSERT INTO CarParts (car_id, part_id, install_date) VALUES (5, 5, '2024-04-05')",

        # Inserting into TestDrive table
        "INSERT INTO TestDrive (car_id, customer_id, employee_id, test_drive_date, duration, comments) VALUES (1, 1, 2, '2024-03-10', 30, 'Customer satisfied with the drive experience.')",
        "INSERT INTO TestDrive (car_id, customer_id, employee_id, test_drive_date, duration, comments) VALUES (2, 2, 2, '2024-03-11', 45, 'Customer inquired about financing options.')",
        "INSERT INTO TestDrive (car_id, customer_id, employee_id, test_drive_date, duration, comments) VALUES (3, 3, 4, '2024-03-12', 30, 'Customer interested in additional features.')",
        "INSERT INTO TestDrive (car_id, customer_id, employee_id, test_drive_date, duration, comments) VALUES (4, 4, 5, '2024-03-13', 60, 'Customer requested a follow-up appointment.')",
        "INSERT INTO TestDrive (car_id, customer_id, employee_id, test_drive_date, duration, comments) VALUES (5, 5, 3, '2024-03-14', 50, 'Customer compared multiple models.')"
    ]

    for command in sample_data:
        c.execute(command)

    conn.commit()
    conn.close()

setup_database()
