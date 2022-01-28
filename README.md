**I used python version 3.9.9**

Instructions on getting the app running:

Download the folder and open it in an IDE like VSCode.
We use python, flask, marshmallow and SQLAlchemy in this app. 

In the terminal, use the following commands.
Make sure python3 is installed.

create virtual enviroment and enables it and keeps all dependencies in one place.
Run command:
**$pip3 install pipenv**
**$pipenv shell **

Need to install the needed dependencies. Can be done all at once.
The below command creates a "Pipfile" and a "Pipfile.lock" file where you can check if all the dependencies are included.
Run command:
**$pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy**


If the program says importError with flask-sqlalchemy you need to select the correct version of python
**In command palette: Python: Select Interpretar
Select the correct version (usually recommended)**

You can now run the app through vscode run or using the following command in terminal:
Run command:
**$python3 app.py**

Go to your browser and type http://localhost:5000/data/create and all instructions can be found on how to test website from there


######################################################## TESTING ######################################################################

Go to the main page:
http://localhost:5000/data/create

Fill out the form with item information to be added to the database.
Price and quantity cannot be negative so if a negative value is inserted, it is displayed as positive. 

At any point, click "All Inventory" to view all the items in the database.
click "Add another item" to add more items to the database.
Click "download inventory (.csv)" to download a csv file of all the inventory. 

DELETING:
Check the id number of the item you want to delete which is displayed in "all inventory".
To delete a certain item, use http://localhost:5000/data/<idnumber>/delete. For example for id number 1, http://localhost:5000/data/1/delete.

UPDATING:
Update an item with the id number which is displayed in "all inventory"
To update a certain item, use http://localhost:5000/data/idnumber/update. For example for item 1, http://localhost:5000/data/1/update.
  
VIEWING A SINGLE ITEM:
View a single item with the id number which is displayed in "all inventory". The single item is shown in JSON format.
To view a certain item, use http://localhost:5000/data/idnumber. For example for item 1, http://localhost:5000/data/1.




