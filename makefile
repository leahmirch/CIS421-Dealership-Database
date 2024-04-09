# Variables
DB_FILE=dealership.db
VENV=venv

mac:
	@echo "Setting up the Dealership Database application..."
	@if [ -f $(DB_FILE) ]; then echo "Deleting existing database file..."; rm $(DB_FILE); fi
	@echo "Setting up the database..."
	python3 setup_database.py
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV)
	@echo "Activating virtual environment and installing Flask..."
	. $(VENV)/bin/activate && pip install flask
	@echo "Running Flask application..."
	. $(VENV)/bin/activate && python3 user_interface.py

windows:
	@echo Setting up the Dealership Database application...
	@if exist $(DB_FILE) (echo Deleting existing database file... & del $(DB_FILE))
	@echo Setting up the database...
	python setup_database.py
	@echo Creating virtual environment...
	python -m venv $(VENV)
	@echo Activating virtual environment and installing Flask...
	$(VENV)\Scripts\activate.bat && pip install flask
	@echo Running Flask application...
	start cmd /k "$(VENV)\Scripts\activate.bat && python user_interface.py"
