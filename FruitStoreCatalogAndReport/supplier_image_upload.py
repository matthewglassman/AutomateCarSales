#!/usr/bin/python3

import requests
import os

#TODO Traverse files in path
path = "<pathtoimages>"  #EX. /home/<user>/images/

url = "https://httpbin.org/post"

folder = os.listdir(path)
for imagefile in folder:
	with open(path + imagefile, 'rb') as image: #Read as binary
		#print(image)

#TODO Upload files to online location
		r = requests.post(url, files={'file': image})
