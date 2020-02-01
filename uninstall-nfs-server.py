#!/usr/bin/python3
import sys
import os
import shutil

dry_run = True  # Set to true to not make changes for testing

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

def uninstall_server(): 
     '''Function to uninstall nfs server.'''
     if dry_run:
        print("Uninstalling nfs-kernel-server")
     else:
        print("Uninstalling nfs-kernel-server")
        os.system('sudo apt-get remove -y nfs-kernel-server')
        os.remove("/etc/exports")
        shutil.copy('/etc/exports.bak', '/etc/exports')
        os.remove("/etc/exports.bak")

if not yes_or_no("Do you want to setup an NFS server?"):
    print("Exiting Setup")
    sys.exit()

uninstall_server()
