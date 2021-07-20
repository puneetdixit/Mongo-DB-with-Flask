import json

import pandas as pd
from IPython.display import HTML
from pymongo import MongoClient

import settings
from src.utils import JSONEncoder


class MongoDBManager(object):
    def __init__(self, database_name, collection_name):
        self.db_connection = None
        self.collection = None
        self.create_connection()
        self.select_or_create_collection(database_name, collection_name)

    def create_connection(self):
        """
        This function is used to create a connection with mongodb server.
        """
        try:
            self.db_connection = MongoClient(host=settings.MONGO_DB_IP, port=settings.MONGO_DB_PORT)
            print("*** Connection established with MongoDB ***")
        except Exception as e:
            raise Exception("Could not connect to MongoDB: ", e)

    def select_or_create_collection(self, database, collection):
        """
        This function is used to select a collection from a particular data. If collection is not present then it will
        create.
        :param database:
        :param collection:
        """
        db = self.db_connection[database]
        self.collection = db[collection]

    def insert_data(self, data):
        """
        This function is used to add employee data to the mongoDb database
        :param data:
        """
        self.collection.insert_one(data)

    def get_all_data(self, search_name=None):
        """
        This function is used to get all employees data. If there is some value in search_name then it will apply
        filter on first_name and last_name.
        :param search_name:
        :return all_data:
        """
        all_data = []
        if search_name:
            search_in_lower = search_name.lower()
            cursor = self.collection.find({"$or": [{"first_name": search_in_lower}, {"last_name": search_in_lower}]})
        else:
            cursor = self.collection.find()
        for record in cursor:
            record['_id'] = json.dumps(record['_id'], cls=JSONEncoder)
            record['first_name'] = record['first_name'].capitalize()
            record['last_name'] = record['last_name'].capitalize()
            all_data.append(record)
        
        if all_data:
            df = pd.DataFrame(all_data)
            df['Name'] = df['first_name'].str.cat(df['last_name'], sep=" ")
            del df['first_name']
            del df['last_name']
            del df['_id']
            df = df.rename(columns={'doj': 'Doj', 'employed': 'Employed', 'gender': 'Gender'})
            columns_order = ['Name', 'Gender', 'Doj', 'Employed']
            new_columns = columns_order + (df.columns.drop(columns_order).tolist())
            df = df[new_columns]
            return HTML(df.to_html(classes='table table-striped', table_id="employeeTable", index=False))
        elif search_name:
            return 'No results found for: "{}"'.format(search_name)
        else:
            return "Data not present in the selected database or collection"

    def delete_document(self, key, value):
        """
        This function is used to delete a document:
        :param key:
        :param value:
        """
        query = {key: value}
        self.collection.delete_one(query)
