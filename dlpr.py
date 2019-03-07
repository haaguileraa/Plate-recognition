# -*- coding: utf-8 -*-
import subprocess
import tempfile
import time
import os

#import shlex

Bild= 'plate_recognition.py'
Video= 'alpr_video.py'


## You can modify these:
N_API='b94e5931100d7f8464d029fb8be37960e3ad520a'
mode=  Video
#Ort_v= '../../Fotos/VIDEO_CARRO-MOTO.mp4'
Ort_v= '../../720/00004.mp4'
#Ort_v= '../../4k/Clip0003.mp4'
Ort_f= '../../Fotos/placa.jpg'#prueba3.png'

#Video Mode
ff='0'  #First fotogramm
ef='10' #Last fotogram
jf='2'  #Jump between fotogramms


#____________DON'T CHANGE___________#
#	           |
#	           v

stringToMatch = '"plate": ' #What do you want to search
stringError= 'Traceback'
matchedLine = ''
error= 'Fehlbedienung, kein Nummernschild erkannte'
  
  
  
###__________VIDEO_____________###


if mode == Video:
	with tempfile.TemporaryFile() as tempf:
    		proc = subprocess.Popen(['python', mode, '--api', N_API, '--start', ff, '--end', ef, '--skip', jf, Ort_v], stdout=tempf)
   		proc.wait()
    		tempf.seek(0)
    		#print tempf.read() #Want to print everything? uncomennt
    		
    		open("placas.txt", "w").close
    		open('placas2.txt', 'w').close()
    		for line in tempf :
    			if stringToMatch in line:
    				matchedLine = line
    				print matchedLine
    				with open("placas.txt", "a") as text_file:
    					text_file.writelines(matchedLine) #+ "\r\n") 
 					#file.write(matchedLine "%d\r\n" % )
 					text_file.close()
 				
	
			elif stringError in line: 
				print error
			
			
			
			
			
			
			
###__________FOTO_____________###	


elif mode == Bild:
	with tempfile.TemporaryFile() as tempf:
    		proc = subprocess.Popen(['python', mode, '--api', N_API, Ort_f], stdout=tempf)
   		proc.wait()
    		tempf.seek(0)
		#print tempf.read() #Want to print everything? uncomennt
		
		open("placas.txt", "w").close
		open('placas2.txt', 'w').close
		for line in tempf :
    			if stringToMatch in line:
    				matchedLine = line
    				print matchedLine
    				with open("placas.txt", "a") as text_file:
    					text_file.writelines(matchedLine )#+ "\r\n") 
 					#file.write(matchedLine "%d\r\n" % )
 					text_file.close()
 				
	
			elif stringError in line: 
				print error
		

		

mull1='"plate": "' 
mull2='",' 			
with  open('placas.txt', 'r') as placas1_txt:
	for line2 in placas1_txt:
		with open("placas2.txt", "a") as placas2_txt: 
			#print line2.replace(mull, '')
			plate = line2.replace(mull1, '')
			plate2 = plate.replace(mull2, '')
			#print plate2
			placas2_txt.writelines(plate2)
		placas2_txt.close()


os.system('python parce.py')


    
