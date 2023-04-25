import socket

def server():
    host = socket.gethostname()         # get the host name
    port = 6000                         # defined port number.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # instantiated the socket
    server_socket.bind((host,port))     # bind host and port together.
    server_socket.listen(2)             # configure how many clients server can lister.
    data_buff = 2048                    # defined buffer size
    print("WAITING FOR CONNECTION...")
    conn, address = server_socket.accept()   #used for accepting the new connection and it returns connection and address
    print("CONNECTION ESTABLISHED !!!")
    print("CONNECTION RECIEVED FROM",address)
    data = conn.recv(data_buff).decode()     # for reciving data and provided the buffer size
    print("Server Recieved the filename: ",data)
    try:                                     # used try and except for catching file not found exception and display the error message.
        file1 = open(data, encoding="utf-8") # file opening
        data = file1.read()                  # reading data
        file1.close()                        # closing file
        print("Sending Data...")
        print(data)
        print('DONE!!!')
        conn.send(data.encode())             # for sending the data to client
    except FileNotFoundError:
        print("Error: File Not Found!!")
    server_socket.close()                    # close the connection

if __name__ == '__main__':
    server()