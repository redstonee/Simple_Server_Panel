#!/usr/bin/python3
import time, psutil, requests, socket

while True:
	a = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	a.connect(('8.8.8.8',80))
	ip = a.getsockname()[0]
	a.close()
	cpul = psutil.cpu_percent()
	mem = psutil.virtual_memory()
	try:
		requests.get('http://121.37.143.236:11451/postinf/{}%/{}/{},{}'.format( ip, cpul, int(mem.used / 1024**2 * 100) / 100, int(mem.total/1024**2 * 100) / 100))

	except requests.RequestException:
		print('Upload Error')

	time.sleep(2)

