import sys
import subprocess

procs = []
path = 'C:\\Users\\Aensea\\Documents\\Nikunj\\Programming\\PassFuzzer\\demo\\'
for i in range(16,21):
    proc = subprocess.Popen([sys.executable, 'test.py',f'-P{path}passlist{i}.txt'])
    procs.append(proc)

for proc in procs:
    proc.wait()