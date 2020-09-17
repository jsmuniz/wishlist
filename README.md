# Customer Wishlist Api

This is a sample project of a Api to manage customer products wishlist. The Api was built using Python with Flask, Flask Restplus, SQLAlchemy and uses PostgreSQL as database

# Configuration

Following are some information about how to configure the development enviroment to run the application

## Pre-requisites

- Python 3.8.2
- Docker
- Docker Compose

## Clone or download the repository

Clone or download and extract the repository in in your machine. `cd` into the root folder of the project

## Initializing the Database

There is a docker compose file in the repository root folder that will start an PostgreSQL instance with pgAdmin4 for managing the database.

Accessing the root folder via command line, enter the command `docker-compose up`

### Connecting to PostgreSQL

After both PostgreSQL and pgAdmin4 started, access the pgAdmin4 in the following URL `https://localhost:16543`
In the login page, access using the following credentials:

- User: user@email.com
- Password: password

To connect to PostgreSQL instance, click **Add New Server**
In the General tab, fill the following fields:

- **Name**: Wishlist
  Leave the other fields as default

In the Connection tab, fill the following fields:

- **Host name/address**: postgres
- **Username**: postgres
- **Password**: password
  Leave the other fields as default

Click in **Save**

### Creating the default Database

To create the default application database, in the left panel go through Servers > Wishlist and Right Click in Databases and select Create > Database...
In the Genral tab, fill the following fields:

- **Database**: wishlist-db
  **It is essencial for the application that the database has the name wishlist-db**
  Leave the other fields as default

## Configuring the Python virtual environment

To configure the application Pyton virtual environment, go to the repository root folder via command line and enter the command:

`python3 -m venv venv`

After that, you need to activate the virtual environment, enter the following command:

`source venv/bin/activate`

## Installing required libs

Access the repository root folder via command line and enter the command:

`pip install -r requirements.txt`

Some error messages may appear in the screen, but this is expected

## Migrating the database

Access the root repository folder via command line. `cd` into src folder

Run the following command to initialize the database migration:

`python manage.py db init`

Run the following command to create the initial migration file:

`python manage.py db migrate`

Run the following command to execute the migration:

`python manage.py db upgrade`

## Running the application

Access the root repository folder via command line. `cd` into src folder
Run the following command in order to run the application:

`python app.py`

The application will start, you can access the application in the following URL:

`http://localhost:8888/api/`

If everything was successfull, you will reach a Swagger page for application and can use all api endpoints

### Authorization

All the endpoints requires an authentication token in the request header `'X-API-KEY'`
Using the application Swagger, you can click in the `Authorize` button in the UI and enter the token value for authentication

Since the application is not connected to any identity server, for demonstration purpose, it will accept requests with the following token value: `67c72716-f872-11ea-9cd5-635c896a9249`
