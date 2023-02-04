import json

from pyrebase import pyrebase
import models
import firebase_admin
from firebase_admin import credentials, firestore

data = models.getProducts()

for produto in data:
    print(produto['marca'])







'''
tipos = ['bebida','alimento','outros']

for i in tipos:
    print(i)




cred = credentials.Certificate("mercadinho-9b7ce-firebase-adminsdk-8f95a-7e18e53ebd.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
listdata=[]
listkeys=[]
ref1 = db.collection('alimento').stream()
ref2 = db.collection('bebida').stream()
ref3 = db.collection('outros').stream()
#ref2 = db.collection('produto').document('cod_2')
for doc in ref1:
    data =  doc.to_dict()
    listdata.append(data)
    listkeys.append(doc.id)

for doc in ref2:
    data = doc.to_dict()
    listdata.append(data)
    listkeys.append(doc.id)

for doc in ref3:
    data = doc.to_dict()
    listdata.append(data)
    listkeys.append(doc.id)
keys=[]
for i in listdata:
    print(i['marca'])


print(keys)
s=0
for j in listkeys:
   print(j)


list=[]
for doc in ref:
    #print('{}=>{}'.format(doc.id, doc.to_dict()))
    data = {doc.id : doc.to_dict()}
    list.append(data)


for i in list:
    print(i)


#print(list[0]['cod_1']['marca'])

'''




'''
    firebaseConfig = {
      'apiKey': "AIzaSyCbylYBXVRCsDb5L0crIKL-_H33iP1x6lM",
      'authDomain': "mercadinho-9b7ce.firebaseapp.com",
      'databaseURL': "https://mercadinho-9b7ce-default-rtdb.firebaseio.com",
      'projectId': "mercadinho-9b7ce",
      'storageBucket': "mercadinho-9b7ce.appspot.com",
      'messagingSenderId': "622806799570",
      'appId': "1:622806799570:web:3544901a94fb95edff090b",
      'measurementId': "G-ZJSXVJTFBR"
    };

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

produtos = db.child('produto').get()

for produto in produtos.each():
    print(produto.val())

    with open("produtos.json", "w") as arq:
     json.dumps(produto, arq, indent=4)
'''


'''  
    firebaseConfig = {
      'apiKey': "AIzaSyCbylYBXVRCsDb5L0crIKL-_H33iP1x6lM",
      'authDomain': "mercadinho-9b7ce.firebaseapp.com",
      'databaseURL': "https://mercadinho-9b7ce-default-rtdb.firebaseio.com",
      'projectId': "mercadinho-9b7ce",
      'storageBucket': "mercadinho-9b7ce.appspot.com",
      'messagingSenderId': "622806799570",
      'appId': "1:622806799570:web:3544901a94fb95edff090b",
      'measurementId': "G-ZJSXVJTFBR"
    };

    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
'''