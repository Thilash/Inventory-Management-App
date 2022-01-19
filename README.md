# Shopify-Backend-Developer-Intern-Summer-2022-
Submission for Shopify backend developer intern challenge for summer 2022
**I used python version 3.9.9**

Instructions on getting the app running:

Download the folder and open it in an IDE like VSCode.
We use python, flask, marshmallow and SQLAlchemy in this app. 

In the terminal, use the following commands.
Make sure python3 is installed.

create virtual enviroment and enables it and keeps all dependencies in one place.
Run command:
**$pip3 install pipenv
$pipenv shell **

Need to install the needed dependencies. Can be done all at once.
Run command:
**$pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy**

If the program says importError with flask-sqlalchemy you need to select the correct version of python
**In command palette: Python: Select Interpretar
Select the correct version (usually recommended)**

You can now run the app through vscode run or using the following command in terminal:
Run command:
**$python3 app.py**

Go to your browser and type http://localhost:5000/data/create and all instructions can be found on how to test website from there
