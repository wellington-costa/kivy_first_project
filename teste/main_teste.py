import os

from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from models import *
from kaki.app import App





class ShowProductsScreen(Screen):
    pass



class TesteApp(MDApp, App):
    DEBUG = 1  # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "screenmanager.kv"),
        os.path.join(os.getcwd(), "login.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "screenmanager",
        "LoginScreen": "login",

    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        return Factory.MainScreenManager()



TesteApp().run()