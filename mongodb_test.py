from pymongo import MongoClient
import pandas as pd

# connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['mydb']
collection = db['users']

# load CSV file into Pandas dataframe
df = pd.read_csv('notebook/data/stud.csv')

# convert dataframe to dictionary
data_dict = df.to_dict('records')

# insert data into MongoDB collection
collection.insert_many(data_dict)

# read data from MongoDB collection
cursor = collection.find()
for document in cursor:
    print(document)
