<img src="https://i.ibb.co/nrdvBys/task-manager-cover-picture.jpg" width="100%">


<div align="center">
<h1>Task Management Application</h1>
A Python-Django Task Management Web Application with REST API
<br>
<br>

<h3>-----Project's Short Video link-----</h3>
Google Drive : https://drive.google.com/drive/folders/1-ga2R4OTHDakaBnaJWgr7QxILlwmdjWU?usp=sharing
<br>
or
<br>
Youtube : https://www.youtube.com/playlist?list=PLmkOy5VTucIUSR2ig_n-PoGmO4fyhBAyD

</div>

<br>

## Technology Used --------

-   **Frontend:** HTML5, CSS3, Bootstrap5
-   **Backend:** Python=3.11.4, Django=4.2.5
-   **Database:** PostgreSQL
-   **Important Lib:** djangorestframework==3.14.0, psycopg2==2.9.9, python-dotenv==1.0.0, Pillow==10.1.0
-   **API:** Django-REST-Framework

<br>

## How to Run This Project Step by step --------


### Clone from GitHub

-   Clone the repository

```bash
git clone https://github.com/samimosmansabuj/task-management-web-application-project.git
```

-   Go to the project directory

```bash
cd task-manager
```

-   Create a virtual environment

```bash
python -m venv venv
```

-   Activate the virtual environment

```bash
source venv/Scripts/activate
```

-   Install the dependencies or Lib

```bash
pip install -r requirements.txt
```

-   Run the server

```bash
python manage.py runserver
```

-   Open the browser and go to http://127.0.0.1:8000/


<br>

### Setup PostgreSQL Database

-   Install PostgreSQL

```bash
pip install psycopg2
```

-   Login to PostgreSQL

-   Create a database

-   Create a user

-   Grant privileges to the user

-   Exit from PostgreSQL


<br>

### Create environment variables & Config settings.py

-   Open the `settings.py` file from `task_manager` directory

-   Create a file named `.env` in the `task_manager` directory and add the following lines

```bash
SECRET_KEY=your_secret_key
DEBUG=False

#Email BackEND (For Send Mail, Forget Password Etc.) - Optional---------***
EMAIL_HOST_USER = EMAIL  #must enter your email
EMAIL_HOST_PASSWORD = EMAIL_APP_PASSWORD   #must enter your email app password

#Database Config-----------------***
DB_NAME=Database_Name
DB_USER=Database_USER
DB_PASSWORD=Database_PASSWORD
DB_HOST=Database_HOST
DB_PORT=Database_PORT
```

See the `.env.example` file for reference.

<br>

### Import Data from database.json

-   You will find a file named `database.json` in the root directory


-   Migrate Database

```bash
python manage.py make migrations
```

```bash
python manage.py migrate
```


-   Run the following command to import data from `database.json`

```bash
python manage.py loaddata database.json
```
<br>

### Admin Panel --------

-   Run the server

```bash
python manage.py runserver
```

-   Open the browser and go to http://127.0.0.1:8000/admin/ for access the admin panel

-   Login with the following credentials:

    -   Username: `admin`
    -   Password: `admin`

-   If these credentials don't work, you can create a superuser by running the following command:

```bash
python manage.py createsuperuser
```

-   Enter the username, email, and password

-   Now you can access the admin panel with the credentials you have just created

<br>

## API Details --------

-   **Endpoint:** http://127.0.0.1:8000/task-api-view/
-   **Method:** GET, POST
-   **Description:**
    -   Returns all the tasks
-   **Endpoint:** http://127.0.0.1:8000/task-api-view/9/
-   **Method:** GET, PUT, PATCH, DELETE
-   **Description:**
    -   Returns a single task
    -   Updates a single task
    -   Partially updates a single task
    -   Deletes a single task


<br>

### Regular User, Employee & Admin --------

-   Regular User Credentials:
    -   Username: `samimregular`
    -   Password: `samimregular`


-   Employee Credentials:
    -   Username: `samimemployee`
    -   Password: `samimemployee`


-   Employee Credentials:
    -   Username: `samimadmin`
    -   Password: `samimadmin`



