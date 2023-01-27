from core import *
import pyrebase

global db

db = ConectDB().conect()


def verify_exist_db(cb, table):
    data = db.collection('produto').where('codigo_barras', '==', cb).stream()
    for doc in data:

       if(doc.id == cb):
           print(doc.id, cb)


def registerProduct(descricao, marca, cod_product, qtd, prec_compra, prec_atacado, prec_varejo, cb):
    product_str = "produto"
    popup = PopupScreen()
    product = {
        'descricao': descricao,
        'marca': marca,
        'codigo': cod_product,
        'valor_compra' : prec_compra,
        'valor_atacado': prec_atacado,
        'valor_varejo': prec_varejo,
        'quantidade': qtd,
        'codigo_barras': cb
    }
    try:
        if (verify_exist_db(cb, product_str) == True):
            popup.showPopupScreenExist(product_str)
            return False

        else:
            if (verify_exist_db(cb,product_str)==False):
                ref = db.collection(product_str).document(cb)
                ref.set(product)
                popup.showPopupScreenSuccess(product_str)
                return True


    except Exception as error:
       print(error)
       return  False

def getProducts():
    pass

