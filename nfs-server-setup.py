#!/usr/bin/python3
import sys
import re
def read():
    global st
    st = ' '
    while st != 'ro' or st != 'rw':
        st = input("Does the share need to be read only or read write (ro/rw):")
        if st == 'ro' or st == 'rw':
            break
        else:
            print("Invalid input, please try again?.")
## IP Validation regex. 
regex = "^(?=\d+\.\d+\.\d+\.\d+($|\/))(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.?){4}(\/([0-9]|[1-2][0-9]|3[0-2]))?$"

def check(Ip):  
  
    global ip
    global ip
    if(re.search(regex, Ip)):  
        print("Valid Ip address")  
        ip = '1'  
    else:  
        print("Invalid Ip address, please try again")
        ip ='0'

REPLY = ' '
while REPLY != 'yes' or REPLY != 'no':
    REPLY = input('Do you want to setup an NFS server?  (yes/no?): ')
    if REPLY == 'yes':
        print("Installing Server")
        break
    if REPLY == 'no':
        print("Exiting Setup")
        sys.exit()
    else:
        print("Invalid input, please try again?")

ip = ' '
REPLY = ' '
while REPLY != 'yes' or REPLY != 'no':
    REPLY = input('Do you want Restrict what IPs can access the Server? (yes/no?): ')
    #print(REPLY)
    if REPLY != 'yes' or REPLY != 'no':
        print("Invalid input, please try again?")        
        if REPLY == 'yes':
            while ip !='1':
                Ip = ' '
                Ip = input ('Please enter an IP network, for example 192.168.0.1/24. Or A single host, e.g. 192.168.1.15 ')
                check(Ip)
                if ip == '1':
                   continue
                if ip == '0':
                   continue  
            break
        if REPLY == 'no':
            print("Not restricting IP")
            Ip = '?'
            break
print(Ip)
