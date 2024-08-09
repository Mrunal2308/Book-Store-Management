# Book Store Management

Book Store Management is a comprehensive Django-based web application designed to facilitate the management of book and author information. It provides an intuitive and user-friendly interface for users to interact with a database of books and authors, manage user accounts, and perform various operations related to book management.

## Project Description

### Overview

The Book Store Management application is built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design. The project focuses on creating a robust and scalable system to manage a catalog of books and their authors. The application includes essential features for user authentication and CRUD (Create, Read, Update, Delete) operations on book and author records.

### Features

1. **User Authentication**:
   - **Sign Up**: Users can create a new account by providing necessary details such as username, email, and password. This process includes validation to ensure data integrity and security.
   - **Login**: Registered users can log in to the system using their credentials. The login mechanism uses secure authentication methods to protect user data.
   - **Logout**: Users can log out of their accounts, ending their session and ensuring their account remains secure.

2. **Book Management**:
   - **Add Books**: Users can add new books to the system by providing details such as the book title, author, publication date, genre, and any other relevant information. This feature helps in building and 
                    expanding the book inventory.
   - **Edit Books**: Existing book records can be updated to reflect changes in book details. This functionality is crucial for maintaining accurate and current information in the database.
   - **Delete Books**: Books that are no longer relevant or needed can be removed from the system, ensuring that the database remains clean and up-to-date.

3. **Author Management**:
   - **Add Authors**: Users can add new authors, including details such as the author's name, biography, and contact information. This feature allows for comprehensive author profiles within the system.
   - **Edit Authors**: Users can update existing author details as needed. This ensures that author profiles remain accurate and complete.
   - **Delete Authors**: Authors can be removed from the system if they are no longer associated with any books or if their information is outdated.

4. **Database Integration**:
   - **MySQL Database**: The application uses a MySQL database to store all data, including user credentials, book records, and author information. This integration ensures efficient data management and 
                         retrieval.

- **Framework**: Django 4.x
- **Database**: MySQL 8.x
- **Programming Language**: Python 3.x

### User Interface

The application features a clean and intuitive user interface, designed to make interactions with the system straightforward. Users can navigate between different sections, manage their accounts, and perform book and author-related operations with ease.



## Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

Clone the repository to your local machine using the following command:
git clone https://github.com/Mrunal2308/Book-Store-Management.git



### 2. Navigate to the Project Directory

Once the repository is cloned, navigate to the project directory:
cd Book-Store-Management


### 3. Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies:
python -m venv env

**Activate the virtual environment:**
- **On Windows:**
  .\env\Scripts\activate

- **On macOS/Linux:**
 source env/bin/activate



### 4. Install Dependencies

With the virtual environment activated, install the project dependencies:
pip install -r requirements.txt






### Configuration:

### 1. Set Up the MySQL Database
Ensure that you have MySQL installed and running on your local machine. Create a database named `bookdb` (or another name of your choice):
CREATE DATABASE bookdb;



### 2. Modify the `settings.py` File

Open the `settings.py` file located in the `Book-Store-Management/book_store_management/` directory and update the `DATABASES` configuration with your local MySQL credentials:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookdb',  # Update if you used a different database name
        'PORT': '3306',
        'HOST': 'localhost',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password'
    }
}
Replace `your_mysql_username` and `your_mysql_password` with your actual MySQL credentials.



### 3. Apply Migrations

Apply the database migrations to set up the necessary tables:
python manage.py migrate


### Running the Application

To run the Django development server, use the following command:
python manage.py runserver

This will start the server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/), where you can access the Book Store Management application.


### Usage

- **Sign Up**: Create a new user account by providing necessary details such as username, email, and password.

- **Login**: Log in using your credentials to access the management features.
  
- **Manage Books and Authors**:
  
  - **Add Books**: Provide details like the book title, author, publication date, and genre.
    
  - **Edit Books**: Modify details of existing books.
    
  - **Delete Books**: Remove books from the database.
    
  - **Add Authors**: Enter details such as the author's name, biography, and contact information.
    
  - **Edit Authors**: Update information for existing authors.
    
  - **Delete Authors**: Remove authors if necessary.








