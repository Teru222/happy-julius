import socket
import xml.etree.ElementTree as ET
import os
import subprocess
import time
host = 'localhost'
port = 10500
def main():
    p = subprocess.Popen(["bash a.sh"], stdout=subprocess.PIPE, shell=True)
    
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    
    try:
        data = ''
        while 1:
           # print(data)
            if '</RECOGOUT>\n.' in data:
                root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
                for whypo in root.findall('./SHYPO/WHYPO'):
                    
                    command = whypo.get('WORD')
                    
                    print(command)
                    if command == u'こんにちは':
                        os.system("aplay '/home/pi/Music/ohayo.wav'")
                        time.sleep(3)
                        # ここに処理
                    #elif command == u'パキン' and score >= 0.996:
                        # ここにパキン処理
                    #elif command == u'おやすみ' and score >= 0.93:
                        # ここにおやすみ処理
                    #elif command == u'いってきます' and score >= 0.93:
                        # ここにいってきます処理
                    #elif command == u'部屋つけて' and score >= 0.93:
                        # ここに部屋つけて処理
                    #elif command == u'おはよう' and score >= 0.9:
                        # ここにおはよう処理
                    #elif command == u'部屋消して' and score >= 0.9:
                        # ここに部屋消して処理
                    #elif command == u'廊下つけて' and score >= 0.93:
                        # ここに廊下つけて処理
                    #elif command == u'廊下消して' and score >= 0.9:
                        # ここに廊下消して処理
                        #data = ''
                print (command)
            else:
                data = data + str(client.recv(1024).decode('utf-8'))
                print('NotFound')
                
    except KeyboardInterrupt:
        #p.kill()
        client.close()

if __name__ == "__main__":
    main()
