# Grazio Salvare Interface
<video autoplay loop muted playsinline>
  <source src="/usage" type="video/mp4">
</video>

## CRUD Module 
This project uses a portable Python module that enables CRUD functionality for MongoDB, using as an example, the Austin Animal Center (AAC) database. The purpose of the module is to help developers build web applications that connect a client-side interface to a database. This particular module was built to make it easier for users to utilize CRUD operations on the AAC database. The main class is therefore called AnimalShelter.
The module offers CREATE, READ, UPDATE, and DELETE functionality for MongoDB through a Python environment. These functions allow the user to manipulate documents in the AAC database by creating a new document, finding/reading an existing document, updating an existing document, and deleting an existing document. 

# Getting Started

### Example Database Schema Overview: 
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

## How to Use the Module:
1.	To use the module, simply download the PythonCRUD.py file and place it in the same directory as your project files. Once this is done, you will need to import the AnimalShelter class into your project.

![image](https://github.com/user-attachments/assets/7502b7f8-d5ca-4b03-b68e-293ce6a26eed)

2.	From here, you will instantiate the AnimalShelter class.
   
![image](https://github.com/user-attachments/assets/d5ea4f6d-ce10-42ba-808e-71713a97b310)

3.	Congrats, you can now use the .create(), .read(), .update(), and .delete() functions with your instance.
   
![image](https://github.com/user-attachments/assets/1c84c4c8-c1e0-444e-ba8e-6e9b2b0e2a03)
 
### To create your own database instance, follow the steps below:
1.	Use your system’s command prompt or terminal to import your database using the mongoimport command and your system’s environment variables.
   
![image](https://github.com/user-attachments/assets/061a83a3-0532-44bb-8f78-942833117dd5)

3.	Next, create a new user account in the mongo shell using the authenticationDatabase (in this example it is admin).
   
![image](https://github.com/user-attachments/assets/b998f2f7-8a3c-4c71-bbe5-1a349c130a74)

5.	Now, authenticate the new account by entering the new user variables (username, password) before entering the Mongo shell. Run the connectionStatus command to ensure that the new user has the correct database privileges.
   
![image](https://github.com/user-attachments/assets/dfb0faf0-6539-4271-b546-95948882e61e)

7.	Finally, you will need to change the environment variables in the AnimalShelter class to match those of your system:
   
![image](https://github.com/user-attachments/assets/a01327b6-d73a-4f99-afcd-41743a243338)

These variables will be used to initialize the database connection when you create an instance of Animal Shelter. 

### Installation
The tools needed to implement this module include a python IDE such as PyCharm, IDLE, VS Code, etc. 
-	Visual Studio Code can be downloaded for free **[here](https://code.visualstudio.com/)**. 

The python driver used in this project is PyMongo.
-	PyMongo is a Python distribution containing tool for working with MongoDB and is the recommended way to work with MongoDB from Python. 
-	The PyMongo documentation can be found **[here](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)**. 

