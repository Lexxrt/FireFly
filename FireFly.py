import sys
import requests
import json
import time
import urllib
import os

class config:
	key = "4395fd642c2f1b24f5d9d01e0a1f838a"

def banner():
	print ("""
  _____ _          _____ _       
 |  ___(_)_ __ ___|  ___| |_   _ 
 | |_  | | '__/ _ \ |_  | | | | |
 |  _| | | | |  __/  _| | | |_| |
 |_|   |_|_|  \___|_|   |_|\__, |
                           |___/ 
	Author: Lexxrt
	Github: https://github.com/Lexxrt             
	""")

def main():
	banner()
	if len(sys.argv) == 2:
		number = sys.argv[1]
		api = "http://apilayer.net/api/validate?access_key=" + config.key + "&number=" + number + "&country_code=&format=1"
		output = requests.get(api)
		content = output.text
		obj = json.loads(content)
		country_code = obj['country_code']
		country_name = obj['country_name']
		location = obj['location']
		carrier = obj['carrier']
		line_type = obj['line_type']

		print ("[+] " + "Phone number information gathering")
		print ("--------------------------------------")
		time.sleep(0.2)

		if country_code == "":
			print (" - Getting Country		[ " + "FAILED " + "]")
		else:
			print (" - Getting Country		[ " + "OK " + "]")

		time.sleep(0.2)
		if country_name == "":
			print (" - Getting Country Name		[ " + "FAILED " + "]")
		else:
			print (" - Getting Country Name		[ " + "OK " + "]")

		time.sleep(0.2)
		if location == "":
			print (" - Getting Location		[ " + "FAILED " + "]")
		else:
			print (" - Getting Location		[ " + "OK " + "]")

		time.sleep(0.2)
		if carrier == "":
			print (" - Getting Carrier		[ " + "FAILED " + "]")
		else:
			print (" - Getting Carrier		[ " + "OK " + "]")

		time.sleep(0.2)
		if line_type == None:
			print (" - Getting Device		[ " + "FAILED " + "]")
		else:
			print (" - Getting Device		[ " + "OK " + "]")

		print ("")
		print ("[+] " + "Information Output")
		print ("--------------------------------------")
		print (" - Phone number: " + str(number))
		print (" - Country: " + str(country_code))
		print (" - Country Name: " + str(country_name))
		print (" - Location: " + str(location))
		print (" - Carrier: " + str(carrier))
		print (" - Device: " + str(line_type))
	else:
		print ("[?] Usage:")
		print ("	./%s <phone-number>" % (sys.argv[0]))
		print ("	./%s +13213707446" % (sys.argv[0]))

main()
