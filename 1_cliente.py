#Configuración Básica de Sockets: Implementa un servidor de sockets básico que escuche en un puerto específico y 
# acepte conexiones de un solo cliente. El servidor debería enviar un mensaje de bienvenida al cliente y luego cerrar la conexión.
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
direccion = '127.0.0.1'
puerto = 5553

s.connect((direccion,puerto))


respuesta = s.recv(2000).decode("utf")
print(respuesta)

