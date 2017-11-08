# coding:utf-8
import socket
import subprocess
import xml.etree.ElementTree as ET
import os
host = "localhost"
port = 10500


voices = {
  u"おはよう" : [], \
  u"こんにちは" : [], \
  u"こんばんは" : []
}



 # def SelectVoice(koe):

;;;;
def main():
    
  # julius起動スクリプトを実行
  p = subprocess.Popen(["bash stat_julius.sh"], stdout=subprocess.PIPE, shell=True)
 # pid = p.stdout.read() # juliusのプロセスIDを取得

   # TCPクライアントを作成し接続
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((host, port))
  
  # サーバからのデータ受信と
  try:
    data = ""
    while 1:
      if "</RECOGOUT>\n." in data:
        # RECOGOUT要素以下をXMLとしてパース
        root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find("<RECOGOUT>"):].replace("\n.", ""))
        
        # 言葉を判別
        for whypo in root.findall("./SHYPO/WHYPO"):
          os.system("aplay '/home/pi/Music/ohayo.wav'")
          word = whypo.get("WORD")
          print (word)
          if word == ("こんにちは"):
          #if whypo.get("WORD") in colors.keys():
            # 判別した言葉に応じて色を変える
            os.system("aplay '/home/pi/Muisc/ohayo.wav'")
          else:
            print ("Unknown")
        data = ""
      else:
        data += str(client.recv(1024).decode('utf-8'))
        

  except KeyboardInterrupt:
    # CTRL+Cで終了
    print ("KeyboardInterrupt occured.")
    p.kill() 
    #subprocess.call(["kill " + pid], shell=True) # juliusのプロセスを終了
    client.close()
    

if __name__ == "__main__":
 
  main()

