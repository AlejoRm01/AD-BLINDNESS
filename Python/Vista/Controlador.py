import sys, subprocess
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Paneles.Login import Login
from Paneles.SignUp import SignUp
from Paneles.Menu import Menu 


"""
Clase Main
Encargada de llamara a las demas clases, ponerlas en ejecucion, y administrar datos entre ellas.
"""
class Controlador:

    def __init__(self):
        self.login = Login()
        self.SignUp = SignUp()
        self.Menu = Menu()
    
    def show_Ingreso(self):
        self.login.UIl.switch_Registro.connect(self.show_Registro)
        self.login.UIl.switch_Menu.connect(self.show_Menu)
        self.login.show()
        self.SignUp.close()
    

    def show_Registro(self):
        self.SignUp.UIs.switch_Login.connect(self.show_Ingreso)
        self.SignUp.show()

    def show_Menu(self):
        self.Menu.UIm.switch_camara.connect(self.show_Camara)
        self.Menu.show()
        self.login.close()
    
    def show_Camara(self):
        exec(open('prueba_colors.py').read())
   
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    controlador = Controlador()
    controlador.show_Ingreso()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
