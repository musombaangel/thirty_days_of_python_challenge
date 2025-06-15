from flask import Flask
from pymongo.mongo_client import MongoClient
import os
import dotenv

load_env=dotenv.load_dotenv
# Load environment variables from .env file
load_env()

mongodb_uri=os.getenv("mongodb_uri")
client=MongoClient(mongodb_uri)
print(client.list_database_names())    #print all database names
print("uri",mongodb_uri)

db=client.student   #create database called student
student_collection=db.students  #create collection named students

#inserting one
student_collection.insert_one({'name': 'Angel', 'number': 134})

#inserting many
student_collection.insert_many([
    {'name': 'John', 'number': 135},
    {'name': 'Jane', 'number': 136},
    {'name': 'Doe', 'number': 137}
])

query={'name':'Jane'}  #query to find students with name Jane
students=student_collection.find(query) #finding the documents that match the query
for student in students:
    print(student)

#updating a document
query={'name':'Angel'}
new_values={'$set': {'name': 'Angel Musomba'},
                '$inc': {'number': 1}}  #incrementing the number by 1
student_collection.update_one(query, new_values)

#deleting a document
query={'name': 'Doe'}
student_collection.delete_one(query)

#deleting the entire collection
student_collection.drop()


app=Flask(__name__)

@app.route('/')
def home():
    return "Mongo DB implementation with Flask"

if __name__=="__main__":
    port=os.environ.get("PORT", 3000)
    app.run(debug=True, host='0.0.0.0', port=port)