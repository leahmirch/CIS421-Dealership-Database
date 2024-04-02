## CIS421 Winter 2024 Programming Assignment : Dealership Database

### Student Names and Emails
- Leah Mirch (lmirch@umich.edu)
- Andrew Leutzinger (aleut@umich.edu)

### Introduction
This project aims to design and implement a relational database system for managing data related to an enterprise. The focus is on understanding real-world data requirements, designing an appropriate database schema, and utilizing SQL for querying and updating the database. The database schema is designed based on an Entity-Relationship (ER) diagram, which is then converted into a relational database schema. 

### Running Instructions
#### Running on Windows:
NOTE: THIS IS UNTESTED
(I do not have a windows device to test this on)
```bash
make windows
Paste http://127.0.0.1:5000 into a browser to access the user interface
```

#### Running on MacOS:
```bash
make mac
Paste http://127.0.0.1:5000 into a browser to access the user interface
```

### Tables of the Database
#### Car
- **Primary Key**: car_id
- **Foreign Key**: dealership_id references Dealership(dealership_id)
- **Attributes**: make, model, year, VIN, purchase_price, sale_price, status, dealership_id
- **Use**: This table stores information about each car in the dealership's inventory. It includes details like make and model, the Vehicle Identification Number (VIN), the purchase and potential sale price, and the current status (e.g., available, sold, under maintenance). The dealership_id links each car to its respective dealership location.

#### Customer
- **Primary Key**: customer_id
- **Attributes**: first_name, last_name, email, phone, address
- **Use**: The Customer table holds information about the dealership's customers. It includes personal contact details and can be used to track customer interactions, sales, and service appointments.

#### Employee
- **Primary Key**: employee_id
- **Foreign Key**: dealership_id references Dealership(dealership_id)
- **Attributes**: first_name, last_name, role, salary, hire_date, dealership_id
- **Use**: This table records data about the dealership's employees, including their role (e.g., salesperson, mechanic), salary, and hire date. Employees are also linked to a specific dealership location.

#### CarTransaction
- **Primary Key**: transaction_id
- **Foreign Keys**: customer_id references Customer(customer_id), car_id references Car(car_id), employee_id references Employee(employee_id)
- **Attributes**: customer_id, car_id, employee_id, transaction_date, type, amount
- **Use**: The CarTransaction table is used to record sales and purchases of cars. Each transaction is linked to a car, a customer, and an employee who facilitated the transaction. It includes the date, the type of transaction, and the transaction amount.

#### Dealership
- **Primary Key**: dealership_id
- **Attributes**: name, location, capacity
- **Use**: This table keeps track of dealership locations. It includes the name and location of each dealership and its car holding capacity.

#### ServiceAppointment
- **Primary Key**: service_appointment_id
- **Foreign Keys**: car_id references Car(car_id), employee_id references Employee(employee_id)
- **Attributes**: car_id, appointment_date, description, service_cost, employee_id
- **Use**: The ServiceAppointment table manages appointments for car services and repairs. It includes details of the service provided, the cost, the date of the appointment, and the employee responsible for the service.

#### Part
- **Primary Key**: part_id
- **Attributes**: name, price
- **Use**: This table catalogs all parts that can be ordered or used in repairs and services by the dealership. Each part has a name and price associated with it.

#### CarParts
- **Primary Key**: car_parts_id
- **Foreign Keys**: car_id references Car(car_id), part_id references Part(part_id)
- **Attributes**: car_id, part_id, install_date
- **Use**: The CarParts table records the parts that have been installed in each car. It could be used for inventory management, service history, and billing purposes.

#### TestDrive
- **Primary Key**: test_drive_id
- **Foreign Keys**: car_id references Car(car_id), customer_id references Customer(customer_id), employee_id references Employee(employee_id)
- **Attributes**: car_id, customer_id, employee_id, test_drive_date, duration, comments
- **Use**: This table keeps records of test drives offered to customers. It logs which customer tested which car, the employee who facilitated the test drive, the date and duration of the test drive, and any comments about the customer's experience or feedback on the car.

### Commands Implemented
- **View Tables Command**: The "View Tables" feature enables users to select and view different tables within the dealership's database, such as Cars, Customers, Employees, Transactions, Dealerships, Service Appointments, Parts, Car Parts, and Test Drives. This functionality provides a comprehensive overview of the dealership's operations, from inventory and customer interactions to employee details and financial transactions.Users can select a table from a dropdown menu, which dynamically updates the page to display the contents of the chosen table. The system presents the data in a tabulated format, with each column representing a field in the database. This allows for easy reading and understanding of the database's current state, offering insights into various aspects of the dealership's operations.
- **Add Car Command**: The "Add Car" feature allows users to insert new car records into the dealership's database directly from the web interface. This functionality is crucial for keeping the inventory up-to-date and provides a quick way to add new arrivals, ensuring that the dealership's offerings are accurately reflected on the system. To add a car, users must fill out a form providing details such as make, model, year, VIN (Vehicle Identification Number), purchase price, sale price (optional until the car is sold), status (available, sold, maintenance), and the dealership ID where the car is located. The system performs validations to ensure that all required fields are filled. If a car is marked as sold, the sale price becomes a required field. Upon successful submission, the car is added to the database, and the user is notified of the success. If there are missing fields or other errors, the user is alerted to correct the information and resubmit.
- **Add Customer Command**: The "Add Customer" feature in the Dealership Database Interface allows users to register new customers into the dealership's system. This functionality is essential for maintaining a detailed record of the dealership's clientele, which is beneficial for sales tracking, customer service, and marketing purposes. To add a customer, users are required to fill in a form specifying the customer's first name, last name, email, phone number, and address. The system checks to ensure that all fields are completed to maintain a comprehensive customer database. Once the form is submitted successfully, the customer's information is stored in the database, and the user receives a notification confirming the successful addition. If any required information is missing or if there's an error in the submission, the user is prompted to correct the details and resubmit the form. This streamlined process ensures the dealership's customer records are always up-to-date and accurate.
- **View Customer Transaction**: The "View Customer Transaction" feature in the Dealership Database Interface allows the user to view all of the details of a specified customers transaction, given their first and last name. The functionality is important for the dealership, holding a record of all customer sales. The given values will be the transaction id, the cars: make, model, and year, the sale employees first name, transaction date, the type of transaction, and finally the amount of the transaction. It is important that all of the data is accurate and accounted for at all times. This feature can be used so the dealership may have access to customer transactions upon customer or manager request.
- **Car Transfer**: The "Car Transfer" feature will allow dealerships to transfer cars from one to the other. In some cases, a customer may want to purchse a car that a dealership does not have, as well as the dealership being further than the customer wishes to travel, to purchase the vehicle. To request a car transfer, the user must enter the car's: make, model, and year, as well as the dealership name the car is currently at and finally what dealership the car is to be transfered to. In order for this functionality to be successful, the car must be availible for sale. If the car is 'sold' or in 'maintenence' the transfer will be declined. When the request is successful, the cars dealership id is updated within the car records. The car transfer will allow the upmost convenience to all customers, and this functionality allows the dealerships to maintain records of inventory at each location.
- **Update Car Price**: The "Update Car Price" feature in the dealership database will allow the user to change the current price of a single car within the database. The user will enter the car make, car model, and car year. From here the dealership will be able to markup or markdown the current price of the vehicle by percentage. The current value of the car will be either deducted or raised and updated into the cars purchase price. the "Update Car Price" functionality keeps all car prices up to date, ensuring no errors in customer expectation as far as what they intend to spend.
- **New Cars Maintenance**: The "New Service" feature allows the the user to add a new service appointment for a car that alrewady exists within the database. The user must enter the car make, car model, car year, and choose from which service is being performed on the car. The date will to be used will be the next available date for a service. This data will be stored as a new entry in the ServiceAppointment table. This feature will allow for the dealership to keep track of which service is needed to perform next, ensuring efficiency of completion.

### Each Student's Role
- Leah Mirch: Developed code for the initial database, created UI, designed and implemented query commands. Created commands for: view tables. Created, and developed the custom query entry field, tested thoroughly with custom high level queries. Designed the database's user interface to handle many inputs and required fields. Created and developed makefile. Created and updated README file. Redesigned UI to look presentable. Created ER Diagram.

### Additional Information
Github Repository: (https://github.com/leahmirch/Dealership-Database) - This repository documents the development process, including code commits, progress tracking, and collaboration. It serves as a central platform for code management and version control, facilitating a structured and efficient development workflow.
