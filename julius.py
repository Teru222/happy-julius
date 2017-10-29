import subprocess

#julius起動スクリプト実行

p = subprocess.Popen(["bash stat_julius.sh"],stdout=subprocess.PIPE,shell=True)
pid = p.stdout.read() # juliusのプロセスIDを取得


p.kill() #起動スクリプトのプロセス終了
subprocess.call(["kill" +pid],shell=True) #juliusのプロセスを終了
