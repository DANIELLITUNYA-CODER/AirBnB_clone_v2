# AirBnB Clone (v2)

This is the continuation of the AirBnB clone project, with a focus on transitioning from FileStorage to DBStorage using SQLAlchemy.

## Overview

The AirBnB clone project is a web application that allows users to list, search, and book short-term lodging. This version (v2) of the project introduces a new storage engine, DBStorage, which uses a MySQL database to store the application data.

## Key Features

1. **Storage Engine Abstraction**: The project uses an abstract storage engine interface, allowing the application to seamlessly switch between different storage backends (FileStorage and DBStorage) without affecting the core functionality.

2. **SQLAlchemy Integration**: The DBStorage engine is implemented using SQLAlchemy, a Python SQL toolkit and Object-Relational Mapper (ORM). This allows for efficient database interactions and management of the application's data models.

3. **MySQL Integration**: The DBStorage engine is configured to use a MySQL database as the underlying storage solution. Environment variables are used to manage the connection details, making the application more portable and easier to deploy.

4. **Improved Test Coverage**: The project includes comprehensive unit tests for the new DBStorage engine, ensuring the reliability and correctness of the application's data management functionality.

5. **Console Enhancements**: The command-line interface (console) has been updated to support the creation of objects with specified parameters, improving the overall user experience.

## Directory Structure

```
AirBnB_clone_v2/
├── console.py
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── city.py
│   ├── db_storage.py
│   ├── engine/
│   │   ├── __init__.py
│   │   ├── db_storage.py
│   │   └── file_storage.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── setup_mysql_dev.sql
├── setup_mysql_test.sql
└── tests/
    ├── __init__.py
    └── test_models/
        ├── __init__.py
        ├── test_city.py
        ├── test_engine/
        │   ├── __init__.py
        │   └── test_db_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py
```

## Usage

To use the AirBnB clone application, follow these steps:

1. Set up the MySQL development and test databases using the provided SQL scripts (`setup_mysql_dev.sql` and `setup_mysql_test.sql`).
2. Run the application's command-line interface (console) using the appropriate environment variables to specify the storage engine and database connection details:

```
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

3. Explore the available commands and functionality, including creating, retrieving, updating, and deleting objects in the database.

## Testing

The project includes a comprehensive test suite to ensure the correctness of the application's functionality. To run the tests, use the following command:

```
HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests
```

## Contributors

- DANIEL LITUNYA.
