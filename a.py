import socket
import xml.etree.ElementTree as ET
import os
import subprocess
import time

host = '192.168.11.26'
port = 10500

def main():

    p = subprocess.Popen(["./b.sh"], stdout=subprocess.PIPE, shell=True)
    pid = str(p.stdout.read().decode('utf-8')) # juliusのプロセスIDを取得
    time.sleep(3)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    try:
        data = ''
        killword =''
        while 1:
            #print(data)
            if '</RECOGOUT>\n.' in data:
                
                root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
                for whypo in root.findall('./SHYPO/WHYPO'):

                    command = whypo.get('WORD')
                    if command == u'こんにちは':
                        if killword != ('こんにちは'):
                            os.system("aplay '/home/pi/Music/ohayo.wav'")
                            killword = ('こんにちは')

                    elif command == u'おはよう':
                        if killword != ('こんにちは'):
                            os.system("aplay '/home/pi/Music/ohayo.wav'")
                            killword = ('おはよう')
                        
                    elif command == u'こんばんは':
                        if killword != ('こんにちは'):
                            os.system("aplay '/home/pi/Music/ohayo.wav'")
                            killword = ('こんばんは')

                    elif command == u'ばいばい':
                        if killword != ('こんにちは'):
                            os.system("aplay '/home/pi/Music/ohayo.wav'")
                            killword = ('ばいばい')
                        
                    elif command == u'せもぽぬめ':
                        os.system("aplay '/home/pi/Music/ohayo.wav'")
                        killword = ('シークレット')

                    elif command == u'おやすみ':
                        os.system("aplay '/home/pi/Music/ohayo.wav'")
                        killword = ('おやすみ')
                        
                    else:
                        os.system("aplay '/home/pi/Music/ohayo.wav'")
                        killword = ('ラズ')
                    print (command)
                    data = '' 

            else:
                data += str(client.recv(1024).decode('utf-8'))
                print('NotFound')


    except KeyboardInterrupt:
        p.kill()
        subprocess.call(["kill " + pid], shell=True)
        client.close()

if __name__ == "__main__":
    main()
