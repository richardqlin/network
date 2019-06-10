import socket
from _thread import *

host = ''

port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = socket.gethostbyname(host)
try:
    s.bind((host, port))

except socket.error as e:
    print(str(e))

s.listen(2)

print('waiting for a connection, server started')


#currentId ='0'

pos = [(0,0) , (100,100)]
def read_pos(str):
    str = str.split(',')
    return int(str[0]),int(str[1])

def make_pos(tmp):
    return str(tmp[0]) + ',' + str(tmp[1])

def threaded_client(conn,player):
    global currentPlayer
    print(player)
    conn.send(str.encode(make_pos(pos[player])))


    receive = ''
    while 1:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data


            #receive = data.decode('utf-8')
            #print(receive)

            if not data:
                print('disconnected')
                break
            else:
                if player == 1:
                    receive = pos[0]
                else:
                    receive = pos[1]

                print('recerived: ', data)
                '''
                arr = receive.split(':')
                id = int(arr[0])
                pos[id] = receive
                if id == 0: nid = 1
                if id == 1: nid = 0
                '''
                print('sending:', receive)

            conn.sendall(str.encode(make_pos(receive)))

        except:
            break
    print('lost connection')
    currentPlayer = 0
    conn.close()



currentPlayer = 0

while 1:
    conn, addr = s.accept()
    print('Connected to', addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
