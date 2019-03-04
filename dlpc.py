# -*- coding: utf-8 -*-
import subprocess
import tempfile


Bild= 'plate_recognition.py'
Video= 'alpr_video.py'


## You can modify these:
N_API='b94e5931100d7f8464d029fb8be37960e3ad520a'
mode=  Bild #Video
Ort_v= '../../video/addr'
Ort_f= '../../photo/addr'

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
    		
    		
    		for line in tempf :
    			if stringToMatch in line:
    				matchedLine = line
    				print matchedLine
    				with open("placas.txt", "a") as text_file:
    					text_file.writelines(matchedLine + "\r\n") 
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
		
		
		for line in tempf :
    			if stringToMatch in line:
    				matchedLine = line
    				print matchedLine
    				with open("placas.txt", "a") as text_file:
    					text_file.writelines(matchedLine + "\r\n") 
 					#file.write(matchedLine "%d\r\n" % )
 					text_file.close()
 				
	
			elif stringError in line: 
				print error
				
			

	
    #	elif stringToMatch not in tempf:
    #		print error
    #		print tempf
    		
    		 
 	#continue
    		
    #	elif  stringToMatch not in line:
    
	#	print("Error");
		
 
   
   
    
