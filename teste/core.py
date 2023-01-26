import pyrebase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import Label



class ConectDB():
  def conect(self):
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
    return db


class PopupScreen():
  def showPopupScreen(self, objetc):
    box = BoxLayout(orientation='vertical', padding=10)
    pop = Popup(title='Sucesso!', content=box, size_hint=(None, None), size=(300, 180))
    label = Label(text=str(objetc + ' Cadastrado com sucesso!'))
    btn = MDRaisedButton(text='ok', on_release=pop.dismiss, pos_hint={'center_x': .5})
    box.add_widget(label)
    box.add_widget(btn)
    pop.open()
