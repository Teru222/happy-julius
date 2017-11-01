# coding:utf-8
import socket
import subprocess
import xml.etree.ElementTree as ET
import RPi.GPIO as GPIO

HOST = "192.168.11.7"
PORT = 10500
voices = {
      u"こんにちは":[],\
      u"おはよう":[]
}

def putVoices(koe):
print happy

def main():
      
      # julius起動スクリプトを実行
      p = subprocess.Popen(["bash stat_julius.sh"], stdout=subprocess.PIPE, shell=True)
      pid = p.stdout.read() # juliusのプロセスIDを取得
      
      # TCPクライアントを作成し接続
      client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client.connect((HOST, PORT))
      
      # サーバからのデータ受信と
      try:
            data = ""
            while 1:
                  if "</RECOGOUT>\n." in data:
                        # RECOGOUT要素以下をXMLとしてパース
                        root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find("<RECOGOUT>"):].replace("\n.", ""))
                        # 言葉を判別
                        for whypo in root.findall("./SHYPO/WHYPO"):
                              if whypo.get("WORD") in voices.keys():
                                    # 判別した言葉に応じて色を変える
                                    putVoices(whypo.get("WORD"))
                              else:
                                    print "Unknown"
                                    data = ""
                        else:
                              data = data + client.recv(1024)
                              
      except KeyboardInterrupt:
      # CTRL+Cで終了
            print "KeyboardInterrupt occured."
            p.kill() #
            subprocess.call(["kill " + pid], shell=True) # juliusのプロセスを終了
            client.close()
            
            if __name__ == "__main__":
                  main()
                  
