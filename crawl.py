import os, json, re

lines = [line.rstrip('\n') for line in open('ip')]

mining = []
admin = []

for addr in lines:
	try:
		command = './geth attach {} --exec "rpc.modules"'.format(addr)

		try:
			result = os.popen(command).readlines()
			parsed = str(result).replace("\\n", '').replace("', '", '" ').replace(':', '":').replace('""', '"')[2:][:-2]
			parsedJson = json.loads(parsed.replace('   ', ''))
			print(addr, parsedJson)

			if 'miner' in parsedJson:
				print('Found miner! ' ,addr, parsedJson)
				mining.append(addr)
			if 'admin' in parsedJson:
				print('Found admin! ' ,addr, parsedJson)
				admin.append(addr)
		except Exception as e:
			print(e)
	except Exception as e:
		print(e)
		break

f = open('mining_ip', 'w')
for ip in mining:
	f.write(ip + '\n')
	
f = open('admin_ip', 'w')
for ip in mining:
	f.write(ip + '\n')
	
f = open('db_ip', 'w')
for ip in mining:
	f.write(ip + '\n')

f.close()
