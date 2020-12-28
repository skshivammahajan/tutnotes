#!/usr/bin/env

import csv 
import requests 
import xml.etree.ElementTree as ET 
import pandas as pd
from zipfile import ZipFile
import boto3
from botocore.exceptions import NoCredentialsError

# URL from which xml will be downloaded
URL = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2020-01-08T00:00:00Z+TO+2020-01-08T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"
# File in which downloaded XML from url will be saved
XML_DOWNLOAD_FILE_NAME = "Download_Data.xml"
# File in whcih Downloaded url will be saved in CSV form
XML_CONVERT_CSV = "Xml_Downloaded.csv"
# File in which finals XML data will be saved in csv form
DATA_XML = "Data_Parsed_XML.csv"

# AWS Security Credentials
ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXX'
SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXX'
AWS_S3_BUCKET = "shivdatahub"


def extract_zip(file_name):
    """"
    Extract the xml from the zip.

    Parameters
    ----------
    file_name : str
        The name of the zip folder to be extracted
    """
    with ZipFile(file_name, 'r') as zip: 
        zip.printdir() 
        print('Extracting ... {}'.format(file_name)) 
        zip.extractall() 


def load_zip(df): 
    """"
    From the xml, parse through to the first download link whose file_type is DLTINS and download the zip

    Parameters
    ----------
    df : DataFrame
        XML dataframe
    """
    try:
        for row in df.iterrows():
            url = row[1]["download_link"]
            file_name = row[1]["file_name"] 
            if row[1]["file_type"] == "DLTINS":
                # creating HTTP response object from given url 
                resp = requests.get(url) 
                # saving the xml file 
                with open(file_name, 'wb') as f: 
                    f.write(resp.content) 
                    print("File Saved {} from Url {}.".format(file_name, url))
                    # Extracting Zip
                    extract_zip(file_name)
                    return file_name.replace("zip", "xml")
    except Exception as ex:
        print(ex)
        return False
            

def savetoCSV(dataitems, filename): 
    """"
    Save data into csv file

    Parameters
    ----------
    dataitems : list of dict
    filename: str
    """
    df = pd.DataFrame(dataitems)
    df.to_csv(filename, index=False)
    print("\nExtracted XML saved in file {}\n".format(filename))
    return df


def load_xml_from_url(url):
    """
    Download the xml from url link
    
    Parameters
    ----------
    url: str
    """
    try:
        resp = requests.get(url) 
        with open(XML_DOWNLOAD_FILE_NAME, 'wb') as f: 
            f.write(resp.content)
            print("Data Downloaded Successfully from url {} and \nsaved in {} file".format(url, XML_DOWNLOAD_FILE_NAME))
            return True
    except Exception as ex:
        print(ex)
        return False


def parseXML(xml_file): 
    """
    Parse Downloaded XML into CSV
    
    Parameters
    ----------
    xml_file: str
    """
    tree = ET.parse(xml_file) 
    root = tree.getroot() 
    dataitems = []
    for item in root.findall('./result/doc'):
        data = {} 
        for child in item:  
            data[child.attrib["name"]] = child.text
        dataitems.append(data) 

    df = savetoCSV(dataitems, XML_CONVERT_CSV) 
    return df

def parse_unzip_xml(xml_file): 
    """
    Convert the contents of the xml into a CSV with the required header:
    
    Parameters
    ----------
    xml_file: str
    """
    tree = ET.parse(xml_file) 
    root = tree.getroot() 
    dataitems = []
    try:
        for item in root.findall(r'./{urn:iso:std:iso:20022:tech:xsd:head.003.001.01}Pyld/{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Document/{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FinInstrmRptgRefDataDltaRpt/{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FinInstrm'):
            data = {} 
            issr = item.getchildren()[0].getchildren()[1].text 
            data["ISSR"] = issr
            FinInstrmGnlAttrbts = item.getchildren()[0].getchildren()[0].getchildren()
            for attrib in FinInstrmGnlAttrbts:
                data["FinInstrmGnlAttrbts." + attrib.tag.rsplit("}")[-1]] = attrib.text
            dataitems.append(data)
        savetoCSV(dataitems, DATA_XML)
        return True
    except Exception as ex:
        print(ex)
        return False


def upload_to_aws(local_file, bucket, s3_file):
    """
    Upload the csv in an AWS S3 bucket
    
    Parameter:

    local_file: str
    bucket: str 
    s3_file: str

    """
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


def process_data(url): 
    # Download the xml from link
    load_xml_from_url(url) 
    # parse xml file 
    df = parseXML(XML_DOWNLOAD_FILE_NAME)
    # From the xml, parse through to the first download link whose file_type is DLTINS and download the zip
    xml_file_name = load_zip(df) 
    # Convert the contents of the xml into a CSV 
    if xml_file_name is not False:
        parse_unzip_xml(xml_file_name)
        # Store the csv in an AWS S3 bucket
        upload_to_aws(DATA_XML, AWS_S3_BUCKET, DATA_XML)


if __name__ == "__main__": 
    process_data(URL)
   
    