import json
import sys
import time

import requests


def banner():
	print('''
  ______ _          ______ _       
 |  ____(_)        |  ____| |      
 | |__   _ _ __ ___| |__  | |_   _ 
 |  __| | | '__/ _ \  __| | | | | |
 | |    | | | |  __/ |    | | |_| |
 |_|    |_|_|  \___|_|    |_|\__, |
                              __/ |
                             |___/ 
	Author: Lexxrt
	Github: https://github.com/Lexxrt             
	''')

def main():
	banner()
	if len(sys.argv) == 2:
		number = sys.argv[1]
		try:
			output = requests.get(f'http://apilayer.net/api/validate?access_key={key}&number={number}&country_code=&format=1', timeout=15)
			obj = json.loads(output.text)
		except Exception as e:
			print(f'Fetching data failed: {e}')
			exit(1)
		
		country_code = obj['country_code']
		country_name = obj['country_name']
		location = obj['location']
		carrier = obj['carrier']
		line_type = obj['line_type']

		print('[+] Phone number information gathering')
		print('--------------------------------------')
		time.sleep(0.2)

		if country_code == '':
			print(' - Getting Country\t\t[ FAILED ]')
		else:
			print(' - Getting Country\t\t[ OK ]')

		time.sleep(0.2)
		if country_name == '':
			print(' - Getting Country Name\t\t[ FAILED ]')
		else:
			print(' - Getting Country Name\t\t[ OK ]')

		time.sleep(0.2)
		if location == '':
			print(' - Getting Location\t\t[ FAILED ]')
		else:
			print(' - Getting Location\t\t[ OK ]')

		time.sleep(0.2)
		if carrier == '':
			print(' - Getting Carrier\t\t[ FAILED ]')
		else:
			print(' - Getting Carrier\t\t[ OK ]')

		time.sleep(0.2)
		if line_type == None:
			print(' - Getting Device\t\t[ FAILED ]')
		else:
			print(' - Getting Device\t\t[ OK ]')

		print('[+] Information Output')
		print('--------------------------------------')
		print(' - Phone number:', number)
		print(' - Country:', country_code)
		print(' - Country Name:', country_name)
		print(' - Location:', location)
		print(' - Carrier:', carrier)
		print(' - Device:', line_type)
	else:
		print('[?] Usage:')
		print('\tFireFly.py <phone-number>')
		print('	python3 FireFly.py +13213707446 (Test Number)')

if __name__ == '__main__':
	try:
		config = open('config.json').read()
		data = json.loads(config)
	except Exception as e:
		print(f'Reading config failed: {e}')
		exit(1)
	key = data['api_key']
	main()
