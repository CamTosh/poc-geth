import os, json, re

lines = [line.rstrip('\n') for line in open('admin_ip')]

addPeer = "admin.addTrustedPeer('enodeHere')"

for addr in lines:
	command = './geth attach {} --exec "{} {}"'.format(addr, addPeer)

	result = os.popen(command).readlines()
	print(str(result))
