from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import ThreeLineListItem

from core import *
from models import *


screen = ScreenManager()

class MainScreenManager(ScreenManager):
    pass

class DashboardScreen(Screen):
   pass

class VendasScreen(Screen):

    def loadListItems(self,list):
        widget = self.children[1].children[0].children[0]
        self.remove_widget(widget)
        for produto in list:
            primary = produto['descricao']
            secondary = produto['marca']
            self.manager.get_screen("vendas").ids.produto_venda.add_widget(
                ThreeLineListItem(text=primary, secondary_text=secondary))

    def filterText(self, text):
        data = getProducts()
        list = []
        if len(data) > 0:
            #tela = self.manager.get_screen("vendas").ids.produto_venda

            for produto in data:
                if text in produto['descricao'] or text in produto['marca'] or text in produto['codigo_barras']:
                    list.append(produto)

            self.loadListItems(list)
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
        primary = produto['descricao'] + "| Marca: "+ produto['marca']
        secondary = "Varejo R$ "+ produto['valor_varejo'] + "| Atacado R$ "+ produto['valor_atacado']
        tertiary = "Qtd= "+ produto['quantidade'] + "| Tipo: "+ produto['tipo']
        self.manager.get_screen("ListProdScreen").ids.produto.add_widget(ThreeLineListItem(text= primary, secondary_text=secondary,tertiary_text=tertiary))
