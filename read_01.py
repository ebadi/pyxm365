"""Read DEV01 memory to file"""
from sys import exit
from NBPort import NBPort

port = NBPort(dump=True)

if not port.open():
	exit("Can't open port !")

hfo = open("01_config.bin", "wb")
for i in range(0, 0x100, 0x80):
	hfo.write(port.DEV01ReadRegs(i>>1, 0x80))
hfo.close()
