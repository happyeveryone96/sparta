from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert / find / update / delete

#doc = {'name':'jane','age':40}
#db.users.insert_one(doc) #db안에 users라는 collection에 insert해라

# same_ages = list(db.users.find({},{'_id':False}))
#                             # 다 가져와라 / _id 값은 보여주지 말아라
#
# for person in same_ages:
#     print(person)

#user = db.users.find_one({'name':'bobby'}) #bobby를 하나만 찾아서 가져옴
#print(user)

#db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#db.users.update_many({'name':'bobby'},{'$set':{'age':19}})
#name이 bobby인 값들을 모두 찾아서 age를 19로 변경

#db.users.delete_one({'name':'bobby'})

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})