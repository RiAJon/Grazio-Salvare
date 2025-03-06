## About the Project
This project is a portable Python module that enables CRUD functionality for MongoDB, using as an example, the Austin Animal Center (AAC) database. The project was fairly straight forward and not many challenges arose during its development. However, one major bump in the road occurred during the module’s testing. At first, the database connection was unsuccessful because the environment variables were not correct in the testing script. This was a reminder of the importance of these variables and the care that needs to be taken when using MongoClient.

## Motivation
The purpose of the project is to create a tool which will help developers build a web application that connects a client-side interface to a database. This particular module was built to make it easier for users to utilize CRUD operations on the AAC database. The main class is therefore called AnimalShelter.
The module offers CREATE, READ, UPDATE, and DELETE functionality for MongoDB through a Python environment. These functions allow the user to manipulate documents in the AAC database by creating a new document, finding/reading an existing document, updating an existing document, and deleting an existing document. 

# Getting Started

## Database Schema Overview: 
The AAC database has 16 fields: 
- rec_num (number) – this field is automatically created and incremented when a document is added, you do not need to include this field in your parameter data when creating a new document
- age_upon_outcome (string)
- animal_id (string)
- animal_type (string)
- breed (string)
- color (string)
- date_of_birth (string)
- datetime (string)
- monthyear (string)
- name (string)
- outcome_subtype (string)
- outcome_type (string)
- sex_upon_outcome (string)
- location_lat (number)
- location_long (number)
- age_upon_outcome_in_weeks (number)

### How to Use the Module:
1.	To use the module, simply download the PythonCRUD.py file and place it in the same directory as your project files. Once this is done, you will need to import the AnimalShelter class into your project.

2.	From here, you will instantiate the AnimalShelter class. 

3.	Congrats, you can now use the .create(), .read(), .update(), and .delete() functions with your instance. 

 
### To create your own database instance, follow the steps below:
1.	Use your system’s command prompt or terminal to import your database using the mongoimport command and your system’s environment variables. 

2.	Next, create a new user account in the mongo shell using the authenticationDatabase (in this example it is admin).
   
4.	Now, authenticate the new account by entering the new user variables (username, password) before entering the Mongo shell. Run the connectionStatus command to ensure that the new user has the correct database privileges. 
 
5.	Finally, you will need to change the environment variables in the AnimalShelter class to match those of your system:

 
These variables will be used to initialize the database connection when you create an instance of Animal Shelter. 

### Installation
The tools needed to implement this module include a python IDE such as PyCharm, IDLE, VS Code, etc. 

-	Visual Studio Code can be downloaded for free here. 

The python driver used in this project is PyMongo.

-	PyMongo is a Python distribution containing tool for working with MongoDB and is the recommended way to work with MongoDB from Python. 

-	The PyMongo documentation can be found here. 

