import os, json, re

lines = [line.rstrip('\n') for line in open('mining_ip')]

unlock = "miner.setEtherbase('0x37C8aB6329Dd4541ec178d3FfAe834e61f536874');"
mine = 'miner.start();'

for addr in lines:
	command = './geth attach {} --exec "{} {}"'.format(addr, unlock, mine)

	result = os.popen(command).readlines()
	print(str(result))
