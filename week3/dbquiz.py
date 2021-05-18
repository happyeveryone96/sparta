from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

matrix = db.movies.find_one({'title':'매트릭스'})
print(matrix['point'])

same_point = list(db.movies.find({'point':'9.39'},{'_id':False}))

for point in same_point:
    print(point['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'point': '0'}})