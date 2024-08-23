# Cliente Simple de Chat: 
#Desarrolla un cliente que se conecte a un servidor de sockets y
#permita al usuario enviar un mensaje simple a través de la terminal. 
#Una vez enviado, el cliente debería cerrar la conexión.
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
direccion = '127.0.0.1'
puerto = 5553

s.connect((direccion,puerto))

while True:
    try:
        respuesta = s.recv(2000).decode("utf-8")
        print(respuesta)
        mensaje = input()
        if mensaje:
            s.send(mensaje.encode("utf-8"))
            s.close()
            break
    except Exception as e :
        (f'Error {e}')

