import sys 
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from Paneles.Login import Login
from Paneles.SignUp import SignUp
#from Paneles.Menu import Menu

"""
Clase Main
Encargada de llamara a las demas clases, ponerlas en ejecucion, y administrar datos entre ellas.
"""
class Controlador:

    def __init__(self):
        pass
    
    def show_Ingreso(self):
        self.login = Login()
        self.login.UIl.switch_Registro.connect(self.show_Registro)
        #self.login.UIl.switch_Menu.connect(self.show_Menu)
        self.login.show()
    

    def show_Registro(self):
        self.SignUp = SignUp()
        self.SignUp.UIs.switch_Login.connect(self.show_Ingreso)
        self.login.close()
        self.SignUp.show()

'''        
    def show_Menu(self):
        self.Menu = Menu()
        self.compra.UIm.switch_Inventario.connect(self.show_Inventario)
        self.compra.UIm.switch_Venta.connect(self.show_Venta)
        self.compra.UIm.switch_Usuario.connect(self.show_Usuario)
        self.compra.show()
'''        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    controlador = Controlador()
    controlador.show_Ingreso()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
