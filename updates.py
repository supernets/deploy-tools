#!/usr/bin/env python
import re, urllib.request

anope_version      = '2.0.6'
bootstrap_version  = '4.0.0'
jquery_version     = '3.3.1'
unrealircd_version = '4.0.17'

def between(source, start, stop):
	data = re.compile(start + '(.*?)' + stop, re.IGNORECASE|re.MULTILINE).search(source)
	return data.group(1) if data else False

def get_source(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'DickServ/1.0')
	source = urllib.request.urlopen(req, timeout=10)
	charset = source.headers.get_content_charset()
	return source.read().decode(charset) if charset else source.read().decode()

def update_anope()      : return between(get_source('http://www.anope.org/'), '<span>Latest Stable Release:</span> Anope ', '\n')
def update_bootstrap()  : return between(get_source('http://getbootstrap.com/'), '<p>Currently v', '. Code licensed')
def update_jquery()     : return between(get_source('http://jquery.com/'), '<span>v', '</span>')
def update_unrealircd() : return between(get_source('http://www.unrealircd.org/docs/FAQ'), '<p>The latest <b>Stable</b> version is <b>', '</b>')

latest_anope = update_anope()
if latest_anope:
	if latest_anope != anope_version:
		print(f'Anope version {latest_anope} has been released!')
	else:
		print('Anope is up to date.')
else:
	print('[!] - Can not retrieve latest Anope version.')
latest_bootstrap = update_bootstrap()
if latest_bootstrap:
	if latest_bootstrap != bootstrap_version:
		print(f'Bootstrap version {latest_bootstrap} has been released!')
	else:
		print('Bootstrap is up to date.')
else:
	print('[!] - Can not retrieve latest Bootstrap version.')
latest_jquery = update_jquery()
if latest_jquery:
	if latest_jquery != jquery_version:
		print(f'jQuery version {latest_jquery} has been released!')
	else:
		print('jQuery is up to date.')
else:
	print('[!] - Can not retrieve latest jQuery version.')
latest_unrealircd = update_unrealircd()
if latest_unrealircd:
	if latest_unrealircd != unrealircd_version:
		print(f'UnrealIRCd version {latest_unrealircd} has been released!')
	else:
		print('UnrealIRCd is up to date.')
else:
	print('[!] - Can not retrieve latest UnrealIRCd version.')