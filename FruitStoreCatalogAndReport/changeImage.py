#!/usr/bin/python3

#Convert images from in list of files using PIL

import sys
import os
from pathlib import Path
from PIL import Image

#TODO Set size
size = (400, 600)

#TODO Set input and output
for infile in os.listdir("<path to files>"):						#For files in path
	outfile = os.path.splitext(infile) [0]		#Get file and extension


#Try Opening and converting file from TIF to JPEG and save
	try:
		with Image.open(infile).convert('RGB') as im:
			im.thumbnail(size)
			im.save("<path_to_be>" + outfile, "JPEG")
	except OSError:
		pass	