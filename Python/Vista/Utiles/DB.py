import csv, os


class tabla_Usuarios():
    
    def __init__(self):
        self.DB = 'DB.csv'
        self.ESQUEMA_LLAVES = ['User', 'Pass']
        self.dicc = [] 

    def inicializar_tabla(self):
        
        with open(self.DB, 'r') as f:
            lector = csv.DictReader(f, fieldnames=self.ESQUEMA_LLAVES)
            
            for row in lector:
                self.dicc.append(row)
            

    def guardar_llaves(self):

        tmp_DB = '{}.tmp'.format(self.DB)
        with open(tmp_DB, mode='w') as f:
            escritor = csv.DictWriter(f, fieldnames=self.ESQUEMA_LLAVES)
            escritor.writerows(self.dicc)
            os.remove(self.DB)
        os.rename(tmp_DB, self.DB)
                    

    def leer_lista_llaves(self):
        return self.dicc

    def crear_llave(self, llave):
        aux = 0
        for i in self.dicc:
            if str(llave['User']) == str(i['User']): 
                aux = 1

        if aux == 0: 
            self.dicc.append(llave)
               

    def leer_contrasena(self, llave):
        for i in self.dicc:
            if str(llave) == str(i['User']): 
                return i['Pass']


    def eliminar(self, llave):
        for i in self.dicc:
            if str(llave) == str(i['User']): 
                self.dicc.remove(i)