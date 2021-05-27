#!/usr/bin/python3

#Import modules needed
import email
import mimetypes
import os.path
import smtplib


#Layout for email to be sent
def generate(sender, recipient, subject, body, attachment_path):
	"""Creates an email with an attachment."""

#Basic Email Layout
	message = email.message.EmailMessage()
	message["From"] = sender
	message["To"] = recipient
	message["Subject"] = subject
	message.set_content(body)

#Process (optional) attachment and add to email
	if not attachment_path == "":
		attachment_filename = os.path.basename(attachment_path)
		mime_type, _ = mimetypes.guess_type(attachment_path)
		mime_type, mime_subtype = mime_type.split('/', 1)

		with open(attachment_path, 'rb') as ap:
			message.add_attachment(ap.read(),
				maintype=mime_type,
				subtype=mime_subtype,
				filename=attachment_filename)

	return message

#Define how to send email using server
def send(message):
	"""Sends the message to the configured SMTP server."""
	mail_server = smtplib.SMTP('localhost')
	mail_server.send_message(message)
	mail_server.quit()