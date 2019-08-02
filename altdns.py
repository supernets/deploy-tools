#!/usr/bin/env python
import socket

dns = (
	'chat.mirccloud.com',
	'irc.fagz.net',
	'irc.hardchats.net',
	'irc.j3ws.biz',
	'irc.j3ws.org',
	'irc.k0de.org',
	'irc.ngr.bz',
	'irc.wepump.in',
	'serious.fuckin.business'
)

servers = set([i[4][0] for i in socket.getaddrinfo('irc.supernets.org', 6667)])
for hostname in dns:
	try:
		if socket.gethostbyname(hostname) in servers:
			print('OK\t\t' + hostname)
		else:
			print('FAIL\t' + hostname)
	except:
		print('ERROR\t' + hostname)