from core import ConectDB, PopupScreen
import pyrebase

global db

db = ConectDB().conect()


def verify_exist_db(cb, product):
    data = db.collection(product).where('codigo_barras', '==', cb).stream()
    for doc in data:
       if(doc.id == cb):
          return doc.id


def registerProduct(data,product):

    popup = PopupScreen()
    cb = data['codigo_barras']

    try:
        if (verify_exist_db(cb, product) == cb):
            popup.showPopupScreenExist(product)
            return False

        else:
                ref = db.collection(product).document(cb)
                ref.set(data)
                popup.showPopupScreenSuccess(product)
                return True


    except Exception as error:
       print(error)
       return  False

def getProducts():
    listdata = []
    ref1 = db.collection('alimento').stream()
    ref2 = db.collection('bebida').stream()
    ref3 = db.collection('outros').stream()

    for doc in ref1:
        data = doc.to_dict()
        listdata.append(data)


    for doc in ref2:
        data = doc.to_dict()
        listdata.append(data)


    for doc in ref3:
        data = doc.to_dict()
        listdata.append(data)

    return listdata

