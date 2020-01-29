#!/usr/bin/python3
import sys
import os
import shutil
## Uninstall function
def uninstall_server():  
    os.system('sudo apt-get remove -y nfs-kernel-server')
    os.remove("/etc/exports")
    shutil.copy('/etc/exports.bak', '/etc/exports')
    os.remove("/etc/exports.bak")

## Function to validate yes no input.
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
question = yes_or_no("Do you want to uninstall the  NFS server?  ")
if reply == '0':
   print("Exiting Setup")
   sys.exit()

print("Uninstalling Server")
uninstall_server()
