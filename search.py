import shodan

api = shodan.Shodan(SHODAN_API_KEY)

ip = []

for i in range(1, 50):
	try:
		results = api.search('geth', i)

		for result in results['matches']:
			print("IP: {}".format(result['ip_str']))
			ip.append(result['ip_str'])

	except Exception as e:
		print(e)
		break

f = open('ip', 'w')
for i in ip:
	f.write('http://' + i + ':8545\n')
f.close()
