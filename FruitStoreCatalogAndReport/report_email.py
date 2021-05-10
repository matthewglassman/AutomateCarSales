#!/usr/bin/python3

#Import Modules needed
import reports
import emails
import datetime
import os 

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
	attachment = '/tmp/processed.pdf'
	#Come back to creating PDF Report

	#Send email
	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ.get('USER'))
	subject = "Upload Completed - Online Fruit Store"
	body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	message = emails.generate(sender, receiver, subject, body, attachment)
	emails.send(message)

if __name__ == "__main__":
	main(sys.argv)