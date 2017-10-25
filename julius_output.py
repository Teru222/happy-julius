import socket

HOST = "192.168.2.104" #アドレス
PORT = 10500 #ポート

#TCPクライアントを作成し接続
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

#サーバの応答を受信
data = client.recv(1024)
