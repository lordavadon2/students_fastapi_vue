from pymongo import MongoClient

client = MongoClient('mongodb+srv://<username>:<password>@mongo-cluster.nefny.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')


db = client["cruddb"]
student_collection = db["students"]
