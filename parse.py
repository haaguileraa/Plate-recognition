import os

os.environ["PARSE_API_ROOT"] = "http://3.16.42.236:80/parse"


from parse_rest.datatypes import File
from parse_rest.connection import register
from parse_rest.user import User

APPLICATION_ID = 'APPID'
REST_API_KEY = 'RESTAPIK'
MASTER_KEY = 'MASTERK'

register(APPLICATION_ID, REST_API_KEY, master_key=MASTER_KEY)

u = User.login("test_user", "1234567890")


from parse_rest.datatypes import File

#plateToMatch='"plate": ' 
u.carLicensePlate=''



with  open('placas2.txt', 'r+') as placas_txt:
	for line in placas_txt:
		#if plateToMatch in line:
		u.carLicensePlate = line
		print(u.carLicensePlate)
		u.save()
	
