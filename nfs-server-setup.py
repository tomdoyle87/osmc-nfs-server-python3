#!/usr/bin/python3
import sys
import re
import os
import shutil

dry_run = True  # Set to true to not make changes for testing

## Function to validate read status of share.
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

## Function to validate IPs and networks.
def check(Ip):  
  
    global ip
    if(re.search(regex, Ip)):  
        print("Valid Ip address")  
        ip = '1'  
    else:  
        print("Invalid Ip address, please try again")
        ip ='0'


def yes_or_no(question):
    '''Function to validate yes no input.'''
    answer = None
    while answer not in ["yes", "y", "no", "n"]:
        if answer is not None:
            print("Input yes or no")
        answer = input(f"{question} (yes/no): ").lower().strip()
    if answer[0] == "y":
        return True
    if answer[0] == "n":
        return False

## Function to install NFS server
def install_server():
    if dry_run:
        print("Installing nfs-kernel-server")
    else:
        os.system('sudo apt-get update' and 'sudo apt-get install -y nfs-kernel-server')
        shutil.copy('/etc/exports', '/etc/exports.bak')


if not yes_or_no("Do you want to setup an NFS server?"):
    print("Exiting Setup")
    sys.exit()

ip = ' '
print("Installing Server")
install_server()
if yes_or_no("Do you want Restrict what IPs can access the Server?"):
    while ip != '1':
        Ip = input("Please enter an IP network, for example 192.168.0.1/24. Or A single host, e.g. 192.168.1.15 ")
        check(Ip)
        if ip == '1':
            break
        if ip == '0':
            continue
else:
    print("Not restricting IP")
    Ip = '?'

default_options = ["sync", "no_root_squash"]
print("Now setting up share for automounts")
read()
line_to_add = f"/media/ {Ip}({st},{','.join(default_options)})"
if dry_run:
    print(line_to_add)
else:
    print(line_to_add, file=open("/etc/exports", "a"))
print("Share for automounts complete")

while True:
    if yes_or_no("Do you wish to setup any additional shares e.g. /home/osmc/share"):
        share = input("Please enter share path? ")
        while not os.path.isabs(share):
            share = input("Please try again, needs to be a absolute path ")
            os.path.isabs(share)
        if not os.path.exists(share):
            print(f"Creating mountpoint: {share}")
            if not dry_run:
                os.makedirs(share)
        read()
        line_to_add = f"{share} {Ip}({st},{','.join(default_options)})"
        if dry_run:
            print(f"Adding: {line_to_add}")
        else:
            print(line_to_add, file=open("/etc/exports", "a"))
    else:
        print("No additional share to added")
        break

if not dry_run:
    exportfs = '/usr/sbin/exportfs -ra'
    os.system(exportfs)
print("Listing Shares: ")
showmount = '/sbin/showmount -e 127.0.0.1'
os.system(showmount)
print("Server setup completed")
