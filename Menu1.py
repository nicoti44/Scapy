## Show menu ##

import os

import sys



print (30 * '-')

print ("   M A I N - M E N U")

print (30 * '-')

print ("1. ARP_Spoofing Attack (MiTM)")

print ("2. Reboot the server")

print (30 * '-')



## Choix de L'utilisateur ###

choice = input('Enter your choice [1-2] : ')



### Conversion du choix UT ##

choice = int(choice)



### Action en fonction du choix de l'UT ###

if choice == 1:

        print ("ARP_Spoofing Attack (MiTM)")

        interface = input("Renseigne ton interface:\n")

        print ("Starting ARP_Spoofing Attack")

      

        os.system(" python /home/ni/Documents/Bam/Bam/ARP_Spoofing.py {interface} 192.168.1.62 192.168.1.1 1")



elif choice == 2:

        print ("a completer")





else:    ## default ##

        print ("Invalid number. Try again...")
