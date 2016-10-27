import socket


def main():
    host = "training.securitum.com"
    port = 11783


    my_socket = socket.socket()


    my_socket.connect((host, port))

    message = input(" -> ")

    while message != 'q':
        my_socket.send(message.encode())
        data = my_socket.recv(128).decode()

        print('Received from server: ' + data)

        message = input(" -> ")

    my_socket.close()

if __name__ == '__main__':
    main()