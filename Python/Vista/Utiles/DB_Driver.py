import pymongo, urllib
from Utiles.Encriptar import encriptar, desencriptar

def conectar():

    client = pymongo.MongoClient("mongodb+srv://arodriguem:"+urllib.parse.quote("CAMO@@134")+"@cluster0.5aa1j.mongodb.net/?retryWrites=true&w=majority")
    
    db = client['User']
    return db

def agregarUs(usuario,contraseña) :
    
    con = encriptar(contraseña) 

    db = conectar()
    db.Usuarios.insert_one({
        'Nombre del usuario' : usuario,
        'Contrasena' : con.decode('utf-8')
    })


def getUsuario(usuario):
    db = conectar()

    usuario = db.Usuarios.find_one({'Nombre del usuario': usuario})

    
    if usuario == None:
        return None
    else:
        contrasena = desencriptar(usuario)
        return contrasena
 
