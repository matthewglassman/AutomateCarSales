#!/usr/bin/python3

#Import modules needed to render PDF

from reportlab.playtpus import SimpleDocTemplate
from reportlab.playtpus import Paragraph, Space, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

#Module that describes how PDF should be rendered
def generate_report(filename, title, additional_info):
	styles = getSampleStylesheet()
	report = SimpleDocTemplate(filename)
	report_title = Paragraph(title, styles["hi"])
	report_info = Paragraph(additional_info, style["BodyText"])
	
	empty_line = Spacer(1,20)
	
	report.build([report_title, empty_line, report_info, empty_line])