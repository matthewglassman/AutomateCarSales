#!/usr/bin/python3

#Import modules needed to render PDF

from reportlab.playtpus import SimpleDocTemplate
from reportlab.playtpus import Paragraph, Space, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

#Module that describes how PDF should be rendered
def generate_report(filename, title, additional_info, table_data):
	styles = getSampleStylesheet()
	report = SimpleDocTemplate(filename)
	report_title = Paragraph(title, styles["hi"])
	report_info = Paragraph(additional_info, style["BodyText"])
	table_style = [('GRID', (0,0), (-1,-1), 1, colors.black), ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), ('ALIGN', (0,0), (-1,-1), 'CENTER')]
	report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
	empty_line = Spacer(1,20)
	report.build([report_title, empty_line, report_info, empty_line, report_table])