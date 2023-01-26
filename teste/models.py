from core import *
import pyrebase

global db

db = ConectDB().conect()

def registerProduct(descricao, marca, cod_product, qtd, prec_compra, prec_atacado, prec_varejo, cb):

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
       db.child('produto').push(product)
       produto = 'Produto'
       PopupScreen().showPopupScreen(produto)
       return True

    except Exception as error:
       print(error)
       return  False

def getProducts():
    pass
