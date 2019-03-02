# -*- coding: utf-8 -*-
import subprocess
import tempfile
import shlex

## You can modify these:
N_API='YOURAPI'
mode='alpr_video.py'  # 'plate_recognition.py'
ff='0'  #First fotogramm
ef='10' #Last fotogram
jf='2'  #Jump between fotogramms
Ort= '../../photo/addr'

#____________DON'T CHANGE___________#
#	           |
#	           v



stringToMatch = '"plate": ' #What do you want to search
matchedLine = ''



with tempfile.TemporaryFile() as tempf:
    proc = subprocess.Popen(['python', mode, '--api', N_API, '--start', ff, '--end', ef, '--skip', jf, Ort], stdout=tempf)
    proc.wait()
    tempf.seek(0)
    #print tempf.read() #Want to print everything? uncomennt
    
  
    for line in tempf :
    	if stringToMatch in line:
    		matchedLine = line
    		print matchedLine
    		with open("plates.txt", "a") as text_file:
    			text_file.writelines(matchedLine + "\r\n") 
 		#file.write(matchedLine "%d\r\n" % )
 			text_file.close()
    		
    		 
 	#continue
    		
    #	elif  stringToMatch not in line:
    
	#	print("Error");
		
   
   
   
    
