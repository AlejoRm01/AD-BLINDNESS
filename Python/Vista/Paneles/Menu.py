import sys
from UI.UI_Menu import *
from Utiles.DB_Driver import agregarUs, getUsuario
from Utiles.Correo import enviarCorreo

class Menu():

    def __init__(self):
        self.UIm = UI_menu()

    def show(self):
        self.UIm.show()
        
    def close(self):
        self.UIm.close()