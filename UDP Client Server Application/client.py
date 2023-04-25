import socket
# Client with buffer size of only 100
def client():
    host = socket.gethostname()                 # gets the host name
    port = 6000                                 # server port
    buffer_size = 100                           # buffer size of receiving data
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # used SOCK_DGRAM for the udp connection.
    server_address = (host, port)
    print("Connecting to port: ", port)
    filename = 'F' + input('Enter the filename: ')# input file name and add F to make it a file PDU
    client_socket.sendto(filename.encode(), server_address)           # send filename  to server by encoding it.
    print('Request sent to server.')
    print('Receiving...')
    while True:
        data, address = client_socket.recvfrom(buffer_size)
        if chr(data[0]) == 'D':                 # for checking Data pdu
            file = open('myfile.txt', 'a', encoding='utf-8')
            file.write(data[1:].decode())       # appending data recieved from server.
            print('\t',data[1:])

        if chr(data[0]) == 'E':                 # for checking the pdu with error.
            print('Failure.')
            print(data[1:].decode())
            break

        if chr(data[0]) == 'L':                 # for checking the last pdu.
            print('SUCCESS: All data received successfully.\nDONE!!!')
            client_socket.close()
            break

if __name__ == '__main__':
    client()