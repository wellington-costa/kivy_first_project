import json

from pyrebase import pyrebase

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