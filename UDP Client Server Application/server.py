import socket
# Created Server with buffer size of only 100 bytes
def server():
    host = socket.gethostname()                     # Getting the host name
    port = 6000                                     # Provided the port name
    buffer_size = 100                               # Define the buffer size of receiving information
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM represents the UDP connection.
    server_address = (host, port)                   # address of the server.
    server_socket.bind(server_address)              # binded the server_socket with the address
    print('Server Started !!!')
    data, client_address = server_socket.recvfrom(buffer_size)
    print('Receiving Request from:', client_address)
    data = data.decode()
    if data[0] == 'F':                              # for checking File PDU
        filename = data[1:]
        print("Received Request for file:", filename)
        try:                                        # try for checking file
            file = open(filename, 'rb')             # reading data from file in the form of bytes
            print("Sending Data...")
            while True:
                data = file.read(99)                # reading only 99 bytes and then add one letter for PDU to make PDU of 100 bytes because we can only send 100 bytes per PDU.
                if not data:                        # for checking if no more data remains in the file to read.
                    last_data = b'L' + data         # added L to indicate the last PDU
                    server_socket.sendto(last_data, client_address)     # since data is read in byte form so, no need to encode it again.
                    print('SUCCESS: All data sent successfully.')
                    break
                data = b'D' + data                  # added D to indicate the Data PDU.
                print('\t',data)
                server_socket.sendto(data, client_address)

        except FileNotFoundError:
            msg = 'Request Failed: Error has occurred. File not Found!!!'
            error = 'E'+ msg
            print(msg)
            server_socket.sendto(error.encode(), client_address)
    else:
        msg = 'Request Failed: Not a filename'
        error = 'E' + msg
        server_socket.sendto(error.encode(), client_address)
    server_socket.close()

if __name__ == '__main__':
    server()