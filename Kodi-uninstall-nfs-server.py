#!/usr/bin/python

import xbmc
import xbmcgui

import sys
import os
import shutil

dry_run = True

def uninstall_server(): 
    '''Function to uninstall nfs server.'''
    if dry_run:
        line1 = "Uninstalling nfs-kernel-server"
        xbmcgui.Dialog().ok('kodi',line1)
    else:
        line1 = "Uninstalling nfs-kernel-server"
        xbmcgui.Dialog().ok('kodi',line1)
        os.system('sudo apt-get remove -y nfs-kernel-server')
        os.remove("/etc/exports")
        shutil.copy('/etc/exports.bak', '/etc/exports')
        os.remove("/etc/exports.bak")

dialog = xbmcgui.Dialog()
if not dialog.yesno('Kodi', 'Do you want to uninstall the NFS server?'):
    line1 = "Exiting Setup"
    xbmcgui.Dialog().ok('kodi',line1)
    sys.exit()

uninstall_server()
