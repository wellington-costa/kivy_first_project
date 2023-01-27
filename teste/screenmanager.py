from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

from core import *
from models import *


screen = ScreenManager()

class MainScreenManager(ScreenManager):
    pass


class CadProdScreen(Screen):

    def clear(self):
        self.manager.get_screen('CadProdScreen').ids.desc_product.text=""
        self.manager.get_screen('CadProdScreen').ids.marca.text = ""
        self.manager.get_screen('CadProdScreen').ids.cod_product.text = ""
        self.manager.get_screen('CadProdScreen').ids.prec_compra.text = ""
        self.manager.get_screen('CadProdScreen').ids.prec_atacado.text = ""
        self.manager.get_screen('CadProdScreen').ids.prec_varejo.text = ""
        self.manager.get_screen('CadProdScreen').ids.qtd.text = ""
        self.manager.get_screen('CadProdScreen').ids.cb.text = ""

    def register(self, descricao, marca, cod_product, qtd, prec_compra, prec_atacado, prec_varejo, cb ):
       if registerProduct(descricao, marca, cod_product, qtd, prec_compra, prec_atacado, prec_varejo, cb) == True:
          self.clear()

       else:
          self.clear()


class ListProdScreen(Screen):
    pass