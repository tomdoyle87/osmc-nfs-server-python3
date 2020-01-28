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

def yes_or_no(question):
    global reply
    answer = input(question + "(yes/no): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(question + "(yes/no):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
        reply = '1'
    if answer[0] == "n":
        reply = '0'
    else:
        return False

reply = ' '
question = yes_or_no('Do you want to setup an NFS server? ')
if reply == '0':
   print("Exiting Setup")
   sys.exit()

ip = ' '
print("Installing Server")
reply = ' '
question = yes_or_no('Do you want Restrict what IPs can access the Server? ')
if reply != '0':
    while ip !='1':
         Ip = input ('Please enter an IP network, for example 192.168.0.1/24. Or A single host, e.g. 192.168.1.15 ')
         check(Ip)
         if ip == '1':
             break
         if ip == '0':
             continue

if reply == '0':
    print("Not restricting IP")
    Ip = '?'

print(Ip)
