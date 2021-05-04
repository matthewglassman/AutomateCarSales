#!/usr/bin/python3

#Import Modules needed
import reports
import emails
import datetime

#Will send use reports.py and emails.py to create the actual PDF and email to send out

#Create date to pass to title

#First get the whole date into a variable
currentdate = datetime.datetime.now()

#Pull out each part of the date needed
currentmonth = currentdate.strftime("%B")
currentday = currentdate.strftime("%d")
currentyear = currentdate.strftime("%Y")
fulldate = currentmonth + " " + currentday + ", " + currentyear
def main(argv):
	#Generate PDF Report
	title = "Processed Update on " + fulldate