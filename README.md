## CIS421 Winter 2024 Programming Assignment : Dealership Database

### Student Names and Emails
- Leah Mirch (lmirch@umich.edu)
- Andrew Leutzinger (aleut@umich.edu)

### Introduction
txt

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

### Each Student's Role
- Leah Mirch: Developed code for the inital database, created UI, designed and implimented query commands. Created commands: view tables, add car. Designed the database's user interface to handle many inputs and required feilds.

### Commands Implemented
- **View Tables Command**: The "View Tables" feature enables users to select and view different tables within the dealership's database, such as Cars, Customers, Employees, Transactions, Dealerships, Service Appointments, Parts, Car Parts, and Test Drives. This functionality provides a comprehensive overview of the dealership's operations, from inventory and customer interactions to employee details and financial transactions.Users can select a table from a dropdown menu, which dynamically updates the page to display the contents of the chosen table. The system presents the data in a tabulated format, with each column representing a field in the database. This allows for easy reading and understanding of the database's current state, offering insights into various aspects of the dealership's operations.
- **Add Car Command**: The "Add Car" feature allows users to insert new car records into the dealership's database directly from the web interface. This functionality is crucial for keeping the inventory up-to-date and provides a quick way to add new arrivals, ensuring that the dealership's offerings are accurately reflected on the system. To add a car, users must fill out a form providing details such as make, model, year, VIN (Vehicle Identification Number), purchase price, sale price (optional until the car is sold), status (available, sold, maintenance), and the dealership ID where the car is located. The system performs validations to ensure that all required fields are filled. If a car is marked as sold, the sale price becomes a required field. Upon successful submission, the car is added to the database, and the user is notified of the success. If there are missing fields or other errors, the user is alerted to correct the information and resubmit.
- **Add Customer Command**: The "Add Customer" feature in the Dealership Database Interface allows users to register new customers into the dealership's system. This functionality is essential for maintaining a detailed record of the dealership's clientele, which is beneficial for sales tracking, customer service, and marketing purposes. To add a customer, users are required to fill in a form specifying the customer's first name, last name, email, phone number, and address. The system checks to ensure that all fields are completed to maintain a comprehensive customer database. Once the form is submitted successfully, the customer's information is stored in the database, and the user receives a notification confirming the successful addition. If any required information is missing or if there's an error in the submission, the user is prompted to correct the details and resubmit the form. This streamlined process ensures the dealership's customer records are always up-to-date and accurate.

### Additional Information
Github Repository: (https://github.com/leahmirch/Dealership-Database) - This repository documents the development process, including code commits, progress tracking, and collaboration. It serves as a central platform for code management and version control, facilitating a structured and efficient development workflow.
