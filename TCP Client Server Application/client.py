import socket

def client():
    host = socket.gethostname()                            # Gets the host name.
    port = 6000                                            # Provided the port number
    data_buff = 2048                                       # Buffer size
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # We instantiated the socket.
    client_socket.connect((host,port))                                  # connected to port.
    filename = 'mytext.txt'                    # provided the file name
    client_socket.send(filename.encode())               # used for sending the data by encoding it.
    data = client_socket.recv(data_buff).decode()   # used for receiving the data by decoding it.
    print("CONNECTION ESTABLISHED !!!")
    if data:                                         # for checking whether we have received data or not
        print("Opening File...\nReceiving Data,,,\n")
        print(data)
        print("\n\nSuccessfully received the data from file.")
    else:
        print("\nError: File Not Found!! \nPlease Enter the correct file name.\n")
    print("CONNECTION CLOSED !!!")
    client_socket.close()                   # for closing the connection.
if __name__ == '__main__':
    client()
