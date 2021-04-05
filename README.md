# osmc-nfs-server-python3

Python3 script for setting up NFS-Server on OSMC, automount shares & manual shares. 

<h3>Install:</h3>

OSMC Stretch:
          
          sudo python3 nfs-server-setup.py
          
OSMC Buster:
          
          sudo python nfs-server-setup.py
   

<h3>Uninstall:</h3>

OSMC Stretch:

          sudo python3 uninstall-nfs-server.py
          
OSMC Buster:

          sudo python uninstall-nfs-server.py
          
Uninstall script removes server and reverts /etc/exports to default. 

<h3>Kodi Instructions</h3>

The easiest way is to map some shortcuts to some keys for example f11 & f12, for example (will need to use the command line):

          cd /home/osmc/.kodi/userdata
          wget https://raw.githubusercontent.com/tomdoyle87/osmc-nfs-server-python3/master/Kodi-nfs-server-setup.py
          wget https://raw.githubusercontent.com/tomdoyle87/osmc-nfs-server-python3/master/Kodi-uninstall-nfs-server.py

Then add the following to keyboard.xml or remote.xml (in the global section):

          <keyboard>
                    <F11>XBMC.RunScript(special://home/Kodi-nfs-server-setup.py)</F11>         
                    <F12>XBMC.RunScript(special://home/Kodi-uninstall-nfs-server.py)</F12>
          </keyboard>

