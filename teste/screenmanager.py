from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import ThreeLineListItem

from core import *
from models import *


screen = ScreenManager()

class MainScreenManager(ScreenManager):
    pass


class CadProdScreen(Screen):

    def clear(self):
        self.manager.get_screen('CadProdScreen').ids.desc_product.text=""
        self.manager.get_screen('CadProdScreen').ids.marca.text = ""
        self.manager.get_screen('CadProdScreen').ids.tipo_product.text = ""
        self.manager.get_screen('CadProdScreen').ids.prec_compra.text = ""
        self.manager.get_screen('CadProdScreen').ids.prec_atacado.text = ""
        self.manager.get_screen('CadProdScreen').ids.prec_varejo.text = ""
        self.manager.get_screen('CadProdScreen').ids.qtd.text = ""
        self.manager.get_screen('CadProdScreen').ids.cb.text = ""

    def register(self, descricao, marca, tipo_product, qtd, prec_compra, prec_atacado, prec_varejo, cb ):
        tipo_product= tipo_product.lower()

        data = {
            'descricao': descricao,
            'marca': marca,
            'tipo': tipo_product,
            'valor_compra': prec_compra,
            'valor_atacado': prec_atacado,
            'valor_varejo': prec_varejo,
            'quantidade': qtd,
            'codigo_barras': cb
        }


        if verifyLabels(data) == True:
            registerProduct(data,tipo_product)
            self.clear()

        else:
          self.clear()


class ListProdScreen(Screen):
    def showData(self):
      self.manager.get_screen('ListProdScreen').ids.produto.clear_widgets()
      data = getProducts()
      for produto in data:
        primary = str(produto['descricao'])+ "| Marca: "+ str(produto['marca'])
        secondary = "Varejo R$ "+str(produto['valor_varejo'])+ "| Atacado R$ "+ str(produto['valor_atacado'])
        tertiary = "Qtd= "+str(produto['quantidade'])+ "| Tipo: "+ str(produto['tipo'])
        self.manager.get_screen("ListProdScreen").ids.produto.add_widget(ThreeLineListItem(text= primary, secondary_text = secondary, tertiary_text = tertiary))