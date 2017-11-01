import subprocess

p = subprocess.Popen(["bash stat_julius.sh"],stdout=subprocess.PIPE,shell=True)
pid = p.stdout.read() 

p.kill()
subprocess.call(["kill" +pid],shell=True)
