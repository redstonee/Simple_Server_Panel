#!/usr/bin/python3
import time, threading
from bottle import *

is_online = 0
IP = ''
cpu_l = 0
mem_u = 0
t0 = time.time() - 5

def chk_online():
	global is_online, t0
	while True:
		if time.time() - t0 > 5:
			is_online = 0

		else:
			is_online = 1

		time.sleep(2)

threading.Thread(target=chk_online).start()

@route('/getinf')
def inff():
	if is_online:
		return {'online':1, 'ip':IP, 'cpu':cpu_l, 'mem':mem_u}

	else:
		return {'online':0}

@route('/postinf/:ip/:cpu_load/:mem_used')
def receivee(ip, cpu_load, mem_used):
	global is_online, IP, cpu_l, mem_u, t0
	t0 = time.time()
	is_online = 1
	IP, cpu_l, mem_u = ip, cpu_load, mem_used

run(host='0.0.0.0', port=11451)
