import csv 
import requests 
import xml.etree.ElementTree as ET 
import pandas as pd
from zipfile import ZipFile


def extract_zip(file_name):
	# opening the zip file in READ mode 
	with ZipFile(file_name, 'r') as zip: 
	    # printing all the contents of the zip file 
	    zip.printdir() 
	  
	    # extracting all the files 
	    print('Extracting ... {}'.format(file_name)) 
	    zip.extractall() 
	    print('Done!')


def load_zip(df): 
	for row in df.iterrows():
		url = row[1][0]
		file_name = row[1][1] 
		# creating HTTP response object from given url 
		resp = requests.get(url) 
		# # saving the xml file 
		with open(file_name, 'wb') as f: 
			f.write(resp.content) 
			print("File Saved {} from Url {}.".format(file_name, url))
			extract_zip(file_name)
		

def parseXML(xmlfile): 
	# create element tree object 
	tree = ET.parse(xmlfile) 
	# get root element 
	root = tree.getroot() 
	# create empty list for data items 
	dataitems = [] 

	# iterate data items 
	for item in root.findall('./result/doc'):
		# empty data dictionary 
		data = {} 
		# iterate child elements of item 
		for child in item: 	
			# special checking for namespace object content:media 
			if child.attrib["name"] == 'file_type': 
				data['file_type'] = child.text
			if child.attrib["name"] == 'download_link': 
				data['download_link'] = child.text
			if child.attrib["name"] == 'file_name': 
				data['file_name'] = child.text
		# append data dictionary to data items list 
		dataitems.append(data) 
	# return data items list 
	return dataitems 


def savetoCSV(dataitems, filename): 
	df = pd.DataFrame(dataitems)
	df.to_csv(filename, index=False)
	print("\nExtracted XML saved in file {}\n".format(filename))
	return df

def load_xml_from_url(url, file_name):
	print("Downloading XML from :", url)
	resp = requests.get(url) 
	# # saving the xml file 
	with open(file_name, 'wb') as f: 
		f.write(resp.content)
		print("\nData Saved Successfully in {}".format(file_name))
		return True
	return False 
	

def main(url): 
	# Input Data File saving xml from web link
	IP_DATA_FILE = "Data.xml"
	# Filename for filtered data to be saved.
	OP_DATA_FILE = 'Extracted_Data.csv'

	# load xml from web 
	code = load_xml_from_url(url, IP_DATA_FILE) 
	if code:	
		# parse xml file 
		dataitems = parseXML(IP_DATA_FILE) 
		# # store data items in a csv file 
		df = savetoCSV(dataitems, OP_DATA_FILE) 
		load_zip(df) 
	
	
if __name__ == "__main__": 
	URL = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2020-01-08T00:00:00Z+TO+2020-01-08T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"
	# calling main function 
	main(URL) 
