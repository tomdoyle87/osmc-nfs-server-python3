import xbmc
import xbmcgui

import sys
import os
import shutil
import ipaddress
import subprocess

dry_run = False

def check(Ip):
    '''Function to validate IP'''
    if Ip is None:
        return False
    try:
        ipaddress.IPv4Network(Ip)
    except ipaddress.AddressValueError as e:
        line1 = "Bad IP address:"
        xbmcgui.Dialog().ok('kodi',line1)
        return False
    except ValueError as e:
        line1 = "Bad network:"
        xbmcgui.Dialog().ok('kodi',line1)
        return False

    return True

def install_server():
    '''Function to install nfs server.'''
    line1 = "Installing nfs-kernel-server"
    source = "/etc/exports"
    dest = "/etc/exports.bak"
    if dry_run:
        xbmcgui.Dialog().ok('kodi',line1)
    else:
        xbmcgui.Dialog().ok('kodi',line1)
        os.system('sudo apt-get update' and 
                  'sudo apt-get install -y nfs-kernel-server')
        shutil.os.system('sudo cp "{}" "{}"'.format(source,dest))
		

dialog = xbmcgui.Dialog()
if not dialog.yesno('Kodi', 'Do you want to setup an NFS server?'):
    bye="Exiting Setup"
    xbmcgui.Dialog().ok('kodi',bye)
    sys.exit()

install_server()

dialog = xbmcgui.Dialog()
if dialog.yesno('Kodi', 'Do you want Restrict what IPs can access the Server?'):
    Ip = None
    while not check(Ip):
        dialog = xbmcgui.Dialog()
        Ip = dialog.input('Please enter an IP network', type=xbmcgui.INPUT_ALPHANUM)
                   
else:
    wildcard = "Not restricting IP"
    xbmcgui.Dialog().ok('kodi',wildcard)
    Ip = '*'
	
line1 = "Now setting up share for automounts"
xbmcgui.Dialog().ok('kodi',line1)

if dialog.yesno('Kodi', 'Should the share be read only (If not sure, select Yes)?'):
    st = "ro"
else:
    st = "rw"

line1 = "Shares for automounts, setup as requested"
if dry_run:
    xbmcgui.Dialog().ok('kodi',line1)
else:
    xbmcgui.Dialog().ok('kodi',line1)
    source = "/home/osmc/exports"
    dest = "/etc/exports"
    print('/media/ ' + Ip + '(' +
          st + ',sync,no_root_squash)', file=open("/home/osmc/exports", "a"))
    shutil.os.system('sudo cp "{}" "{}"'.format(source,dest))

line1 = "Share for automounts complete"
xbmcgui.Dialog().ok('kodi',line1)

while True:
    if dialog.yesno('Kodi', 'Do you wish to setup any additional shares, e.g. /home/osmc/share'):
        share = dialog.input('Please enter a share path?', type=xbmcgui.INPUT_ALPHANUM)
        while not os.path.isabs(share):
            share = dialog.input('Please try again, needs to be a absolute path',  type=xbmcgui.INPUT_ALPHANUM)
            os.path.isabs(share)
        if not os.path.exists(share):
            line1 = "Creating mountpoint"
            xbmcgui.Dialog().ok('kodi',line1)
            if not dry_run:
                #os.makedirs(share)
                os.environ['share'] = share
                command = [". /home/osmc/.kodi/create-dir.sh" ]
                subprocess.call(command, shell=True)
                line1 = "Creating mountpoint"
                xbmcgui.Dialog().ok('kodi',line1)
        if dialog.yesno('Kodi', 'Should the share be read only (If not sure, select Yes)?'):
            st = "ro"
        else:
            st = "rw"
        if dry_run:
            line1 = "Setting up additonal shares as requested"
            xbmcgui.Dialog().ok('kodi',line1)            
        else:
            source = "/home/osmc/exports"
            dest = "/etc/exports"
            line1 = "Setting up additonal shares as requested"
            xbmcgui.Dialog().ok('kodi',line1)
            print(share, Ip + '(' + st + ',sync,no_root_squash)',file=open("/home/osmc/exports", "a"))
            shutil.os.system('sudo cp "{}" "{}"'.format(source,dest))

    else:
        line1 = "No additional share to added"
        xbmcgui.Dialog().ok('kodi',line1)
        break
if not dry_run:
    exportfs = 'sudo /usr/sbin/exportfs -ra'
    os.system(exportfs)
    source = "/home/osmc/exports"
    os.remove(source)

line1 = "Server setup completed"
xbmcgui.Dialog().ok('kodi',line1)
