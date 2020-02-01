#!/usr/bin/python3
import sys
import re
import os
import shutil
import ipaddress

if sys.argv[1] in ['--dry-run', '-d', '--d']:
    dry_run = True
    print("Running dry_run, no changes will be written.")
else:
    dry_run = False


def ro_or_rw(question):
    '''Function to validate ro rw input.'''
    answer = None
    while answer not in ["ro", "rw"]:
        if answer is not None:
            print("Input ro or rw")
        answer = input(question + "(ro/rw): ").lower().strip()
    return answer


def check(Ip):
    '''Function to validate IP'''
    if Ip is None:
        return False
    try:
        ipaddress.IPv4Network(Ip)
    except ipaddress.AddressValueError as e:
        print("Bad IP address:", e)
        return False
    except ValueError as e:
        print("Bad network:", e)
        return False

    return True


def yes_or_no(question):
    '''Function to validate yes no input.'''
    answer = None
    while answer not in ["yes", "y", "no", "n"]:
        if answer is not None:
            print("Input yes or no")
        answer = input(question + "(yes/no): ").lower().strip()
    if answer[0] == "y":
        return True
    if answer[0] == "n":
        return False


def install_server():
    '''Function to install nfs server.'''
    if dry_run:
        print("Installing nfs-kernel-server")
    else:
        os.system('sudo apt-get update' and
                  'sudo apt-get install -y nfs-kernel-server')
        shutil.copy('/etc/exports', '/etc/exports.bak')


if not yes_or_no("Do you want to setup an NFS server?"):
    print("Exiting Setup")
    sys.exit()

install_server()

if yes_or_no("Do you want Restrict what IPs can access the Server?"):
    Ip = None
    while not check(Ip):
        Ip = input("Please enter an IP network, " +
                   "for example 192.168.1.0/24. " +
                   "Or A single host, e.g. 192.168.1.15 ")
else:
    print("Not restricting IP")
    Ip = '*'

print("Now setting up share for automounts")
st = ro_or_rw("Should the share be read/write or read only? ")

if dry_run:
    print('/media/ ' + Ip + '(' + st + ',sync,no_root_squash)')
else:
    print('/media/ ' + Ip + '(' +
          st + ',sync,no_root_squash)', file=open("/etc/exports", "a"))
print("Share for automounts complete")

while True:
    if yes_or_no("Do you wish to setup any additional shares " +
                 "e.g. /home/osmc/share"):
        share = input("Please enter share path? ")
        while not os.path.isabs(share):
            share = input("Please try again, needs to be a absolute path ")
            os.path.isabs(share)
        if not os.path.exists(share):
            print("Creating mountpoint")
            if not dry_run:
                os.makedirs(share)
        st = ro_or_rw("Should the share be read/write or read only? ")
        if dry_run:
            print(share, Ip + '(' + st + ',sync,no_root_squash)')
        else:
            print(share, Ip + '(' + st + ',sync,no_root_squash)',
                  file=open("/etc/exports", "a"))
    else:
        print("No additional share to added")
        break

if not dry_run:
    exportfs = '/usr/sbin/exportfs -ra'
    os.system(exportfs)
print("Listing Shares: ")
if not dry_run:
    showmount = '/sbin/showmount -e 127.0.0.1'
    os.system(showmount)
print("Server setup completed")
