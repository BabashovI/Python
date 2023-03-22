from multiping import MultiPing

lst_ip = []
resp_ip = []
with open('IP.txt', 'r') as ip:
	for i in ip:
		lst_ip.append(i.strip())
mp = MultiPing(lst_ip)
mp.send()
resp, no_resp = mp.receive(2)
for host in resp.keys():
	resp_ip.append(host)
print(resp_ip)
print(no_resp)
with open('resp_ip.txt', 'w') as f:
	for i in resp_ip:
		f.write('{}\n'.format(i))