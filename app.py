from flask import Flask, request, render_template

import settings
from src.insertEmployees import insert_employees_data
from src.mongo_db_manager import MongoDBManager

mongodb = MongoDBManager(settings.MONGO_DB_DATABASE, settings.MONGO_DB_COLLECTION)

app = Flask(__name__)


@app.route('/')
def index():
    return {"message": "Server is running"}


@app.route('/insertEmployees', methods=['POST', 'GET'])
def insert_employee():
    """
    This function is used as a insertEmployee view. If you want to get the insert form the call this api with GET
    method it will render a template to fill the form and if you want to insert the data the call this api with POST
    method.
    """
    if request.method == 'POST':
        return insert_employees_data(mongodb, request)
    return render_template("insertEmployee.html")


@app.route('/viewEmployees', methods=['GET'])
def get_all_employees():
    """
    This function is used as a viewEmployees view. Only GET method is allowed.
    """
    search = request.args.get('searchName')
    data = mongodb.get_all_data(search)
    if not search:
        search = ''
    return render_template('viewEmployees.html', table=data, search=search)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=settings.SERVER_PORT, debug=False)
