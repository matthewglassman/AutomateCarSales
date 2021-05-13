#!/usr/bin/python3

#Import Modules Needed
import json
import requests
import os
import path

"""Will convert text files to dictionary and then into JSON to send to web"""

#TODO Create path to text files and traverse through files adding entries to a dictionary
path = "<path to text files to iterate>"

keys = ["name", "weight", "description", "image_name"]

folder = os.listdir(path)

#Iterate over the objects and build a dictionary
for file in folder:
	keycount = 0
	fruit = {}
#POST JSON Object to onlne location
