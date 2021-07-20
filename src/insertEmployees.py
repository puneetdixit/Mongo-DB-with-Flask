def insert_employees_data(mongo_db_obj, request):
    """
    This function is used to insert the data into mongo db collection
    :param mongo_db_obj:
    :param request:
    :return:
    """

    employee_data = {
        "first_name": request.form.get('first_name'),
        "last_name": request.form.get('last_name'),
        "gender": request.form.get('gender'),
        "doj": request.form.get('doj'),
        "employed": request.form.get('employed')
    }
    empty_values = [key for key, value in employee_data.items() if not value]
    if empty_values:
        return {"status": "failure", "message": "parameters not provided " + str(empty_values)}
    employee_data["first_name"] = employee_data["first_name"].lower()
    employee_data["last_name"] = employee_data["last_name"].lower()
    mongo_db_obj.insert_data(employee_data)
    return {"status": "success", "desc": "Employee data inserted"}
