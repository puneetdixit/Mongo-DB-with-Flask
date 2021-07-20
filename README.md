Prerequisites - MongoDB server, Python3.9
    If you want to use your local mongodb server then install it in your system.
        For ubuntu systems - https://linuxize.com/post/how-to-install-mongodb-on-ubuntu-18-04/
        For Windows systems - https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
    
    Python3.9
        For ubuntu systems - https://phoenixnap.com/kb/how-to-install-python-3-ubuntu
        For windows systems - https://docs.python.org/3/using/windows.html


Step 1. Create a virtual environment for this project.
    Run these commands on your shell.
    If virtualenv not installed in your system then go through this link 
    https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

    -> python3.9 -m venv venv_name
    -> source venv_name/bin/activate

Step 2. Go to your code path.
    Run this command on your shell.
    -> pip3 install -r requirements.txt

Step 3. Modify variables in settings.py file
    1.  SERVER_PORT is the port of your system on which your server will run. Modify the value of SERVER_PORT = 5000, 
        Provide the value of port on which you want to run your server. 
        By default, your server will run on port 5000

    2.  MONGO_DB_IP and MONGO_DB_PORT is the ipaddress and port on which your mongodb server is running.
        If you are using local hosted mongodb server then do not change the variables

    3.  MONGO_DB_DATABASE and MONGO_DB_COLLECTION add your database name collection name on which you want to store your
        employee data.
        If database or collection not present in your mongo db server then it will auto create it.

Step 4. Run your server.
    Run these commands on your shell.

    -> python app.py
    If you run your server using this command then it will run on the port which you set in settings.py file

    or

    -> flask run --host 0.0.0.0 --port 5000
    If you want to change your port on run time then you can change it here. Provide the --port value

Step 5. To check your server is working go to http://127.0.0.1:5000/ or localhost:5000 it will return 
    {
        "message": "Server is running"
    }

Step 6. Add employee in your database.
    - Go to http://127.0.0.1:5000/insertEmployees in your browser, fill the form and click on Add Employee button. 
      It will submit your data in mongodb.
    - You can view your all employee data by clicking on View All Employee button.

Step 7. View employee
    - Go to http://127.0.0.1:5000/viewEmployees in your browser, it will show a table with employee details.
    - You can search your employee by name or by surname, enter employee name or surname and click on search. It will 
      display the filtered result
    - You can add new employee by clicking on Add New Employee button.
