# Vipra-Contacts-application
Vipra technical test: A contacts application to create, View and edit contacts.

# starting the project

After cloning the project you need to do a command to start the project. To start the project you need to either use a virtual environemtn such as pycharm or Visual studio or use the terminal in order to CD to vipra_technical. 

##setting up frontend

The frontend of the project is done in React.JS and so therefore requires different setup to run. This is done by using the CD command to CD into the folder called frontend. 

Once you are in that file type npm install and it will download all the dependancies required to run the frontend.

### Runserver

To run the server after performing the above command you need to type python manage.py runserver. This will then run the server on your computer on your localhost:8000 and can then be accessed. 

# Actions

In this application you can take a few actions which work by sending requests which then change the data in the Sqlite database. 

## Add Contact

To add a contact you simply need to be logged in and navigate to the home page. Once there you can click on the top right text which says Add Contact and it will then load a form which will allow you to input the Contacts:
Name, Email, and Number.

## Update Contact

To Update your contact you need to be logged in and navigate to the Home page. There on under each contacts information there is a button which says update. Once you click that the same form for Add contacts will show up but this time you will be changing the information and on submit will push those changes.

## Delete Contact

To Delete a contact you need to navigate to the details page of the contact. Under each contacts information is a View button which will show all the information of the contact on it's own making it easier to read. In that view is also a delete button. By clicking this and then confirming your deletion it will erase the contact from the database.

