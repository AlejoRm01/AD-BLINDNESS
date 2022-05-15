from cryptography.fernet import Fernet


#---------------------------Encriptar-----------------------------------
def encriptar(password):
    
    file = open('key.key','rb')
    key = file.read()
    file.close()
    f = Fernet(key)
    encoded = password.encode()
    password = f.encrypt(encoded)

    return password 
#------------------Desencriptar-------------------------
def desencriptar(password):
      
    if not(type(password) == None):
        for i in password:
            m = i['Contraseña']
            file = open('key.key','rb')
            key = file.read()
            file.close()
            f = Fernet(key)
            m = m.encode()
            decrypted = f.decrypt(m).decode()   
            return decrypted
#------------------------Verificar---------------------------- ----

def verificar(password):
    entrar = False
    res = desencriptar(password)
    if password == res:
        entrar = True
        return entrar
    else:
        return entrar