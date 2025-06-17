import socket
import csv
class server:
    __socket_obj : socket.socket
    __connection : socket.socket
    __file : open
    __path : str
    _reader : csv.reader
    __data : list
    def __int__(self):
        server.__socket_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.__socket_obj.bind(("197.0.0.1",2222))
        server.__socket_obj.listen(5)
        server.__connection,self.client_address=server.__socket_obj.accept()
    def get_item(self):
        try :
            if server.__connection:
                data=server.__connection.recv(1024).decode()
                server.__path=input(f"data path:")
        except:
            print("connection error")
            exit()
    def reader(self):
        server.__file_obj=open(server.__path,"r")
        server._reader=csv.reader(server.__file_obj)
        server.__data=list(x for x in server._reader)
    def send_data(self):
        server.__connection.sendall(server.__data.encode())
ser=server()
ser.get_item()