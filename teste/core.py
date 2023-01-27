import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import Label



class ConectDB():
  def conect(self):


     cred = credentials.Certificate("mercadinho-9b7ce-firebase-adminsdk-8f95a-7e18e53ebd.json")
     firebase_admin.initialize_app(cred)

     db = firestore.client()
     return db






class PopupScreen():
  def showPopupScreenSuccess(self, objetc):
    box = BoxLayout(orientation='vertical', padding=10)
    pop = Popup(title='Sucesso!', content=box, size_hint=(None, None), size=(300, 180))
    label = Label(text=str(objetc + ' Cadastrado com sucesso!'))
    btn = MDRaisedButton(text='ok', on_release=pop.dismiss, pos_hint={'center_x': .5})
    box.add_widget(label)
    box.add_widget(btn)
    pop.open()
  def showPopupScreenExist(self, object):
      box = BoxLayout(orientation='vertical', padding=10)
      pop = Popup(title='ERRO!', content=box, size_hint=(None, None), size=(300, 180))
      label = Label(text=str(object + ' Já está cadastrado!'))
      btn = MDRaisedButton(text='ok', on_release=pop.dismiss, pos_hint={'center_x': .5})
      box.add_widget(label)
      box.add_widget(btn)
      pop.open()
