from flask import Flask, request
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://agyurifaa:najwafathiy99@cluster0.r7ne7dy.mongodb.net/?retryWrites=true&w=majority")
db = client.sicweek8
my_collections = db.assignmentweek8

@app.route('/')
def display():
	payload = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
	body = request.get_json{my_collections.find(), params = payload)
	print(r.json())

if __name__ == '__main__':
	app.run(debug==True)