#!/usr/bin/python3

import requests
import os
import path

#TODO Traverse files in path
path = "<path_to_photo_files>"  #EX. /home/<user>/images/

url = "http://localhost/upload/"

folder = os.listdir(path)
for imagefile in folder:
	with open(path + imagefile, 'rb') as image: #Read as binary
	

#TODO Upload files to online location
	r = requests.post(url, files={'file': image})